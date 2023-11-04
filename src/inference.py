import joblib
import argparse
from sklearn.metrics import classification_report, roc_curve, auc
from sklearn.metrics import average_precision_score, precision_recall_curve

def run_inference(x_test, xgb_model, lstm_model, weights):
    # load model
    xgboost = joblib.load(xgb_model)
    lstm = joblib.load(lstm_model)

    # Load weights
    weights = joblib.load(weights)
    weight_xgb = weights['weight_xgb']
    weight_lstm = weights['weight_lstm']

    # Generate predictions
    pred_xgb = xgboost.predict_proba(X_test)[:, 1]
    pred_lstm = lstm.predict(X_test).ravel()

    # Compute the ensemble prediction
    ensembled_probability = weight_xgb * pred_xgb + weight_lstm * pred_lstm

    return ensembled_probability

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='data/dataset1000.json')
    parser.add_argument('--xgb_model', type=str, default='best_xgboost.pkl')
    parser.add_argument('--lstm_model', type=str, default='best_lstm.pkl')
    parser.add_argument('--weights', type=str, default='ensemble_weights.pkl')
    args = parser.parse_args()

    processed_df = process_data(dataset_path)
    X_test = data_df.drop(['transcript_id', 'transcript_position'], axis=1)

    ensembled_probability = run_inference(args.dataset, 
                                        args.xgb_model,
                                        args.lstm_model,
                                        args.weights)
    
    output_df = pd.DataFrame({'transcript_id': data_df['transcript_id'],
                            'transcript_position': data_df['transcript_position'],
                            'probability': ensembled_probability})

    output_df.to_csv('output.csv', index=False)