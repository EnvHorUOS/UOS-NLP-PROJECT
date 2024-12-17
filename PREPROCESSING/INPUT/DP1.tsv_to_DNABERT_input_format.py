import sys
import pandas as pd

def transform_input_file(input_file, output_file):
    """
    입력 파일을 [CLS] WT_seq [SEP] Mut_seq [SEP] 형식의 sequence와 Pathogenicity 값을 label로 변환합니다.
    """
    # TSV 파일 읽기
    df = pd.read_csv(input_file, sep="\t")

    # sequence 열 생성
    df['sequence'] = "[CLS] " + df['WT_NT_Sequence'] + " [SEP] " + df['Mutated_NT_Sequence'] + " [SEP]"

    # label 열 생성
    df['label'] = df['Pathogenicity']

    # 필요한 열만 선택
    transformed_df = df[['sequence', 'label']]

    # 결과 파일 저장
    transformed_df.to_csv(output_file, sep="\t", index=False)

if __name__ == "__main__":
    # 사용법: python script.py input_file output_file
    input_file = sys.argv[1]  
    output_file = sys.argv[2]  
    transform_input_file(input_file, output_file)