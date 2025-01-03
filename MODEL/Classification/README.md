## Binary Classification code
#### Train 과정에서 저장한 모델 가중치와 Feature Vector를 활용한 Classification Code
(저장 모델의 경우, 가장 성능이 높은 checkpoint 저장 가중치 값을 활용한다)
<br>
<br>

## onlyDNABERT
#### 1. DNABERT 모델 준비
   - ```!git clone https://github.com/MAGICS-LAB/DNABERT_2.git```
   - (허깅페이스 활용) ```from transformers import AutoTokenizer, AutoModelForSequenceClassification```
   - fine-tuning된 모델(사전에 저장한 모델 가중치) 불러오기
#### 2. Classification
   - 불러온 모델 활용 **분류** 진행 (코드 **Classification (onlyDNABERT)** 부분)
<br>

## ML
#### 1. 사전 학습 과정에서 미리 저장해둔 **Feature Vector** 불러오기
```
# 파일 경로 설정
train_feature_file = f"{base_path}/FeatureVector/train_features.npy"
train_label_file = f"{base_path}/FeatureVector/train_labels.npy"
dev_feature_file = f"{base_path}/FeatureVector/dev_features.npy"
dev_label_file = f"{base_path}/FeatureVector/dev_labels.npy"
test_feature_file = f"{base_path}/FeatureVector/test_features.npy"
test_label_file = f"{base_path}/FeatureVector/test_labels.npy"

# Train 및 Dev 데이터 로드
train_features = np.load(train_feature_file)
train_labels = np.load(train_label_file)
dev_features = np.load(dev_feature_file)
dev_labels = np.load(dev_label_file)

# Train-Dev 합치기
X_train = np.vstack((train_features, dev_features))
y_train = np.hstack((train_labels, dev_labels))

# Test 데이터 로드
X_test = np.load(test_feature_file)
y_test = np.load(test_label_file)```
```
#### 2. 이후 각 모델별로 import 해서 Classification 진행
#### 3. Ensemble의 경우 2개의 모델을 확률 기준 동일한 비율로 가져옴

<br>
<br>
