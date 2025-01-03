# 필요 라이브러리 : conda install -c conda-forge biopython

'''
[ 코드 설명 ]
DNABERT input 형태 전처리 코드

- GRCh38에서 CLNHGVS 정보에 따른 서열값 가져옴 (ex.NC_000001.11:g.69134A>G 형태 변이 위치 정보)
    - 변이 위치 기준 양쪽 100bp parsing
    - 총 201bp
    - WT, 변이 서열 모두 제작
- 병원성 변이 라벨 : 1

칼럼 아래와 같이 준비
    "Variant_ID": row["ID"],
    "WT_NT_Sequence": str(seq_region),
    "Mutated_NT_Sequence": str(mutated_seq),
    "Position_HGVSC": row["CLNHGVS"],
    "Pathogenicity": 1
'''

from Bio import SeqIO
from Bio.Seq import Seq
import pandas as pd
import sys

# 1. 데이터 불러오기
input_file = sys.argv[1]  # "pathogenic_preprocessing.tsv"
data = pd.read_csv(input_file, sep="\t")
print(f"Data shape: {data.shape}")  # 데이터 크기 출력

# FASTA 파일 경로
fasta_file = sys.argv[2]  # "GCF_000001405.40_GRCh38.p14_genomic.fna"

# 2. FASTA 파일 읽기
fasta_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))

# 0번째 key 확인
keys = list(fasta_dict.keys())
print("FASTA Keys (First 5):", keys[:5])  # 첫 5개 키 확인

# 결과 저장 리스트
results = []

# 3. 변이 처리 및 서열 추출
for index, row in data.iterrows():
    try:
        # CLNHGVS에서 변이 위치 가져오기
        hgvs = row['CLNHGVS']
                
        # 키 분리
        chrom, pos_ref_alt = hgvs.split(":g.")
        chrom = chrom.split(".")[0]  # 버전 제거

        # 키 매칭 확인
        matched_keys = [key for key in keys if chrom in key]
        if not matched_keys:
            raise ValueError(f"Chromosome {chrom} not found in FASTA keys.")

        # 적합한 키 선택
        fasta_key = matched_keys[0]

        # 변이 위치와 정보 추출
        pos = int(''.join(filter(str.isdigit, pos_ref_alt)))
        ref_base, alt_base = pos_ref_alt.split(str(pos))[-1].split(">")

        # 변이 위치를 기준으로 서열 추출 (앞뒤로 최대 100bp)
        ref_seq = fasta_dict[fasta_key].seq
        start = max(0, pos - 101)  # 변이 위치 기준 100bp 앞
        end = min(len(ref_seq), pos + 100)  # 변이 위치 기준 100bp 뒤

        seq_region = ref_seq[start:end].upper()  # 대문자로 변환

        # 변이 적용
        relative_pos = pos - start - 1
        if seq_region[relative_pos] != ref_base.upper():
            raise ValueError(f"Reference base mismatch at position {pos}: expected {ref_base}, found {seq_region[relative_pos]}")
        mutated_seq = seq_region[:relative_pos] + alt_base.upper() + seq_region[relative_pos + 1:]

        # 결과 저장
        results.append({
            "Variant_ID": row["ID"],
            "WT_NT_Sequence": str(seq_region),
            "Mutated_NT_Sequence": str(mutated_seq),
            "Position_HGVSC": row["CLNHGVS"],
            "Pathogenicity": 1
        })

    except Exception as e:
        print(f"Error processing row {index}: {e}")

# 4. 결과를 DataFrame으로 변환
output_df = pd.DataFrame(results)

# 5. TSV 파일로 저장
output_file = sys.argv[3] # "ClinVar_final_pathogenic.tsv" 
output_df.to_csv(output_file, sep="\t", index=False)

print(f"결과가 '{output_file}'로 저장되었습니다.")
