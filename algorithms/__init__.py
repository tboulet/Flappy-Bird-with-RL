from typing import Dict, Type, Any, Tuple

from algorithms.base.base_algorithm import BaseRLAlgorithm

from algorithms.random import RandomAlgorithm
from algorithms.sarsa_lambda import SARSA_Lambda
from algorithms.monte_carlo import MonteCarlo


algo_name_to_AlgoClass: Dict[str, Type[BaseRLAlgorithm]] = {
    "Random": RandomAlgorithm,
    "SARSA Lambda": SARSA_Lambda,
    "Monte Carlo": MonteCarlo,
}
