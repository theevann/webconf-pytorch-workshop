This is a tutorial presented during a workshop at the TheWebConf 2021.

It consists of 6 interactive Jupyter notebooks.

# Notebooks

The links below open the notebooks in Google Colab. This way, you don't have to install anything on your computer and you get a GPU for free. 

1. [Basics](https://colab.research.google.com/github/theevann/webconf-pytorch-workshop/blob/master/1-Basics.ipynb)
1. [Autograd](https://colab.research.google.com/github/theevann/webconf-pytorch-workshop/blob/master/2-Autograd.ipynb)
1. [Optimization](https://colab.research.google.com/github/theevann/webconf-pytorch-workshop/blob/master/3-Optimization.ipynb)
1. [Modules](https://colab.research.google.com/github/theevann/webconf-pytorch-workshop/blob/master/4-Modules.ipynb)
1. [CNN](https://colab.research.google.com/github/theevann/webconf-pytorch-workshop/blob/master/5-CNN.ipynb)
1. [Transfer Learning](https://colab.research.google.com/github/theevann/webconf-pytorch-workshop/blob/master/6-Transfer-Learning.ipynb)

### Log in using your Google account
![Google Colab Login](figures/colab-connect.png)

### Enable GPU support by changing the ‘runtime type’

![Google Colab Runtime](figures/colab-runtime.png)

### Introduction to Google Colab

[This notebook](https://colab.research.google.com/notebooks/basic_features_overview.ipynb) covers the basic features of Google Colab.

---


# Further learning

Check out these others tutorials and courses if you are hungry to learn more:

- Official tutorials: [pytorch.org/tutorials](https://pytorch.org/tutorials/). There are many!
- Step-by-step tutorial: [towardsdatascience.com](https://towardsdatascience.com/understanding-pytorch-with-an-example-a-step-by-step-tutorial-81fc5f8c4e8e)
- PyTorch for deep learning (.py files): [yunjey/pytorch-tutorial](https://github.com/yunjey/pytorch-tutorial)
- PyTorch for deep learning (notebooks): [yandexdataschool/Practical_DL](https://github.com/yandexdataschool/Practical_DL)



---

# Alternative setups

## Binder

Binder is an alterantive way to run remote notebooks that does not require a Google account.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/theevann/amld-pytorch-workshop/master) 
<br />


## Running locally using Conda
If you want to run the notebooks locally, you can use `conda`. The following instructions
should work on Linux/Mac OS, Windows might require slight adaptations.

### Step 1: Install conda
If you have not installed it yet, you can download it from [Anaconda (Python 3.6 version)](https://www.anaconda.com/download/#linux).

Verify that it is installed by running
```bash
conda -V
```

Make sure your conda installation is up-to-date:
```bash
conda update conda
```

#### Step 2: Download repository and install environment
Now clone the repository:
```bash
git clone https://github.com/theevann/amld-pytorch-workshop.git
cd amld-pytorch-workshop
```

The available `conda` environments can be listed using
```bash
conda env list
```

Let's now create a new environment called _'amld-pytorch'_.
```bash
conda env create -f environments.yml
```


#### Step 3: Activate/Deactivate the environment
After the environment has been created, you can **activate** it by
```bash
source activate amld-pytorch
```

Now start the Jupyter notebook by running
```bash
jupyter notebook
```

The environment can similarly **deactivated** by
```bash
source deactivate
```
