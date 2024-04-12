# RL for Flappy Bird

A framework for RL on Flappy Bird.

This was done in the tabular settings in the context of the course "Reinforcement Learning" at CentraleSupélec.

Code by Timothé Boulet.


# Installation

Clone the repository, create a venv (advised), and install the requirements:

```bash
git clone git@github.com:tboulet/Flappy-Bird-with-RL.git
cd Flappy-Bird-with-RL
python -m venv venv
source venv/bin/activate  # on linux
venv\Scripts\activate  # on windows
pip install -r requirements.txt
```


# Run the code
 
For training your algorithms on a certain env, run the following command:

```bash
python run.py algo=<algo tag> env=<env tag>
```

For example, to train the Monte Carlo algorithm on the Flappy Bird environment:

```bash
python run.py algo=mc env=flappy
```

We use Hydra as our config system. The config folder is `./configs/`. You can modify the config (logging, metrics, number of training episodes) from the `default_config.yaml` file. You can also create your own config file and specify it with the `--config-name` argument :

```bash
python run.py algo=mc env=flappy --config-name=my_config_name
```

Advice : create an alias for the command above this.
# Algorithms
The algo tag should correspond to a configuration in ``configs/algo/`` where you can specify the algo and its hyperparameters. 

Currently, the following algorithms are available:
 - `random` : Random policy, a baseline that selects actions uniformly at random
 - `sarsa_l` : SARSA(lambda), an improvement of SARSA that uses eligibility traces to update the Q-values. It is a trade-off between the bias of one-step returns (Q Learning and SARSA) and the variance of Monte-Carlo returns, but more flexible than N-step returns
 - `mc` : Monte-Carlo, a model-free reinforcement learning algorithm that learns the optimal policy by estimating the Q-values with Monte-Carlo returns

# Environments

The env tag should correspond to a configuration in ``configs/env/`` where you can specify the env and its hyperparameters.

Currently the following envs are implemented :
- `toy` : A simple deterministic bandit problem (for testing purposes)
- `flappy` : The tabular version of the Flappy Bird game, where the state is the vertical and horizontal distance to the next pipe, and the action is to jump or not


# Visualisation and results

### WandB
WandB is a very powerful tool for logging. It is flexible, logs everything online, can be used to compare experiments or group those by dataset or algorithm, etc. You can also be several people to work on the same project and share the results directly on line. It is also very easy to use, and can be used with a few lines of code.

If `do_wandb` is True, the metrics will be logged in the project `wandb_config['project']` with entity `wandb_config['entity']`, and you can visualize the results on the WandB website.

### Tensorboard
Tensorboard is a tool that allows to visualize the training. It is usefull during the development phase, to check that everything is working as expected. It is also very easy to use, and can be used with a few lines of code.

If `do_tb` is True, you can visualize the logs by running the following command in the terminal.
```bash
tensorboard --logdir=tensorboard
```

### CLI

You can also visualize the results in the terminal. If `do_cli` is True, the metrics will be printed in the terminal every `cli_frequency_episode` episodes.

# Other

### Seed

You can specify the seed of the experiment with the `seed` argument. If you don't specify it, the seed will be randomly chosen.

### cProfile and SnakeViz

cProfile is a module that allows to profile the code. It is very useful to find bottlenecks in the code, and to optimize it. SnakeViz is a tool that allows to visualize the results of cProfile and so what you should focus. It is used through the terminal :

```bash
snakeviz logs/profile_stats.prof
```