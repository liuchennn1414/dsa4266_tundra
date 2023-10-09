# dsa4266_tundra

If you are running the code locally, I recommend using conda as a environment control tool
https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html
After installation of conda, in your terminal(skip if not using conda):
```
conda create -n DSA4266_tundra_env python=3.10
conda activate DSA4266_tundra_env
```
Then you can run the following code to clone the repo and install the required packages
```
git clone https://github.com/liuchennn1414/dsa4266_tundra.git
cd dsa4266_tundra
mkdir data
pip install -r requirements.txt
```
download `data.info` and `dataset0.json.gz` from canvas into the `data` folder

run `merge_data_without_sampling.py` to merge the two files

run `train_test.ipynb` to split the train and test dataset

run `svm.ipynb` to train and test the svm model
