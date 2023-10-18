# dsa4266_tundra

## Project Flow 
---
1. **Data Parsing & EDA**

The given dataset has been parsed and form 2 version:
- Version 1: row version, each reading is one row, one transcript_id can have multiple row. The dimension of this dataset is ~10M x 14 
- Version 2: column version, the reading for each transcript has been aggregated and the mean, std and median has been calculated for each of the 9 columns. Feature selection has been performed to reduce dimensionality. 

2. **Data preprocessing**
- Featuer Engineering 
For each version, we processed the sequence data by seperating it to seq_left (first 5), seq_center (middle 5) and seq_right(last 5). For each column, label encoding has been conducted to convert the column to numeric. (Aware that some order has been introduced inside, do we want to address this?)
- Train Test Split 
We split our train and test set by gene_id, i.e. transcripts under same gene_id will all be present in either test or train set, but not both. This is to avoid any leakage of information about the genes. 
- Oversampling with smote
Due to the imbalance nature of our data, SMOTE has been conducted for the train set to balance the 0 and 1 labels. The test set remains imbalamce. 
- Minmax standardisation 
To avoid any latent weight due to different range for each column, we performed minmax standardisation to train set, and then for test set, seperately. 

3. **Models** 

For each version, two models has been studied: 
- XGBoost 
- NN (LTSM for version2)
We have also studied other models such as logistic regression and SVM. Comparing the score, we narrowed down to XGBoost and NN only. 
For each model, hyperparameter tuning has also been conducted with innovative tuning method such as Bayesian Optimisation with Hyperopt. We then study the classification_report anf plot out the ROC curve to evaluate the quality of our model. 

