import pandas as pd
import sys

def filter_by_tier_1_with_header(census_file, filtering_file, output_file):
    # CancerGeneCensus.tsv 불러오기
    census_data = pd.read_csv(census_file, sep='\t')

    # TIER 열이 1인 유전자의 COSMIC_GENE_ID만 추출
    tier_1_ids = census_data[census_data['TIER'] == 1]['COSMIC_GENE_ID']

    # T1.filtering.tsv 불러오기 
    filtering_data = pd.read_csv(filtering_file, sep='\t')

    # T1.filtering.tsv에서 COSMIC_GENE_ID가 Tier 1 목록에 있는 행들만 필터링
    filtered_data = filtering_data[filtering_data['COSMIC_GENE_ID'].isin(tier_1_ids)]

    # 필터링된 데이터를 헤더와 함께 출력 파일로 저장
    filtered_data.to_csv(output_file, sep='\t', index=False, header=True)
    print(f"Filtered data saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <CancerGeneCensus.tsv> <3.filtering.tsv> <output_file>")
        sys.exit(1)

    census_file = sys.argv[1]
    filtering_file = sys.argv[2]
    output_file = sys.argv[3]

    filter_by_tier_1_with_header(census_file, filtering_file, output_file)
