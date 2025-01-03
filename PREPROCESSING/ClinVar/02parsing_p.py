'''
[ 코드 설명 ]
tsv 파일 토대로 원하는 변이 정보 parsing 코드 (pathogenic 버전)

- 신뢰성 있는 자료 (전문가의 의견, 논문 기재, 연구 결과 존재 등등)
- 병원성 정보
- SNV 정보
- 특수 레퍼런스 제거 (미토콘드리아 등)

중복된 내용 여부에 대해서는 따로 EDA 진행함 (코드 삭제..)
'''

import pandas as pd
import sys

# VCF 파일 경로
vcf_file = sys.argv[1] # clinvar_vcf.tsv
out_file = sys.argv[2] # 'pathogenic_preprocessing.tsv'

clinvar_data = pd.read_csv(vcf_file, sep='\t')
# ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'CLNDN', 'CLNHGVS', 'CLNREVSTAT', 'CLNSIG', 'CLNVC', 'MC', 'CLNSIGCONF', 'CLNVI']


################################################################################
# CLNREVSTAT 불필요 원소 (행) 삭제
# 제외할 조건을 포함하는 CLNREVSTAT 값 정의
trusted_values = [
    "criteria_provided,_single_submitter",
    "criteria_provided,_multiple_submitters,_no_conflicts",
    "reviewed_by_expert_panel",
    "practice_guideline"
]
# CLNREVSTAT 값이 trusted_values에 해당하는 행만 유지
filtered_data = clinvar_data[clinvar_data['CLNREVSTAT'].isin(trusted_values)]


################################################################################
# CLNSIG 컬럼의 value_counts() -> txt 파일 제작 (더 자세히 확인하기 위해)
'''clnsig_counts = filtered_data['CLNSIG'].value_counts()

# 텍스트 파일로 저장
output_file = "CLNSIG.txt"
with open(output_file, 'w') as file:
    file.write(clnsig_counts.to_string())  # value_counts() 결과를 문자열로 변환하여 저장

print(f"CLNSIG value_counts() 결과가 '{output_file}' 파일로 저장되었습니다.")'''
# 병원성 분류 조건 정의
pathogenic_values = [
    "Pathogenic",
    "Likely_pathogenic",
    "Pathogenic/Likely_pathogenic",
    "Pathogenic|drug_response",
    "Likely_pathogenic/Likely_risk_allele",
    "Likely_pathogenic|drug_response",
    "Pathogenic/Likely_pathogenic/Pathogenic,_low_penetrance",
    "Likely_pathogenic,_low_penetrance"
]

# CLNSIG 값이 benign_values에 해당하는 행만 선택
filtered_data = filtered_data[filtered_data['CLNSIG'].isin(pathogenic_values)]


################################################################################
# single_nucleotide_variant (SNV)만 남기기
filtered_data = filtered_data[filtered_data['CLNVC'] == 'single_nucleotide_variant']
filtered_data = filtered_data[filtered_data['ALT'] != '.']

print(filtered_data['REF'].value_counts())
print(filtered_data['ALT'].value_counts())

# REF / ALT 값이 단일 염기인 경우만 남기기
# filtered_data = filtered_data[filtered_data['REF'].str.len() == 1]
# filtered_data = filtered_data[filtered_data['ALT'].str.len() == 1]


################################################################################
# 미토콘드리아 변이 제거 (필요한 경우)
# 미토콘드리아 및 특수 레퍼런스 시퀀스 제거 -> 살려야하면 나중에 살리기
# 'NT_', 'MT', 'NC_012920.1', 'NW_'로 시작하는 항목 필터링
special_references = filtered_data[filtered_data['#CHROM'].str.contains(r'^(MT|NC_012920\.1|NT_|NW_)', na=False)]
# 해당 항목 제거
filtered_data = filtered_data[~filtered_data['#CHROM'].str.contains(r'^(MT|NC_012920\.1|NT_|NW_)', na=False)]


# 특수 레퍼런스 시퀀스 출력
print("특수 레퍼런스 시퀀스 데이터:")
print(special_references)


################################################################################
##  추가 전처리에서 불필요한 컬럼 삭제
# '#CHROM'(염색체), 'POS'(위치), 'ID', 'REF'(원래), 'ALT'(변이)
# 'CLNDN'(질병), 'CLNHGVS'(HGVS 정보), 'CLNREVSTAT'(신뢰성), 'CLNSIG'(양성, 병원성)
# 'CLNVC'(돌연변이 종류), 'MC'(??), 'CLNSIGCONF'(내용 충돌), 'CLNVI'(출처)
### 이미 처리 완료한 컬럼 : CLNREVSTAT, CLNSIG, CLNVC, CLNSIGCONF
### 그냥 쓸모 없는 컬럼 : MC, CLNVI
# 삭제할 컬럼 정의
columns_to_drop = ['CLNREVSTAT', 'CLNSIG', 'CLNVC', 'CLNSIGCONF', 'MC', 'CLNVI']

# 지정한 컬럼 삭제
filtered_data = filtered_data.drop(columns=columns_to_drop)

# 결과 확인
print(filtered_data.head())
print(filtered_data.columns)

filtered_data.to_csv(out_file, sep='\t', index=False)