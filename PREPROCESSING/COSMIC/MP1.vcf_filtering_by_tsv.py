import pandas as pd
import sys

def filter_vcf_by_genomic_mutation_id(tsv_file, vcf_file, output_vcf):

    # TSV의 GENOMIC_MUTATION_ID 값 저장
    tsv_data = pd.read_csv(tsv_file, sep='\t')
    genomic_mutation_ids = set(tsv_data['GENOMIC_MUTATION_ID'])

    # VCF 파일을 읽고 필터링
    with open(vcf_file, 'r') as infile, open(output_vcf, 'w') as outfile:
        for line in infile:
            # 헤더 출력
            if line.startswith("#"):
                outfile.write(line)
                continue
            
            cols = line.strip().split("\t")
            info_field = cols[2]  # GENOMIC_MUTATION_ID 
            
            # GENOMIC_MUTATION_ID가 tsv 파일에 있는지 확인
            if info_field in genomic_mutation_ids:
                outfile.write(line)

    print(f"Filtered VCF saved to {output_vcf}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python filter_vcf_by_genomic_mutation_id.py <tsv_file> <vcf_file> <output_vcf>")
        sys.exit(1)

    tsv_file = sys.argv[1] 
    vcf_file = sys.argv[2] 
    output_vcf = sys.argv[3]

    filter_vcf_by_genomic_mutation_id(tsv_file, vcf_file, output_vcf)
