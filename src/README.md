# Ensembling Model for m6A site prediction

## Introduction
This repository contains the code for the paper "Ensembling Model for m6A site prediction". The code is written in Python 3.10.13.

## Setup
First, clone the repo and install required packages:
```
git clone https://github.com/liuchennn1414/dsa4266_tundra.git
cd dsa4266_tundra
pip install -r requirements.txt
cd src
```

## Evaluation using default datasets
We already prepared a pair of [1000 lines dataset.json](data/dataset1000.json) and [1000 lines data.info](data1000.info) in the `data` folder for faster evaluation. Running the following command will do perform inference and evaluation using our datasets.
```
python run_evaluation.py
```
**Note: Please make sure you are in the /src/ directory**
## Evaluation using your own datasets
If you wish to evaluate our model with your own data.
```
python run_evaluation.py --dataset your/path/to/dataset.json --info your/path/to/data.info
```
**Note: Your data.info should contain the true labels.**

## Inference
To do inference with your own data:
```
python run_inference.py --dataset your/path/to/dataset.json
```
**Note: You do not need a data.info for inference**

## Training and tuning
**Note: The entire training and tuning process could take a few hours**

TODO?