# rl-salk
Main repo for system design and playing around with different architectures

# Getting Started
We recommend you install Anaconda to have a fixed environment for your OpenAI gym, tensorflow and other libarary for your dev environment.

## Anaconda

### Installation:
You can download binary distribution of anaconda and install it for your preferred OS at:
    https://www.anaconda.com/distribution/

If you don't want Anaconda to activate the "base" environment by default, run this command:
```
conda config --set auto_activate_base false
```

### Creating a conda environment
```
conda create -n gym python=3 pip
```
This creates an environment called "gym", now you can switch and install gym package

### Activating a conda environment
```
conda activate gym
```

## OpenAI Gym
OpenAI Gym contains some RL environments that you can experiment with.

### Installation
```
pip install gym
```
# GridWorld Example Gym Env
First you need to install the rl_salk gym env
```
cd libs
pip install -e .
```
You can now import and create the installed env
```
python
```
```
import gym
import rl_salk
env = gym.make('grid-world-v0')
```

### Creating new gym environments

The docs: http://gym.openai.com/docs/

Blog post: https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa

### Using Git

[Git cheat sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

## Jupyter notebook

Jupyter notebook offers a nice interface for putting code, numerical results, and graphics in the same document. Generally you interact with Jupyter notebooks by running a local server on your computer (`jupyter notebook`) and pointing your browser to the appropriate page. After you have created a notebook locally, if you add it to a Git repository on GitHub, you can view the notebook on GitHub without running a server (e.g. the [Cliff Walk notebook](https://github.com/rl-salk/rl-salk/blob/master/notebooks/cliff_walk_demo.ipynb)).

### Installation

```
conda activate <your-env-name>
pip install jupyter ipython
```

```
cd notebooks/
jupyter notebook
```


### Troubleshooting

If you create a new environment that is different from the default one, you need to install ipythonkernel in the new environments. Here is how I did:

In the terminal (replacing `<your-env-name>` with `gym`, for instance):
```
conda activate <your-env-name>
conda install ipykernel
python -m ipykernel install --user --name <your-env-name> --display-name "Python (<your-env-name>)"
jupyter notebook
```

In the notebook, click:
Kernel -> Change Kernel -> Python (<your-env-name>)
    
This procedure is from: [How to install IPython Kernels for different environments](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)
