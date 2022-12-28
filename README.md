# Deep Reinforcement Learning Models for a Drone Hovering Task
Welcome to the repository of my Bachelor's thesis, which was conducted at the Department of Electrical and Computer Engineering at [TUM](https://www.tum.de/). The topic of this thesis is "Sample Complexity Analysis of Transfer Learning for Deep Reinforcement Learning Models".

In context of this Bachelor's thesis, I implement different deep Reinforcement Learning models on a drone to perform a hovering task in a Transfer Learning setting; first I pre-train the Reinforcement Learning models on the differential equations-based simulation environment of the drone where an amount of knowledge is acquired, then I transfer this knowledge by post-training the models on a [PyBullet](https://github.com/bulletphysics/bullet3)-based 3D simulation environment. By means of commonly used metrics, I evaluate the benefits of Transfer Learning to the learning process of the desired task compared to the case where no knowledge is transferred. Furthermore and most importantly, I analyze the sample complexity of the post-training of the implemented deep Reinforcement Learning algorithms. This allows me to draw conclusions about which models deliver the overall best performance and are most appropriate for the combination of deep Reinforcement Learning with Transfer Learning in this specific use case.

For a more detailed discussion please refer to [my thesis](https://github.com/Malekba98/Deep_Reinforcement_Learning_Bachelor_thesis/blob/main/report_and_presentation/report.pdf) and [final presentation](https://github.com/Malekba98/Deep_Reinforcement_Learning_Bachelor_thesis/blob/main/report_and_presentation/presentation.pdf).

This repository contains implementations of the differential equations-based and the [PyBullet](https://github.com/bulletphysics/bullet3)-based 3D simulation environments used in this thesis, which were forked from a previous version of this [repository](https://github.com/SvenGronauer/phoenix-drone-simulation).

Hovering Task 
--- 
![Hover](./docs_readme/hover.png)

## Overview of Simulation Environments

|                                       | Task         | Controller    | Physics            | Observation Frequency | Domain Randomization |  *Aerodynamic effects*  |
|-------------------------------------: | :----------: | :-----------: | :----------------: | :-------------------: | :------------------: | :-------------------------: |
| `DroneHoverPIDSystemEqEnv-v0`         | Hover        | Attitude Rate PID controller (500Hz)   | System Equations |  100 Hz |  10%        |   None |                 
| `DroneHoverPIDBulletEnv-v0`           | Hover        | Attitude Rate PID controller (500Hz)   | PyBullet     |  100 Hz |        10%     |             Drag |                 




# Installation and Requirements
To clone and install the repository, run the following three lines:
```
$ git clone https://github.com/Malekba98/Deep_Reinforcement_Learning_Bachelor_thesis.git
$ cd Deep_Reinforcement_Learning_Bachelor_thesis/
$ pip install -e .
```

> Note: if your default `python` is 2.7, in the following, replace `pip` with `pip3` and `python` with `python3`


## Supported Systems

We tested the repository under *Ubuntu 20.04* and *Mac OS X 11.2* running Python 3.7
and 3.8. Other system might work as well but have not been tested yet.
Note that PyBullet supports Windows as platform only experimentally!. 

Note: This package has been tested on Mac OS 11 and Ubuntu (18.04 LTS, 
20.04 LTS), and is probably fine for most recent Mac and Linux operating 
systems. 


## Dependencies 

Bullet-Safety-Gym heavily depends on two packages:

+ [Gym](https://github.com/openai/gym)
+ [PyBullet](https://github.com/bulletphysics/bullet3)


## Getting Started


After the successful installation of the repository, the Bullet-Safety-Gym 
environments can be simply instantiated via `gym.make`. See: 

```
>>> import gym
>>> import phoenix_simulation
>>> env = gym.make('DroneHoverPWMBulletEnv-v0')
```

The functional interface follows the API of the OpenAI Gym (Brockman et al., 
2016) that consists of the three following important functions:

```
>>> observation = env.reset()
>>> random_action = env.action_space.sample()  # usually the action is determined by a policy
>>> next_observation, reward, done, info = env.step(random_action)
```

Besides the reward signal, our environments provide additional information 
that is contained in the `info` dictionary:
```
>>> info
{'cost': 1.0}
```

A minimal code for visualizing a uniformly random policy in a GUI, can be seen 
in:

```
import gym
import phoenix_simulation

>>> env = gym.make('DroneHoverPWMBulletEnv-v0')

while True:
    done = False
    env.render()  # make GUI of PyBullet appear
    x = env.reset()
    while not done:
        random_action = env.action_space.sample()
        x, reward, done, info = env.step(random_action)
```
Note that only calling the render function before the reset function triggers 
visuals.
