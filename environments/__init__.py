from typing import Dict, Type, Any, Tuple
from environments.base_environment import BaseEnvironment
from environments.flappy_bird import FlappyBirdEnv
from environments.toy import ToyExampleEnvironment
import gym

env_name_to_EnvClass: Dict[str, Type[BaseEnvironment]] = {
    "Toy Example": ToyExampleEnvironment,
    "Flappy Bird": FlappyBirdEnv,
}
