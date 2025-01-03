## DATASET
#### [ 다운 필요 목록 ]
**ClinVar**
> ```https://www.ncbi.nlm.nih.gov/clinvar/docs/maintenance_use/#download``` 링크를 통해 전반적인 파일 다운 가능 

**clinvar.vcf**
> ```https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/``` 링크에서 **clinvar.vcf.gz** 다운로드
> 
> ```$ gzip -d {압축 파일}.gz``` 압축 해제 후 사용

**GRCh38 version FASTA file**
> ```https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001405.26/```
>
> ```Download``` > ```all``` > ```Genome sequences (FASTA)```
<br>
<br>

## 01make_tsv.py

#### [ 코드 설명 ]
**vcf to tsv 코드**
> vcf 의 주요 정보 : INFO 필드에 존재
> - INFO 필드를 tsv 파일의 columns 으로 변경
> - 이때, Parsing에 필요한 정보들만 사용 (나머지는 tsv 파일로 저장하지 않음)
<br>

#### [ 사용법 ]
```
$ python3 01make_tsv.py clinvar.vcf(input 파일) clinvar_vcf.tsv(output 파일; 원하는 이름)
```
<br>
<br>

## 02parsing.py
#### [ 코드 설명 ]
**tsv 파일 토대로 원하는 변이 정보 parsing 코드 (양성변이 버전)**
> 아래 기준으로 Parsing
> - 신뢰성 있는 자료 (전문가의 의견, 논문 기재, 연구 결과 존재 등등; CLNREVSTAT 컬럼) 
> - 양성 정보 (CLNSIG 컬럼)
> - SNV 정보 (CLNVC 컬럼)
> - 특수 레퍼런스 제거 (미토콘드리아 등; #CHROM 컬럼)
<br>

#### [ 사용법 ]
```
$ python3 02parsing.py clinvar_vcf.tsv(input 파일) first_preprocessing.tsv(output 파일; 원하는 이름)
```
<br>
<br>

## 03row_input.py
#### [ 코드 설명 ]
**DNABERT input 제작을 위한 전단계 전처리 코드**
> GRCh38에서 CLNHGVS 정보에 따른 서열값 가져옴 (ex.NC_000001.11:g.69134A>G 형태 변이 위치 정보)
> - 변이 위치 기준 양쪽 100bp parsing
> - 총 201bp
> - WT, 변이 서열 모두 제작

> 양성 변이 라벨 : 0
> - 칼럼 아래와 같이 준비
> ```    "Variant_ID": row["ID"],
>     "WT_NT_Sequence": str(seq_region),
>     "Mutated_NT_Sequence": str(mutated_seq),
>     "Position_HGVSC": row["CLNHGVS"],
>     "Pathogenicity": 0
> ```
<br>

#### [ 사용법 ]
```
$ python3 03row_input.py first_preprocessing.tsv(input 파일) GCF_000001405.40_GRCh38.p14_genomic.fna(저장한 전체 genome fasta 파일) ClinVar_final_sequences.tsv(output 파일; 원하는 이름)
```
<br>
<br>

## 참고 내용
#### ```~_p``` 파일의 경우 병원성 변이 정보를 Parsing 하는 코드
#### ```conda install -c conda-forge biopython``` 필요
