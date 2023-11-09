# this script contains how we create dataset1000.json and data1000.info
# to run this script, make sure you have dataset0.json and data.info in the same folder
import json
import pandas as pd

original_dataset_path = 'dataset0.json'
dataset_path = 'dataset1000.json'
info_path = 'data.info'
output_info_path = 'data1000.info'

# create dataset1000.json
#split dataset into 1000 lines per file
def split_into_1000(max_files = 10):
    output_fnames = []
    with open(original_dataset_path, 'r') as f:
        data_list = []
        for i, line in enumerate(f):
            data_list.append(json.loads(line))
            if (i+1) % 1000 == 0:
                output_fname = 'dataset'+str(i+1)+'.json'
                output_fnames.append(output_fname)
                with open(output_fname, 'w') as f:
                    for data in data_list:
                        json.dump(data, f)
                        f.write('\n')
                data_list = []
            if i == max_files * 1000:
                break
    print(f"{max_files} files created")
    return output_fnames

# create a shortened 1000 lines data.info from a dataset.json with 1000 lines
def get_shortened_info(dataset1000_path, output_info_path):
    data_list = []
    with open(dataset1000_path, 'r') as f:
        for line in f:
            data_list.append(json.loads(line))
    results = []
    
    for data in data_list:
        trans_id, first = next(iter(data.items()))
        position, second = next(iter(first.items()))

        result = [trans_id, position]
        results.append(result)

    result_df = pd.DataFrame(results)

    # rename colnames
    colnames = ['transcript_id', 'transcript_position']

    result_df.columns = colnames
    result_df['transcript_position'] = result_df['transcript_position'].astype(int)
    info_df = pd.read_csv(info_path)

    info_df_filtered = info_df.merge(result_df, 
                                    on=['transcript_id', 'transcript_position'], 
                                    how='inner')

    info_df_filtered = info_df_filtered[['gene_id', 'transcript_id', 'transcript_position', 'label']]
    info_df_filtered.to_csv(output_info_path, index=False)

if __name__ == '__main__':
    # create 10 datasets with 1000 lines each
    dataset_files = split_into_1000(max_files=1)
    for file in dataset_files:
        get_shortened_info(file, file[:-5]+'.info')