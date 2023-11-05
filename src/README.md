# Ensembling Model for m6A site prediction
[![GitHub Stars](https://img.shields.io/github/stars/liuchennn1414/dsa4266_tundra?style=social)](https://github.com/liuchennn1414/dsa4266_tundra)
[![license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/liuchennn1414/dsa4266_tundra/blob/main/LICENSE)
## Introduction
This repository contains the code for the paper "Ensembling Model for m6A site prediction". The code is written in Python3.10 and tested on Ubuntu 22.04. 

## Model performance
We summarize the evaluation results as follows. We also provide the fine-tuned weights. The detailed documentation of our project flow the models can be found at [`README.md`](../README.md).

| name | model checkpoint | ROC AUC | PR AUC  | Average Score |
|------------|:----------------------------------------|:----------:|:-------:|:-----:|
| xgboost | [best_xgboost](../ensemble/best_xgboost.json) | 0 | 0 | 0 |
| LSTM | [best_lstm](../ensemble/best_lstm_tuned.h5) | 0 | 0 | 0 |
| ensemble | [ensemble_weights](../ensemble/ensemble_weights.pkl) | 0 | 0 | 0 |

## Setup Environment
### 1. Make sure you have installed Conda
```
conda --version
```
<details>
<summary><U>Step-by-step Conda Installation</U></summary>

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
</details>

### 2. Create a new Conda environment (This will take about 5 to 10 minutes)
    ```bash
    git clone https://github.com/liuchennn1414/dsa4266_tundra.git
    cd dsa4266_tundra/src
    conda env create -f environment.yml
    conda activate dsa4266_tundra
    ```
<details>
<summary><U>Alternative: Manual Python Installation (without Conda)</U></summary>

You can also install Python manually by running the following commands, but you may run into version conflicts. 

1. Install python:
    ```
    git clone https://github.com/liuchennn1414/dsa4266_tundra.git
    cd dsa4266_tundra/src
    sudo apt update
    sudo apt-get install -y python3.10 python3-pip
    ```
2. Check if Python is already installed:
    ```
    python --version
    pip --version
    ```
3. Then install the required packages:
    ```
    pip install -r requirements.txt
    ```
</details>

## Evaluation
### Evaluation using our default datasets
We have prepared a pair of [1000 lines dataset.json](data/dataset1000.json) and [1000 lines data.info](data1000.info) in the `data` folder for faster evaluation. Running the following command will perform inference and evaluation using our default datasets.
```
python3 run_evaluation.py
```
<I>Note: Please make sure you are in the /src/ directory</I>

### Evaluation using your own datasets

If you wish to evaluate our model with your own data.
```
python3 run_evaluation.py --dataset your/path/to/dataset.json --info your/path/to/data.info
```
<I>Note: Your data.info should contain the true labels.</I>

## Inference
To do inference with your own data:
```
python3 run_inference.py --dataset your/path/to/dataset.json
```
<I>Note: You do not need a data.info for inference</I>