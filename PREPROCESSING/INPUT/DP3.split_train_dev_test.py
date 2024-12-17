import pandas as pd
import sys
from sklearn.model_selection import train_test_split

def split_csv(input_file, train_file, dev_file, test_file, train_ratio=0.7, dev_ratio=0.15, test_ratio=0.15):
    """
    CSV 파일을 train, dev, test로 나눕니다.

    Parameters:
        input_file (str): 전체 데이터가 담긴 CSV 파일 경로
        train_file (str): train 데이터 저장 경로
        dev_file (str): dev 데이터 저장 경로
        test_file (str): test 데이터 저장 경로
        train_ratio (float): train 데이터 비율 (default: 0.7)
        dev_ratio (float): dev 데이터 비율 (default: 0.15)
        test_ratio (float): test 데이터 비율 (default: 0.15)
    """
    # 입력 데이터 읽기
    df = pd.read_csv(input_file)

    # 데이터 나누기
    train_size = train_ratio
    dev_size = dev_ratio / (dev_ratio + test_ratio)  # dev와 test는 나머지 비율로 다시 나눔

    train_data, temp_data = train_test_split(df, test_size=1-train_size, random_state=42)
    dev_data, test_data = train_test_split(temp_data, test_size=1-dev_size, random_state=42)

    # 데이터 저장
    train_data.to_csv(train_file, index=False)
    dev_data.to_csv(dev_file, index=False)
    test_data.to_csv(test_file, index=False)

    print(f"Data split completed:\nTrain: {len(train_data)} rows\nDev: {len(dev_data)} rows\nTest: {len(test_data)} rows")

if __name__ == "__main__":
    # 사용법: python script.py input_file train_file dev_file test_file
    input_file = sys.argv[1]  # 전체 데이터 파일
    train_file = sys.argv[2]  # train 데이터 파일 경로
    dev_file = sys.argv[3]    # dev 데이터 파일 경로
    test_file = sys.argv[4]   # test 데이터 파일 경로

    # 비율은 기본값 사용 (70% train, 15% dev, 15% test)
    split_csv(input_file, train_file, dev_file, test_file)
