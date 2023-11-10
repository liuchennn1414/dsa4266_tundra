# Exploration

This folder contains the methods we have tried, but was not used in the final model. 

The main difference in this folder is that the datasets are processed differently from the xgboost, lstm and ensemble model used in the final model.

## Data preprocessing
The data preprocessing takes around 1 hour.

For all of the methods here, readings are not aggregated to mean, median and standard deviation, this is to keep all valuable information in the readings. This preprocessing method will create very long datasets, and **greatly increase** the preprocessing and training time.

## svm_rows
We tried a Support Vector Machine. The dataset is created using `merge_data & EDA.ipynb`. The ROC and PR AUC are much higher than the logistic_regression_rows model, but still lower than the final model and also takes a insanely long time to train.

## logistic_regression_rows
We tried a logistic regression as a baseline model. The dataset used is same as `svm_rows`. The ROC and PR AUC are much lower than the svm_rows and the final model.

## xgboost_rows
After learning about the outstanding performance of XGBoost, we tried XGBoost with the same dataset used in `svm_rows`. The training time is much shorter than svm_rows, but still takes much longer than the xgboost model using aggregated data. The ROC and PR AUC are also lower than the aggregated data version. 

## xgboost_row_new_data_processing
We still think that a dataset without aggregation could generate a better model, as it does not lose any information. Hence, we reviewed what might be the problems in our dataset and processed a new dataset without aggregation.
The dataset is processed with the following additional steps:
1. Split the sequence into 5-mers and 1-mers, which creates 10 extra columns.
2. Since we were unsure if the standard deviation created during aggregation has played an important role in the model, we created the standard deviation columns for each of the columns.
3. We balanced and reduced the data by sampling 20 rows from each transcript_id and transcript_position group.
4. Merged result_df with the label data. The final merged_data df have 2,436,760 rows and 31 columns. 

The first result was quite close to the xgboost method with aggregated data, but it will take too long to find the best parameters for the model. Hence, we decided to use the aggregated data version for the final model.

## other_models
We also kept a version of simple neural network (nn) and random forest in this folder. 

The nn.ipynb is initially used while exploring row version. We chose LSTM later for the column version which outperform the row vserion. 

The random forest is for column vserion, and it is an extra exploration to test if it outperform XGBoost and LSTM. Since the ROC & PR result is not outstanding, this model is not selected. 