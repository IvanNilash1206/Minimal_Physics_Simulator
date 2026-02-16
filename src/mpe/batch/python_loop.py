#src/mpe/batch/python_loop.py

import numpy as np
from src.mpe.batch.base import BatchIntegrator

class PythonLoopIntegrator(BatchIntegrator):
    def __init__(self, k_over_m: float):
        self.k_over_m = k_over_m

    def step(self, x, v, dt):
        n = len(x)

        for i in range(n):
            a = -self.k_over_m * x[i]
            x[i] += dt * v[i]
            v[i] += dt * a

        return x, v

