from data_processing import process_data
from inference import run_inference
import joblib
import pandas as pd
import argparse
from sklearn.metrics import classification_report, roc_curve, auc
from sklearn.metrics import average_precision_score, precision_recall_curve

def merge_data(data_df, info_df):
    info_df['transcript_position'] = info_df['transcript_position'].astype(int)
    info_df = info_df[['transcript_id', 'transcript_position', 'label']]
    data_df = pd.merge(data_df, info_df, on=['transcript_id', 'transcript_position'], how='left')
    return data_df

def run_evaluation(dataset_path, info_path, xgb_model, lstm_model, weights):
    # load data
    processed_df = process_data(dataset_path)
    info_df = pd.read_csv(info_path)

    # merge data
    data_df = merge_data(processed_df, info_df)

    # create test data
    X_test = data_df.drop(['transcript_id', 'transcript_position', 'label'], axis=1)
    y_test = data_df['label']

    # predict
    ensembled_probability = run_inference(X_test, 
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='data/dataset1000.json')
    parser.add_argument('--info', type=str, default='data/data.info')
    parser.add_argument('--xgb_model', type=str, default='../ensemble/best_xgboost.pkl')
    parser.add_argument('--lstm_model', type=str, default='../ensemble/best_lstm.pkl')
    parser.add_argument('--weights', type=str, default='../ensemble/ensemble_weights.pkl')
    args = parser.parse_args()

    run_evaluation(args.dataset, 
                    args.info, 
                    args.xgb_model,
                    args.lstm_model,
                    args.weights)