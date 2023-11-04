# Ensembling Model for m6A site prediction

## Introduction
This repository contains the code for the paper "Ensembling Model for m6A site prediction". The code is written in Python 3.10.13.

## Download Conda(skip if you already done so)
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
## Setup environment
Using conda, you can easily setup the environment by running the following commands:
```
git clone https://github.com/liuchennn1414/dsa4266_tundra.git
cd dsa4266_tundra/src
conda env create -f environment.yml
conda activate dsa4266_tundra
```
ALTERNATIVELY, if conda is not working, you can install python manually (not recommended):
```
git clone https://github.com/liuchennn1414/dsa4266_tundra.git
cd dsa4266_tundra/src
sudo apt update
sudo apt-get install python3.10.12
pip install -r requirements.txt
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