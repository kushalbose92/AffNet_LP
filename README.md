# AffNet

This code base contains the AffNet-based implementation of Unsupervised Homophily Estimation, Link Prediction and Recommendation

---

## 📂 Project Structure
```
AffNet/
│── AffNet                  # Unsupervised Homophily Estimation, Link Prediction 
│── AffNetR                 # Recommendation
│── requirements.txt         # Dependencies
│── README.md                # Project info
```

---

## ⚙️ Installation

1. **Clone repository**
```bash
git clone <this URL>
cd AffNet
```

2. **Install dependencies**

> ⚠️ Important: PyTorch Geometric has special installation instructions.  
> First install PyTorch matching your CUDA version:  
> https://pytorch.org/get-started/locally/

Example (CUDA 11.8):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Then install PyG:
```bash
pip install torch-geometric torch-scatter torch-sparse
```

Finally:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

For AffNet, the main program is *predict_link.py*. For AffNetR, the program is main.py.
Other programs are there to reproduce graphs or other presentations in the paper.
Most programs can be called without arguments like the following. 

```bash
python predict_link_approaches.py
python plot_approaches.py
```


The following programs in AffNet need arguments and they are similar.

- *predict_link.py*

- *predict_link_heads.py*

- *predict_link_approaches.py*

- *beta_analysis.py*

- *predict_link_noisy.py* 


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

Results are saved in:
- `results` → numerical metrics, plots  

---

## 📊 Features
- Multiple datasets: Non-OGB homophilic and heterophilic, OGB, MovieLens-1M (for Recommendation)
- Measures Affinity-based Homophily without using node labels
- Predicts missing links in graph dataset
- Recommends in bipartite graphs (e.g. user-item recommendation)
- Saves results in CSV for later analysis

