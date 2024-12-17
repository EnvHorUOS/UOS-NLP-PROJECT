import sys
import csv

def filter_cosmic_vcf(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')

        for row in reader:
            if row[0].startswith("#"):  # 헤더 스킵
                writer.writerow(row)
                continue

            # IS_CANONICAL 필터링
            info = row[7]  # INFO 필드
            # INFO 필드를 key=value 형태로 분리하고 딕셔너리로 변환
            info_dict = {}
            for item in info.split(';'):
                if '=' in item:
                    key, value = item.split('=', 1)  # '='를 기준으로 key, value 분리
                    info_dict[key] = value

            if info_dict.get('IS_CANONICAL') != 'y':
                continue

            # COSMIC ID 가공
            row[2] = row[2].split('_')[0]  # COSMIC ID 필드

            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filter_cosmic_vcf.py <input_vcf> <output_vcf>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    filter_cosmic_vcf(input_file, output_file)

