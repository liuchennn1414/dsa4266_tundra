import pandas as pd
import argparse
from sklearn.metrics import classification_report, roc_curve, auc
from sklearn.metrics import average_precision_score, precision_recall_curve

from data_processing import process_data, normalize_data
from inference import run_inference

def merge_data(data_df, info_df):
    info_df['transcript_position'] = info_df['transcript_position'].astype(int)
    data_df['transcript_position'] = data_df['transcript_position'].astype(int)
    info_df = info_df[['transcript_id', 'transcript_position', 'label']]
    data_df = pd.merge(data_df, info_df, on=['transcript_id', 'transcript_position'], how='inner')
    return data_df

def run_evaluation(dataset_path, info_path, xgb_model, lstm_model, weights):
    # load data
    processed_df = process_data(dataset_path)
    info_df = pd.read_csv(info_path)

    # merge data
    data_df = merge_data(processed_df, info_df)

    # create test data
    X_test = data_df.drop(['transcript_id', 'label'], axis=1)
    y_test = data_df['label']

    # normalize data
    normalize_X_test = normalize_data(X_test)

    # predict
    ensembled_probability = run_inference(normalize_X_test, 
                                          xgb_model, 
                                          lstm_model, 
                                          weights)

    # print evaluation report
    y_pred = (ensembled_probability > 0.5).astype(int)
    print(classification_report(y_test, y_pred))

    # Calculate PR AUC
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    roc_auc = auc(fpr, tpr)
    print('ROC AUC: {0:0.2f}'.format(roc_auc))
    pr_auc = average_precision_score(y_test, y_pred)
    print('PR AUC: {0:0.2f}'.format(pr_auc))
    print('Average score: {0:0.2f}'.format((roc_auc + pr_auc)/2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='data/dataset1000.json')
    parser.add_argument('--info', type=str, default='data/data1000.info')
    parser.add_argument('--xgb_model', type=str, default='../ensemble/best_xgboost.json')
    parser.add_argument('--lstm_model', type=str, default='../ensemble/best_lstm_tuned.h5')
    parser.add_argument('--weights', type=str, default='../ensemble/ensemble_weights.pkl')
    args = parser.parse_args()

    run_evaluation(args.dataset, 
                    args.info, 
                    args.xgb_model,
                    args.lstm_model,
                    args.weights)