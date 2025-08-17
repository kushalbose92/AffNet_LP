## Description

This code base contains the following in two different folders:
	A. AffNet - Unsupervised Homophily Estimation and Link Prediction
	B. AffNetR - Recommendation on Bipartite Graphs


### Installation

pip install -r requirements.txt


### How to Run
**Example**

For AffNet, the main program is *predict_link.py*. For AffNetR, the program is main.py.
Other programs are there to reproduce graphs or other presentations in the paper.
Most programs can be called without arguments like the following. 

```bash
python predict_link_approaches.py
python plot_approaches.py
```

The following programs in AffNet need arguments and they are similar.
*predict_link.py*, *beta_analysis.py*, *predict_link_noisy.py* 

In AfNetR, *main.py* needs arguments.

AffNet:
```bash
python predict_link.py --dataset=Cora --emb_features=358 --n_heads=4 --max_nodes=2708 --init_lr=0.002 --epochs=2000
python beta_analysis.py --dataset=Cora --emb_features=358 --n_heads=4 --max_nodes=2708 --init_lr=0.002 --epochs=2000
python predict_link_noisy.py --dataset=Cora --emb_features=358 --n_heads=4 --max_nodes=2708 --init_lr=0.002 --epochs=2000
etc
```

```bash
AffNetR:
python main.py --dataset=MovieLens1M --emb_features=16  --num_heads=4 --test_frac=0.3 --init_lr=0.1 --lr_decay=0.98 --dropout=0.5 --k=20 --epochs=50
```

### Changes you may need to do:
1. Mandatory: Within script - *root* and *data_folder*
2. Optional: In commandline arguments - Hyper-parameter values 

### License

MIT
	
