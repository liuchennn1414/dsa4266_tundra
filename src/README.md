# Ensembling Model for m6A site prediction

## Introduction
This repository contains the code for the paper "Ensembling Model for m6A site prediction". The code is written in Python 3.10.13.

## Setup
First, clone the repo and install required packages:

```bash
git clone https://github.com/liuchennn1414/dsa4266_tundra.git
cd dsa4266_tundra
pip install -r requirements.txt
```

## Evaluation
We prepared a evaluation dataset in the `data` folder. To run the code, simply run:

```bash
python run_evaluation.py
```
The output will be saved in the `output` folder.

If you wish to do evaluation with your own data:

```bash
python run_evaluation.py --dataset your/path/to/dataset.json --info your/path/to/data.info
```
**Note: Your data.info should contain the true labels of your data.**

## Inference
To do inference with your own data:

```bash
python run_inference.py --dataset your/path/to/dataset.json
```
**Note: For inference, your do not need a data.info**

## Training your own model
TODO