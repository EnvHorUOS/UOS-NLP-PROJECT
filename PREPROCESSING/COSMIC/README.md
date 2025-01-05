# Input Dataset
- https://cancer.sanger.ac.uk/cosmic/download/cosmic
- COSMIC > v100 > GRCh38 데이터셋을 다운받아 다음과 같이 저장하였다.
- 0.CancerGeneCensus.tsv
- 0.CompleteTargetedScreensMutant_Normal.vcf
- 0.CompleteTargetedScreensMutant.tsv
- 0.Genes.fasta
<br>
<br>

# COSMIC Preprocessing
## 1. VCF_CODE : vcf 파일을 filtering 하기 위한 코드
### VP1. SNV변이만 출력
- SO_TERM == SNV 인 행만 filtering

```bash
python VP1.print_SNV_line.py 0.CompleteTargetedScreensMutant_Normal.vcf V1.SNV_output.vcf
```
<br>        

### VP2. exon영역 안의 변이만 출력
- 정규표현식 HGVSC=ENST00000378288.8:c.337C>T의 형식에 맞는 행만 출력

```bash
python VP2.print_CDS_mut_line.py V1.SNV_output.vcf V2.CDS_output.vcf
```
<br>
<br>

## 2. TSV_CODE : tsv file을 filtering 하기 위한 코드
### TP1. 임상정보가 존재하는 행 & 체세포 변이로 확인된 행만 출력
- 임상정보 존재: df["POSITIVE_SCREEN"] == "y”
- 체세포 변이로 확인: df["MUTATION_SOMATIC_STATUS"] != "Variant of unknown origin”

```bash
python TP1.filtering_not_positive_and_unknown.py 0.CompleteTargetedScreensMutant.tsv T1.filtering_output1.tsv
```
<br>    

### TP2. driver mutation일 확률이 높은 행만 출력
- CancerGeneCensus 기준 Tier 1인 gene에 해당하는 line 만 출력
- Tier 1의 의미: 암 발생과 직접적인 연관성이 과학적으로 확립된 유전자

```bash
python TP2.driver_filtering.py T1.filtering_output1.tsv T2.filtering_output2.tsv
```
<br>     
<br>

## 3. MERGE_CODE: filtering된 vcf 파일과 tsv 파일을 합쳐서 최종 input 형식으로 만드는 코드
### MP1. TSV와 VCF에 모두 포함된 mutation만 필터링(최종 파일 형태 : VCF)

```bash
python MP1.vcf_filtering_by_tsv.py T2.filtering_output2.tsv V2.CDS_output.vcf M1.merge_output.vcf
```
<br>     

### MP2. 주 전사체 정보만 남기기
- 전사체가 많은 유전자에 가중치가 가는 것을 방지하기 위해서 주 전사체만 남겨주기(IS_CANONICAL==y)

```bash
python MP2.main_transcript.py M1.merge_output.vcf M2.main_transcript.vcf
```
<br>     

### MP3. 서열과 위치 정보가 담긴 최종 정리 파일 만들기
- vcf 파일과 fasta 파일을 기반으로 변이 ID, 야생형 서열, 돌연변이 서열, HGVSC 정보, 병원성(0/1) 정보를 정리하여 tsv 파일로 저장하였다.
- HGVSC 정보와 fasta의 정보가 불확실한 서열(N)으로 인해 매칭되지 않는 것을 방지하기 위해 N 개수에 따라 위치 정보를 보정하였다.
- fasta 파일이 (-) strand 정보일 경우 역상보 서열로 변환해주었다.
- BERT token의 maximum Length가 512라는 점과 DNA sequencing시의 한 리드 길이를 반영하여, WT 201nt, mut 201nt로 잘라주었다.

```bash
python MP3.parsing_vcf_fasta_DNA.py 0.Genes.fasta M2.main_transcript.vcf M3.COSMIC_final.tsv
```
    
