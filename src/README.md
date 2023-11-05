# Ensembling Model for m6A site prediction
[![GitHub Stars](https://img.shields.io/github/stars/liuchennn1414/dsa4266_tundra?style=social)](https://github.com/liuchennn1414/dsa4266_tundra)
[![license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/liuchennn1414/dsa4266_tundra/blob/main/LICENSE)
## Introduction
This repository contains the code for the paper "Ensembling Model for m6A site prediction". The code is written in Python3.10 and tested on Ubuntu 22.04. 

## Model performance
We summarize the evaluation results as follows. We also provide the fine-tuned weights. The instructions to reproduce the results can be found below.

| name | model checkpoint | ROC AUC | PR AUC  | Average Score |
|------------|:----------------------------------------|:----------:|:-------:|:-----:|
| xgboost | [best_xgboost](../ensemble/best_xgboost.json) | 0 | 0 | 0 |
| LSTM | [best_lstm](../ensemble/best_lstm_tuned.h5) | 0 | 0 | 0 |
| ensemble | [ensemble_weights](../ensemble/ensemble_weights.pkl) | 0 | 0 | 0 |

## Download Conda (skip if you already done so)
1. download the installer
```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
```
2. install conda quietly
```
bash ~/miniconda.sh -b
```
3. Remove the Miniconda installer
```
rm ~/miniconda.sh
```
4. Activate conda
```
source $HOME/miniconda3/bin/activate
```
5. Add conda to your PATH (OPTIONAL)
```
printf '\n# add path to conda\nexport PATH="$HOME/miniconda3/bin:$PATH"\n' >> ~/.bashrc
```
## Setup Environment

### Using conda

You can set up the environment using conda by running the following commands:

```bash
git clone https://github.com/liuchennn1414/dsa4266_tundra.git
cd dsa4266_tundra/src
conda env create -f environment.yml
conda activate dsa4266_tundra
Note: This will take about 5 to 10 minutes
```
<details>
<summary><B>Alternative: Manual Python Installation</B></summary>

You can also install Python manually by running the following commands, but you may run into version conflicts. 
```
git clone https://github.com/liuchennn1414/dsa4266_tundra.git
cd dsa4266_tundra/src
sudo apt update
sudo apt-get install -y python3.10 python3-pip
```
Check if Python is already installed:
```
python --version
pip --version
```
Then install the required packages:
```
pip install -r requirements.txt
```
</details>

## Evaluation
### Evaluation using default datasets
We already prepared a pair of [1000 lines dataset.json](data/dataset1000.json) and [1000 lines data.info](data1000.info) in the `data` folder for faster evaluation. Running the following command will perform inference and evaluation using our datasets.
```
python3 run_evaluation.py
```
<I>**Note: Please make sure you are in the /src/ directory**</I>

<details>
<summary><B>Evaluation using your own datasets</B></summary>

If you wish to evaluate our model with your own data.
```
python3 run_evaluation.py --dataset your/path/to/dataset.json --info your/path/to/data.info
```
**Note: Your data.info should contain the true labels.**
</details>

## Inference
To do inference with your own data:
```
python3 run_inference.py --dataset your/path/to/dataset.json
```
<I>**Note: You do not need a data.info for inference**</I>