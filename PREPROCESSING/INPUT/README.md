# DNABERT Preprocessing
## DP1. DNABERT Finetuning용 형식으로 변경
- DNABERT input 형식:  sequence, label
- 비병원성 데이터와 병원성 데이터에 각각 적용
- WT_seq과 Mut_seq을 pair로 넣어주기 위해 ```[CLS] WT_seq [SEP] Mut_seq [SEP]``` 형식 사용

```bash
python DP1.tsv_to_DNABERT_input_format.py M3.COSMIC_final.tsv D1.COSMIC_DNABERT.tsv
python DP1.tsv_to_DNABERT_input_format.py M3.Clinvar_final.tsv D1.Clinvar_DNABERT.tsv
```
    
## DP2. 병원성 데이터와 비병원성 데이터 병합하기 (undersampling)
- 병원성 변이가 더 적으므로 병원성 변이 수에 맞추어 undersampling 및 shuffling 해주었다.
- 반드시 line수가 더 많은 데이터(비병원성)를 ```sys.argv[2]``` 자리에 넣어주어야 한다.
- 이 과정에서 tsv 파일이 csv로 변경된다.

```bash
python D2.undersampling.py D1.COSMIC_DNABERT.tsv D1.Clinvar_DNABERT.tsv D2.undersampling.csv
```

## DP3.  train.csv, dev.csv, test.csv로 split
- train : dev : test = 70 : 15 : 15 비율로 나눠준다.

```bash
python DP3.split_train_dev_test.py D2.undersampling.csv train.csv dev.csv test.csv
```
