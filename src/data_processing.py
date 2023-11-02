import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib
z
rfe = ['avg_1-flank_mean',
 'avg_central_std',
 'avg_1+flank_std',
 'med_1-flank_mean',
 'med_central_std',
 'std_central_std',
 'std_central_mean',
 'std_1+flank_mean',
 'seq_right']

seq_label_encoder = 'label_encoder.pkl'
min_max_scaler = 'min_max_scaler.pkl'

def process_dataset(dataset_path):
    # process the json dataset and returns a dataframe
    data_list = []
    with open(dataset_path, 'r') as f:
        for line in f:
            data_list.append(json.loads(line))
    results = []

    # aggregate data with mean, median, std
    for data in data_list:
        trans_id, first = next(iter(data.items()))
        position, second = next(iter(first.items()))
        sequence, data = next(iter(second.items()))

        avg = np.mean(data, axis=0)
        med = np.median(data, axis=0)
        std = np.std(data, axis=0)

        result = [trans_id, position, sequence] + list(avg)+ list(med) + list(std)
        results.append(result)
    result_df = pd.DataFrame(results)

    # rename colnames
    colnames = ['transcript_id', 'transcript_position', 'sequence']
    for i in ['avg', 'med','std']:
        for j in ['1-flank', 'central', '1+flank']:
            for q in ["length", "std", "mean"]:
                colnames.append(i + '_' + j + '_' + q)

    result_df.columns = colnames
    result_df['transcript_position'] = result_df['transcript_position'].astype(int)

    return result_df

def process_data(dataset_path, info_path, output_path):
    info = pd.read_csv(info_path)
    info['transcript_position'] = info['transcript_position'].astype(int)

    data_df = process_dataset(dataset_path)

    # merge data with info
    merged_data = pd.merge(data_df, info, on=['transcript_id', 'transcript_position'], how='inner')
    # merged_data["transcript_id"] = merged_data["transcript_id"].str.replace('ENST', '').astype(int)
    # merged_data["gene_id"] = merged_data["gene_id"].str.replace('ENSG', '').astype(int)
    merged_data['seq_left'] = merged_data['sequence'].str[0:5]
    merged_data['seq_center'] = merged_data['sequence'].str[1:6]
    merged_data['seq_right'] = merged_data['sequence'].str[2:7]

    label_encoder = joblib.load(seq_label_encoder)
    df_le = merged_data.copy()
    seq_data = ['seq_left','seq_center','seq_right']
    for seq in seq_data: 
        encoded_labels = label_encoder.fit_transform(df_le[seq])
        df_le[seq] = encoded_labels
    
    # choose feature selected by RFE
    df_le = df_le[rfe]

    # normalize data
    min_max_scaler = joblib.load(min_max_scaler)
    df_le = pd.DataFrame(min_max_scaler.fit_transform(df_le), columns=df_le.columns)

    # save processed data
    df_le.to_csv(output_path, index=False)
    return df_le


if __name__ == "__main__":
    dataset_path = 'data/dataset0.json'
    info_path = 'data/data.info'
    output_path = 'data/processed_data.csv'
    processed_df = process_data(dataset_path, info_path, output_path)
    print(processed_df.head())
