## UOS-NLP-PROJECT (BIONLP)

---

## 1. 배경 & 목적


---

- 프로젝트명 : Pathogenicity Classification with Cancer Sequence Data
- 목적 : Bioinformatics와 NLP 기술을 접목하여 유전사 서열 기반 정확도가 높은 병원성 예측 모델 개발
- 배경 : 서열 정보를 이용한 병원성 변이 분석은 암 진단을 위한 기초 분석으로써 인간의 질병 연구 및 정밀 치료에 기여

## 2. 주최/주관 & 참가 대상 & 성과

---

- 주최: ???
- 참가대상 : 
- 평가지표 : 
- 성과: 

## 3. 프로젝트 기간

---

- 프로젝트 기간 : 2024.09. ~ 2024.12.
- 프로젝트 발표일 : 2024.12.18.(수)

## 4. 내용

---




## 5. 담당 역할

---

- 박자영 : 모델 및 주제 정리, ClinVar Data 전처리, 결과 분석, PPT 제작
- 신민경 : COSMIC Data 전처리, 주요 베이스라인 코드 구축, 결과 분석


## 6. 프로젝트 구성

---

### 6-1. Introduction
[주제 선정 배경]
- 주제 :
  

[데이터 소개]


[Bioinformatics 개념]


[NLP 개념]


 
### 6-2. Methodology
- DNABERT :
- ML : XGBoost, LightGBM, Ensemble


### 6-3. Data Preprocessing
[???]
PREPROCESSING > COSMIC, CLINVAR, INPUT 디렉토리의 READ ME 참조

### 6-4. Model Train
[Train Model] 


[Hyper Parameter] 


### 6-5. Results & Discussion
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
- 


## 7. 자료
---

- PPT

- 코드

- 데이터



## 8. 프로젝트 소감

---


| 이름 | 소감 |
| --- | --- | 
| 박자영 | -- |
| 신민경 | -- |

## 9. Citation
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