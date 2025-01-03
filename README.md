## UOS-NLP-PROJECT (BIONLP)

---

## 1. 배경 & 목적


---

- 프로젝트명 : Pathogenicity Classification with Cancer Sequence Data
- 목적 : Bioinformatics와 NLP 기술을 접목하여 유전사 서열 기반 정확도가 높은 병원성 예측 모델 개발
- 배경 : 서열 정보를 이용한 병원성 변이 분석은 암 진단을 위한 기초 분석으로써 인간의 질병 연구 및 정밀 치료에 기여

## 2. 프로젝트 기간

---

#### 프로젝트 기간 : 2024.10 ~ 2024.12
- 10월 : 아이디어 탐색 및 주제 선정
- 11월 : DATASET 구축
- 12월 : NLP Model 구축
#### 프로젝트 발표일 : 2024.12.18.(수)



## 3. 담당 역할

---

- 박자영 : 모델 및 주제 정리, ClinVar Data 전처리, 결과 분석, PPT 제작
- 신민경 : COSMIC Data 전처리, 모델 주요 베이스라인 코드 구축, 결과 분석


## 4. 프로젝트 구성

---

### 4-1. Introduction
[주제 선정 배경]
- 주제 : 병원성 변이 분류를 위한 DNABERT 기반 분류 모델 개발
인가의 질병 및 치료 연구의 토대가 될 수 있는 병원선 변이 분류를 위한 모델 개발을 목적으로 함.
기존 레퍼런스들보다 발전된 NLP 모델을 사용해보는 것을 목표로 하며, 병원성 변이 분류를 기반으로 암 질환 분류 혹은 진단 관련 모델 제작을 후속 목표로 수립.
  
[데이터 소개]
- COSMIC (병원성 변이 정보 획득 경로)
  : 암 유전체 연구를 위해 수집된 체세포 돌연변이 데이터베이스로, 암과 관련된 유전자 변이를 포함
- ClinVar (양성 변이 정보 획득 경로)
  : 유전자 변이와 임상적 중요성(질병 연관성 등)을 연계하여 제공하는 공개 데이터베이스

[Bioinformatics 개념]
: 생물학적 데이터를 분석하고 해석하기 위해 컴퓨터 과학, 통계학, 수학을 결합한 학문
- 유전자 서열, 단백질 구조, 유전체 데이터 등을 처리하여 질병의 원인 규명이나 신약 개발 등에 활용
- 다양한 알고리즘과 데이터베이스를 기반으로 생명 현상을 정량적으로 분석하고 예측하는 데 중점을 두는 학문

[NLP, LLM 개념]
: NLP (인간의 언어를 컴퓨터가 이해하고 처리할 수 있도록 하는 인공지능의 한 분야)
  - 텍스트와 음성 데이터를 분석하여 번역, 요약, 감정 분석, 질문 응답 등 다양한 언어 기반 작업 수행
  - 형태소 분석, 구문 분석, 시멘틱 해석과 같은 기술이 사용 (전통적)
  - 최근에는 딥러닝 기반의 모델 주로 활용
: LLM (대규모 언어 모델; Large Language Model)
  - 대량의 텍스트 데이터를 학습하여 언어의 맥락과 의미를 이해하고 생성할 수 있는 인공지능 모델 (GPT, BERT, T5 등)
  - 초거대 모델은 수십억에서 수조 개의 매개변수를 통해 더 정교한 언어 생성과 해석 가능
  - 번역, 생성, 질의응답 등 다양한 작업에서 뛰어난 성능


### 4-2. Methodology
- DNABERT-2 (BERT를 기반으로 개발된 생물정보학 도구)
  : DNA 서열의 특징을 학습하여 변이 예측, 병원성 분석 등에 활용
  : ver1에서는 k-mer 토큰화를 적용하여 DNA 서열 데이터를 처리하나 ver2에서는 BPE 토큰화 활용
- ML : XGBoost, LightGBM, Ensemble

[모델 구성]
1. DNABERT에 염기서열 정보를 입력하여 Feature Vector 추출 (자체적 Classification도 진행)
2. Feature Vector를 ML Ensemble 모델의 입력값으로 사용
3. 병원성 여부 Binary Classification 진행

### 4-3. Data Preprocessing, Model Train
PREPROCESSING > COSMIC, CLINVAR, INPUT 디렉토리의 READ ME 참조
MODEL > DNABERT, Classification 디렉토리 READ ME 참조

### 4-5. Results & Discussion
[모델 성능]
Ensemble 기준
- Accuracy: 94%
- AUC: 97%

[한계점 및 개선 방향]
한계점: overfitting

원인
- undersampling으로 인한 절대적인 데이터 부족
- 병원성 데이터(COSMIC)와 비병원성 데이터(Clinvar)의 분포 차이

개선 방향
- 추가적인 데이터 확보 및 데이터 불균형 해소
- SNV 외에도 indel, frameshift 등 다양한 변이 정보를 추가적으로 활용
- 분포가 다른 데이터셋을 test set으로 활용하여 일반화 성능 검사 필요

[의의]
- 프로젝트 설계, 데이터 수집부터 모델링까지 모두 직접 진행한 첫 프로젝트
- 생물정보학 분야에서 사용할 수 있는 분석의 토대 마련


## 5. 프로젝트 소감

---


| 이름 | 소감 |
| --- | --- | 
| 박자영 | Bioinformatics 분야를 접한지 얼마 되지 않은 시점에서 관련 도메인 지식을 가지고 처음으로 진행한 대형 프로젝트였다. 결과 부분에서 아쉬움이 존재하지만, 기회가 된다면 성능 개선과 후속 연구를 이어나가보고 싶은 마음이다. 이번 프로젝트를 계기로 Biomedical AI 분야에 입성하고자 한다.|
| 신민경 | -- |

## 6. Citation
DNABERT-2
    @misc{zhou2023dnabert2,
      title={DNABERT-2: Efficient Foundation Model and Benchmark For Multi-Species Genome}, 
      author={Zhihan Zhou and Yanrong Ji and Weijian Li and Pratik Dutta and Ramana Davuluri and Han Liu},
      year={2023},
      eprint={2306.15006},
      archivePrefix={arXiv},
      primaryClass={q-bio.GN}
    }

UBAI
    본 프로젝트는 서울시립대학교 도시과학빅데이터·AI연구원의 슈퍼컴퓨팅 자원을 지원 받아 수행되었습니다.
    The authors acknowledge the Urban Big Data and AI Institute of the University of Seoul supercomputing resources (http://ubai.uos.ac.kr) made available for conducting the research reported in this project.
