'''
[ 코드 설명 ]
vcf to tsv 코드

주요 정보 : INFO 필드에 존재
-> columns 으로 변경
-> Parsing에 필요한 정보들만 가져옴 (나머지 pass)
'''


import pandas as pd
import sys

# VCF 파일 경로
vcf_file = sys.argv[1] # clinvar.vcf
out_file = sys.argv[2] # clinvar_vcf.tsv

data = []
with open(vcf_file, 'r') as file:
    for line in file:
        if line.startswith('#'):  # 헤더 제외
            if line.startswith('#CHROM'):
                header = line.strip().split('\t')
            continue
        data.append(line.strip().split('\t'))

# 기본 DataFrame 생성
df = pd.DataFrame(data, columns=header)

# INFO 필드 파싱
info_data = []
for row in df['INFO']:
    info_dict = {key: value for item in row.split(';') for key, value in [item.split('=')] if '=' in item}
    info_data.append(info_dict)
info_df = pd.DataFrame(info_data).fillna('')

# DataFrame 병합
df = pd.concat([df.drop(columns=['INFO']), info_df], axis=1)

# 필요한 컬럼 리스트
columns_to_keep = [
    '#CHROM', 'POS', 'ID', 'REF', 'ALT', 'CLNDN', 'CLNHGVS', 'CLNREVSTAT', 'CLNSIG', 'CLNVC', 'MC', 'CLNSIGCONF', 'CLNVI'
]

# 필요한 컬럼만 선택
filtered_df = df[columns_to_keep]
print(filtered_df)
print(filtered_df.columns)

# TSV로 저장
filtered_df.to_csv(out_file, sep='\t', index=False)