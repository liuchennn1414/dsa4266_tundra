from data_processing import process_data
import joblib
import argparse

model_path = 'model.pkl'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='data/dataset0.json')
    parser.add_argument('--info', type=str, default='data/data.info')
    args = parser.parse_args()

    dataset_path, info_path = args.dataset, args.info

    # download data
    # mkdir data
    # aws s3 sync --no-sign-request s3://sg-nex-data/data/processed_data/m6Anet/ data/
    processed_df = process_data(dataset_path, info_path)

    # load model
    model = joblib.load(model_path)
    y_pred = model.predict(processed_df)

    # save prediction
    processed_df['prediction'] = y_pred
    processed_df.to_csv('prediction.csv', index=False)