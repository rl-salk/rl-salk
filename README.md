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

### Creating environment
```
conda create -n gym python=3 pip
```
This creates an environment called "gym", now you can switch and install gym package

### Activating conda environment
```
activate gym
```

## OpenAI Gym
OpenAI Gym contains some RL environments that you can experiment with.

### Installation
```
pip install gym
```

