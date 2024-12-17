import pandas as pd
import numpy as np
import sys

def sample_and_combine(pathogenic_file, non_pathogenic_file, output_file):
    # 파일 읽기
    df_pathogenic = pd.read_csv(pathogenic_file, sep="\t")
    df_non_pathogenic = pd.read_csv(non_pathogenic_file, sep="\t")
    
    # 병원성 데이터 개수
    sample_size = len(df_pathogenic)
    
    # 비병원성 데이터에서 랜덤 샘플링
    df_non_pathogenic_sampled = df_non_pathogenic.sample(n=sample_size, random_state=42)
    
    # 데이터 합치기
    combined_df = pd.concat([df_pathogenic, df_non_pathogenic_sampled], ignore_index=True)
    
    # 셔플링
    combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # 저장
    combined_df.to_csv(output_file, sep=",", index=False)
    print(f"Combined file saved as {output_file}")

if __name__ == "__main__":
    # 사용법: python script.py pathogenic_file non_pathogenic_file output_file
    pathogenic_file = sys.argv[1]  # 병원성 변이 파일
    non_pathogenic_file = sys.argv[2]  # 비병원성 변이 파일
    output_file = sys.argv[3]  # 출력 파일
    sample_and_combine(pathogenic_file, non_pathogenic_file, output_file)
