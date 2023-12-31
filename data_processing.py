import json
import pandas as pd
import numpy as np
import joblib

# results from RFE feature selection [DO NOT CHANGE]
rfe = ['avg_central_mean', 
        'avg_1+flank_std', 
        'med_central_std', 
        'med_central_mean', 
        'med_1+flank_std', 
        'std_1-flank_std', 
        'std_1-flank_mean', 
        'std_central_std', 
        'std_central_mean', 
        'std_1+flank_std', 
        'std_1+flank_mean', 
        'seq_left', 
        'seq_center', 
        'seq_right']

# label encoder and min max scaler [DO NOT CHANGE]
seq_label_encoder = 'model_checkpoints/label_encoder.pkl'
min_max_scaler = 'model_checkpoints/minmax_scaler.pkl'

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

def normalize_data(df):
    # normalize data
    scaler = joblib.load(min_max_scaler)
    df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df

def process_data(dataset_path):
    data_df = process_dataset(dataset_path)
    
    # convert sequence to 5-mer
    data_df['seq_left'] = data_df['sequence'].str[0:5]
    data_df['seq_center'] = data_df['sequence'].str[1:6]
    data_df['seq_right'] = data_df['sequence'].str[2:7]

    label_encoder = joblib.load(seq_label_encoder)
    seq_data = ['seq_left','seq_center','seq_right']
    for seq in seq_data: 
        encoded_labels = label_encoder.fit_transform(data_df[seq])
        data_df[seq] = encoded_labels

    # choose feature selected by RFE
    normalize_df = data_df[rfe]
    data_df = data_df[['transcript_id', 'transcript_position']]

    # merge data
    data_df = pd.concat([data_df, normalize_df], axis=1)

    return data_df

if __name__ == "__main__":
    dataset_path = 'data/dataset1000.json'
    processed_df = process_data(dataset_path)
    normalize_df = normalize_data(processed_df.drop(['transcript_id'], axis=1))
    # processed_df.to_csv(output_path, index=False)
    print(processed_df.head())
    print("*"*50)
    print(normalize_df.head())
