# dsa4266_tundra

## Overview 
--- 
This repoistory records all scripts & documentations for NUS AY23/24 Sem 1 DSA4266 project done by team tundra. Our team members are: Joey Li Jin Tao, Chen Yichi, Liu Chen and You Bohan. 

The primary objective of this project to develop a machine learning method to detect m6A RNA modifications in RNA molecules from direct RNA-Seq data; Following by that, we aim to predict m6A RNA modifications in 12 samples of direct RNA from the SG-NEx data using the model trained, and conduct data analysis over the prediction result. 

The overall structure of the repository is as such: 
* [data](../data): Contains the sample dataset used for student evaluation. 
* [data_preprocessing](../data_preprocessing): Contains code for data parsing & EDA process. 
    * [merge_data.ipynb](../data_preprocessing/merge_data.ipynb): Code for data parsing (column version)
    * [variable_selection.ipynb](../data_preprocessing/variable_selection.ipynb): Code for feature selection (RFE & Lasso) 
    * [encoding_train_test_rfe.ipynb](../data_preprocessing/encoding_train_test_rfe.ipynb): Code for Feature Engineering, train test split and undersampling. 
    * [EDA.ipynb](../data_preprocessing/EDA.ipynb): Code for EDA
* [xgboost](../xgboost): Code for model XGBoost (column version)
    * [xgboost_rfe.ipynb](../xgboost/xgboost_rfe.ipynb): Exploration code for XGBoost, contains baseline XGBoost, and bayesian tuning process. 
    * [xgboost_rfe_full.ipynb](../xgboost/xgboost_rfe_full.ipynb): Clean up version of XGBoost, using only the final chosen XGBoost model. 
    * [xgboost_workflow.ipynb](../xgboost/xgboost_workflow.ipynb): Essential steps needed to generate prediction result using the final XGBoost model. 
* [lstm](../lstm): Code for model LSTM (column version)
    * [LSTM_columns_final_tuned.ipynb](../lstm/LSTM_columns_final_tuned.ipynb): Full set code for LSTM 
* [ensemble](../ensemble): Code for ensemble model, this contains our final model. 
    * [ensemble_method.ipynb](../ensemble/ensemble_method.ipynb): Exploration code for ensemble method, including 4 different ensemble methods. 
    * [ensemble_workflow.ipynb](../ensemble/ensemble_workflow.ipynb): Cleaned up version using the final selected ensemble model. 
* [model_checkpoints](../model_checkpoints): Checkpoint for our final model. 
* [predictions](../predictions): Task 2 prediction output for SG-NEX samples and analysis over the prediction results. 
    * file name with merge_data: files that is used for extra data processing
    * file name with analysis: analysis process done by different team members 
    * csv files: prediciton output 
* [docs](../docs): Project timeline and project README.md 
* [exploration](../exploration): Archived code for other models and data processing method we have explored. These are not used in the final model. You can find more information about them [here](../exploration/README.md). 
* Documents not in folder are scripts for student evaluation purpose.

## Project Flow 
---

The flow of our project is as follow: 

### 1. Data Parsing & EDA
The given dataset has been parsed and form 2 version:
- Version 1: row version, each reading is one row, one transcript_id can have multiple row. 
- Version 2: column version, the reading for each transcript has been aggregated and the mean, std and median has been calculated for each of the 9 columns. This is the method we selected base on model performance and time complexity. [merge_data.ipynb](../data_preprocessing/merge_data.ipynb)
- EDA to study the distribution and correlation among attributes, give inspiration for data preprocessing later. [EDA.ipynb](../data_preprocessing/EDA.ipynb)


### 2. Data preprocessing
The following steps have been done for data preprocessing: 
#### Featuer Engineering 
For each version, we processed the sequence data by seperating it to seq_left (first 5), seq_center (middle 5) and seq_right(last 5). For each column, label encoding has been conducted to convert the column to numeric. 
#### Feature Selection 
We have tried out LASSO & RFE. Column selected by RFE is used for its better performance in terms of ROC & PR AUC score. 
#### Train Test Split 
We split our train and test set by gene_id, i.e. transcripts under same gene_id will all be present in either test or train set, but not both. This is to avoid any leakage of information about the genes. 
#### Oversampling with SMOTE
Due to the imbalance nature of our data, SMOTE has been conducted for the train set to balance the 0 and 1 labels. The test set remains imbalamce. 
#### Minmax standardisation 
To avoid any latent weight due to different range for each column, we performed minmax standardisation to train set, and then for test set, seperately. 

See more details here: [variable_selection.ipynb](../data_preprocessing/variable_selection.ipynb); [encoding_train_test_rfe.ipynb](../data_preprocessing/mencoding_train_test_rfe.ipynb)

### 3. Models and Evaluation 

#### Stage 1: Model exploration 

We have first explored 6 different models: 

Logistic regression, SVM, random forest, NN, XGBoost and LSTM 

**By looking at the models' f1 score, PR AUC and ROC AUC, we shortlisted our models to 2: XGBoost and LSTM.** 

Some model have been examined for both row version and column version to compare which version is better. You can find more details for those non-final models in [exploration](../exploration). 

#### Stage 2: Hyperparameter tuning 

For XGBoost and LSTM, we perform **hyperparameter tuning** (GridSearch & RandomSearch) and innovative tuning such as **Bayesian optimisation with Hyperopt** to obtain the best hyperperameters. They are the models we used to submit for intermediate result. 

#### Stage 3: Ensemble Model 

Noticing from intermediate submission that the result for LSTM is slighly better than XGBoost but unstable when facing synthetic RNAs, we decide to combine the effect of both model using ensemble methods. We have explored **4 different ensemble methods**: 
* **Baseline Ensemble**: average result of the 2 models. 
* **Ensemble 1**: Stack with Logistic regression. This treats the result of both models as parameters of a simple logistic regression function. 
* **Ensemble 2**: VotingClassifier. This will require wrapping of the sequential LSTM into a classifier, and results in a failure when we try to export & load the model. 
* **Ensemble 3**: Weighted Ensemble model using MAE. This will assign the highest weight to the model that has a lower MAE. 


We then compare both the ROC AUC and PR AUC result, and have chosen the weighted ensemble model of XGBoost & lSTM using MAE as our final model. 

### 4. Prediction and Analysis 
We used the weighted ensemble model of XGBoost & lSTM using MAE to generate predictions for the 12 samples from SG-NEX data. We then performed 3 different analysis over it: 
1. Feature difference between modified & unmodified transcript across cell lines. [Click here for more details.](../predictions/liuchen_analysis.ipynb)
2. Compare m6A enrichment score across cell lines 
3. Investigate individual sites / genes 

You can view our prediction analysis result in the video / through our report. 

### Conclusion
The capability of correctly prediction m6A modification is of great importance for both scientific and medical breakthroughs. We have reflect on some space of improvement to further improve our model: 

1. We have chosen to keep sequence outside of feature selection process as we believe the sequence will bring some important pattern information. However, it is worthy to try exploring including it into our feature selection process. 

2. Label encoding of sequence has introduced extra ordering into the data. We may consider to perform one hot encoding, follow by feature selection to reduce dimensionality. 

3. One thing we noticed is that the PR AUC is not improved much (<0.5) even with the help of ensemble model. It it worthy to explore more techniques on tuning models base on PR AUC / a mix of PR AUC & ROC AUC (we did try it for XGBoost, but with limited effect). One thing also worh noting is that for imbalance data, ROC AUC might be overconfident in representing the data. 
