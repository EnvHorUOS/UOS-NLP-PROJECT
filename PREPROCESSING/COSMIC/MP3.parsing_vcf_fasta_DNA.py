import sys
import re
from Bio.Seq import Seq

def apply_mutations_and_save_nt_sequence(fasta_file, vcf_file, output_file):
    # FASTA 파일을 transcript 기준으로 저장
    sequences = {}
    strand_info = {}
    with open(fasta_file, 'r') as f:
        current_transcript = ""
        current_seq = ""
        for line in f:
            if line.startswith(">"):
                if current_transcript:
                    sequences[current_transcript] = current_seq
                header_parts = line.strip().split()
                current_transcript = header_parts[1]
                strand_match = re.search(r"\((\+|\-)\)", line)
                strand_info[current_transcript] = strand_match.group(1) if strand_match else "?"
                current_seq = ""
            else:
                current_seq += line.strip()
        if current_transcript:
            sequences[current_transcript] = current_seq

    # VCF 파일을 읽고 각 변이에 대해 염기 서열 추출
    with open(vcf_file, 'r') as vcf, open(output_file, 'w') as out_f:
        out_f.write("Variant_ID\tWT_NT_Sequence\tMutated_NT_Sequence\tPosition_HGVSC\tPathogenicity\n")
        for line in vcf:
            fields = line.split("\t")
            variant_id = fields[2]
            transcript = fields[7].split(";")[1].split("=")[1]
            hgvsc_info = re.search(r'HGVSC=([\w.]+):c\.(\d+)([ATCG])>([ATCG])', fields[7])

            if hgvsc_info and transcript in sequences:
                hgvsc_position = hgvsc_info.group(0)  # HGVSC 정보 그대로 사용
                original_pos = int(hgvsc_info.group(2)) - 1  # 변이는 0-기반 인덱스로 처리
                ref = hgvsc_info.group(3)
                alt = hgvsc_info.group(4)

                # 해당 transcript의 시퀀스를 복제하여 변이 적용
                original_seq = sequences[transcript]
                strand = strand_info.get(transcript, "?")

                # N 개수 보정
                n_count_before_pos = original_seq[:original_pos].count("N")
                corrected_pos = original_pos + n_count_before_pos

                # HGVSC는 원래 서열 기준으로 처리
                if corrected_pos < len(original_seq) and original_seq[corrected_pos] == ref:
                    mutated_seq = original_seq[:corrected_pos] + alt + original_seq[corrected_pos+1:]

                    # strand가 "-"일 경우 역상보 서열로 변환
                    if strand == "-":
                        # 역상보 변환
                        mutated_seq = str(Seq(mutated_seq).reverse_complement())
                        original_seq = str(Seq(original_seq).reverse_complement())

                    # 주변 100NT씩 자르기
                    start = max(0, corrected_pos - 100)
                    end = min(len(original_seq), corrected_pos + 101)
                    wt_nt_seq = original_seq[start:end]
                    mut_nt_seq = mutated_seq[start:end]

                    # 병원성 여부는 항상 1
                    pathogenicity = 1

                    # TSV 파일 저장
                    out_f.write(f"{variant_id}\t{wt_nt_seq}\t{mut_nt_seq}\t{hgvsc_position}\t{pathogenicity}\n")
                else:
                    print(f"Reference base mismatch at {transcript} corrected position {corrected_pos+1} for variant {variant_id}")

if __name__ == "__main__":
    # 사용법: python script.py fasta_file vcf_file output_file
    fasta_file = sys.argv[1]  
    vcf_file = sys.argv[2]    
    output_file = sys.argv[3] 
    apply_mutations_and_save_nt_sequence(fasta_file, vcf_file, output_file)
