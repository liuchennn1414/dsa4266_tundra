import joblib
import argparse
import pandas as pd
import xgboost as xgb
from tensorflow.keras.models import load_model

from data_processing import process_data, normalize_data

def run_prediction(X_test, xgb_model, lstm_model, weights):
    # load model
    xgboost = xgb.Booster()
    xgboost.load_model(xgb_model)
    lstm = load_model(lstm_model)

    # Load weights
    weights = joblib.load(weights)
    weight_xgb = weights['weight_xgb']
    weight_lstm = weights['weight_lstm']

    # Generate predictions
    m = xgb.DMatrix(X_test)
    pred_xgb = xgboost.predict(m)
    pred_lstm = lstm.predict(X_test).ravel()

    # Compute the ensemble prediction
    ensembled_probability = weight_xgb * pred_xgb + weight_lstm * pred_lstm

    return ensembled_probability

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='data/dataset1000.json')
    parser.add_argument('--xgb_model', type=str, default='model_checkpoints/best_xgboost.json')
    parser.add_argument('--lstm_model', type=str, default='model_checkpoints/best_lstm.h5')
    parser.add_argument('--weights', type=str, default='model_checkpoints/ensemble_weights.pkl')
    parser.add_argument('--output_path', type=str, default='prediction_output/ensembled_result.csv')
    args = parser.parse_args()

    data_df = process_data(args.dataset)
    X_test = data_df.drop(['transcript_id'], axis=1)
    normalize_X_test = normalize_data(X_test)

    ensembled_probability = run_prediction(normalize_X_test, 
                                        args.xgb_model,
                                        args.lstm_model,
                                        args.weights)
    
    output_df = pd.DataFrame({'transcript_id': data_df['transcript_id'],
                            'transcript_position': data_df['transcript_position'],
                            'score': ensembled_probability})

    output_df.to_csv(args.output_path, index=False)