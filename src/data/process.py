import json

#split dataset into 1000 lines per file
with open('dataset0.json', 'r') as f:
    data_list = []
    for i, line in enumerate(f):
        data_list.append(json.loads(line))
        if (i+1) % 1000 == 0:
            with open('dataset'+str(i+1)+'.json', 'w') as f:
                for data in data_list:
                    json.dump(data, f)
                    f.write('\n')
            data_list = []
        if i == 10000:
            break