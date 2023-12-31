# Ensembling Model for m6A site prediction
[![GitHub Stars](https://img.shields.io/github/stars/liuchennn1414/dsa4266_tundra?style=social)](https://github.com/liuchennn1414/dsa4266_tundra)
[![license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/liuchennn1414/dsa4266_tundra/blob/main/LICENSE)
## Introduction
This repository contains the code for the paper "Ensembling Model for m6A site prediction". The code is written in Python3.10 and tested on Ubuntu 20.04. 

## Model performance
The model we are using is a **weighted ensembling model of XGBoost and LSTM**, weighted based on MAE. We summarize the evaluation results as follows. We also provide the fine-tuned weights. **The detailed documentation of this repository's structure, our project flow and the models can be found at [`docs/README.md`](docs/README.md)**.

| name | model checkpoint | ROC AUC | PR AUC  | Average Score |
|------------|:----------------------------------------|:----------:|:-------:|:-----:|
| xgboost | [best_xgboost](model_checkpoints/best_xgboost.json) | 0.73141 | 0.39297 | 0.56219 |
| LSTM | [best_lstm](model_checkpoints/best_lstm.h5) | 0.87304 | 0.22735 | 0.55019 |
| ensemble | [ensemble_weights](model_checkpoints/ensemble_weights.pkl) | 0.88495 | 0.42470 | 0.65482 |

## Setup Environment

### 0. Instance Requirements
- Ubuntu 20 04 Large
- t3.medium (or above)

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
3. Remove the Miniconda installer (OPTIONAL)
    ```
    rm ~/miniconda.sh
    ```
4. Activate conda (If you accidentally close the terminal, you will need to run this command again)
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
cd dsa4266_tundra
conda env create -f environment.yml
conda activate dsa4266_tundra
```
<details>
<summary><U>Alternative: Manual Python Installation (without Conda)</U></summary>

You can also install Python manually by running the following commands, but you may run into version conflicts. 

1. Install python:
    ```
    git clone https://github.com/liuchennn1414/dsa4266_tundra.git
    cd dsa4266_tundra
    sudo apt update
    sudo apt-get install -y python3.10 python3-pip
    ```
2. Check if Python is already installed:
    ```
    python3 --version
    pip --version
    ```
3. Then install the required packages:
    ```
    pip install -r requirements.txt
    ```
</details>

## Prediction
### Prediction using our default datasets
We have prepared a pair of [1000 lines dataset.json](data/dataset1000.json) and [1000 lines data.info](data1000.info) in the `data` folder for faster prediction. Running the following command will perform prediction using our default datasets.
```
python3 prediction.py
```
To view the prediction results:
```
head prediction_output/ensembled_result.csv
```
### Prediction with your own data (OPTIONAL)
```
python3 prediction.py --dataset your/path/to/dataset.json --output_path prediction_output/your_output_name.json
```

<I>Note: You do not need the data.info for prediction</I>

## Evaluation (OPTIONAL)

### Evaluation using our default datasets (OPTIONAL)
The evaluated results will be different from the table in [model performance](#model-performance) because we are using different datasets. 
```
python3 evaluation.py
```

### Evaluation using your own datasets (OPTIONAL)

If you wish to evaluate our model with your own data.
```
python3 evaluation.py --dataset your/path/to/dataset.json --info your/path/to/data.info
```
<I>Note: Your data.info should contain the true labels.</I>