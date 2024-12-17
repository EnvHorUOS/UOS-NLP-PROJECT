import sys

filename = sys.argv[1] 

def filter_snv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # 주석 건너뛰기
            if line.startswith("##"):
                continue
            if line.startswith("#"):
                outfile.write(line)
                continue
            
            columns = line.strip().split('\t')
            
            # 8번째 열에 SO_TERM=SNV가 있는지 검사
            if len(columns) >= 8 and "SO_TERM=SNV" in columns[7]:
                outfile.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("사용법: python sfk.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        filter_snv(input_file, output_file)