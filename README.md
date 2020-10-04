

<h3 align="center">
<p> A Drug-Target Interaction Prediction Toolkit with state-of-the-art Deep Learning Methods</h3>
<h4 align="center">
<p> and its Applications in Drug Virtual Screening and Biological activity predition </h4>

---

This repository hosts Ebola_research, a Deep Learning Based Drug-Target Interaction Prediction Toolkit with Applications in Drug Repurposing and Virtual Screening Toolkit (using PyTorch) for Ebola drug research and any disease target reserach.  



### Features



- Realistic and user-friendly design: 
	- automatic identification to do drug target binding affinity (regression) or drug target interaction prediction (binary) task.
	- support cold target, cold drug settings for robust model evaluations and support single-target high throughput sequencing assay data setup.
	- easy monitoring of training process with detailed training metrics output such as test set figures (AUCs) and tables, also support early stopping.
	- detailed output records such as rank list for repurposing result.
	- various evaluation metrics: ROC-AUC, PR-AUC, F1 for binary task, MSE, R-squared, Concordance Index for regression task.
	- label unit conversion for skewed label distribution such as Kd.
	- time reference for computational expensive encoding.
	- PyTorch based, support CPU, GPU, Multi-GPUs.
	


## Install & Usage
Try it on [Binder](https://mybinder.org)! Binder is a cloud Jupyter Notebook interface that will install the environment dependency for you. 

It is advisable to install it locally since Binder needs to be refreshed every time launching:

<details>
  <summary>Click here for the installation instruction!</summary>

First time:
```bash
git clone https://github.com/LouisDarko/Ebola_research.git
## Download code repository

cd Ebola_research
## Change directory to Ebola_research

conda env create -f environment.yml  
## Build virtual environment with all packages installed using conda

conda activate DeepPurpose
## Activate conda environment (use "source activate DeepPurpose" for anaconda 4.4 or earlier) 

jupyter notebook
## open the jupyter notebook with the conda env

## run our code, e.g. click a file in the DEMO folder
... ...

conda deactivate 
## when done, exit conda environment 
```

In the future:
```bash
cd Ebola_research
## Change directory to Ebola_research

conda activate DeepPurpose
## Activate conda environment

jupyter notebook
## open the jupyter notebook with the conda env


... ...

conda deactivate 
## when done, exit conda environment 
```
</details>





## Contact
Please contact louisdarko20@gmail.com or lksdarko@st.ug.edu.gh. for clarification

## Encodings
Currently, we support the following encodings:

| Drug Encodings  | Description |
|-----------------|-------------|

| CNN | Convolutional Neural Network on SMILES|


| Target Encodings  | Description |
|-----------------|-------------|
|
| CNN | Convolutional Neural Network on target seq|


## Data

It supports .txt and .csv files. It assumes the following data format.

<details>
  <summary>Click here for the format expected!</summary>

For drug target pairs:
```
Drug1_SMILES Target1_Seq Score/Label
Drug2_SMILES Target2_Seq Score/Label
....
```
Then, use 

```python 
from DeepPurpose import dataset
X_drug, X_target, y = dataset.read_file_training_dataset_drug_target_pairs(PATH)
```

For bioassay training data:
```
Target_Seq
Drug1_SMILES Score/Label
Drug2_SMILES Score/Label
....
```

Then, use 

```python 
from DeepPurpose import dataset
X_drug, X_target, y = dataset.read_file_training_dataset_bioassay(PATH)
```

For drug repurposing library:
```
Drug1_Name Drug1_SMILES 
Drug2_Name Drug2_SMILES
....
```
Then, use 

```python 
from DeepPurpose import dataset
X_drug, X_drug_names = dataset.read_file_repurposing_library(PATH)
```

For target sequence to be repurposed:
```
Target_Name Target_seq 
```
Then, use 

```python 
from DeepPurpose import dataset
Target_seq, Target_name = dataset.read_file_target_sequence(PATH)
```

For virtual screening library:
```
Drug1_SMILES Drug1_Name Target1_Seq Target1_Name
Drug1_SMILES Drug1_Name Target1_Seq Target1_Name
....
```
Then, use 

```python 
from DeepPurpose import dataset
X_drug, X_target, X_drug_names, X_target_names = dataset.read_file_virtual_screening_drug_target_pairs(PATH)
```
</details>



## trained model


The python script used to build the CNN model for this study can be found inside the model folder

<details>
 


## Disclaimer
The model is built on a framework developed by Kexin Huang: kexinhuang@hsph.harvard.edu 

</details>


## MM-PBSA analysis for residue energy contributions
The R script implemented to elucidate the energy contribution of the critical residues of the protein-ligand complex during binding can be found in the R-script folder

