# Data folder

This folder contains the data created for evaluation.

Both `dataset1000.json` and `data1000.info` contains only 1000 lines. 

This is for faster evaluation.

## How we created the data

Check out the [`process.py`](process.py) script in this folder to see how we created the files.

To run this script, you would need to download the `dataset0.json` and `data.info` files and place them in this `/data/` folder, then simply run:
```
python3 process.py
```