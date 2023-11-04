import json
import pandas as pd
import numpy as np

dataset_path = 'dataset1000.json'
info_path = 'data.info'
# #split dataset into 1000 lines per file
# with open('dataset0.json', 'r') as f:
#     data_list = []
#     for i, line in enumerate(f):
#         data_list.append(json.loads(line))
#         if (i+1) % 1000 == 0:
#             with open('dataset'+str(i+1)+'.json', 'w') as f:
#                 for data in data_list:
#                     json.dump(data, f)
#                     f.write('\n')
#             data_list = []
#         if i == 10000:
#             break
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
info_df = pd.read_csv(info_path)

info_df_filtered = info_df.merge(result_df, 
                                on=['transcript_id', 'transcript_position'], 
                                how='inner')

info_df_filtered = info_df_filtered[['gene_id', 'transcript_id', 'transcript_position', 'label']]
info_df_filtered.to_csv('data1000.info', index=False)