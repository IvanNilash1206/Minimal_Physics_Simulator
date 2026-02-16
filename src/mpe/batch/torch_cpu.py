# src/mpe/batch/torch_cpu.py

import numpy as np
from src.mpe.batch.base import BatchIntegrator

class TorchCPUIntegrator(BatchIntegrator):
    def __init__(self, k_over_m: float):
        self.k_over_m = k_over_m

    def step(self, x, v, dt):
        a = -self.k_over_m * x
        x = x + dt * v
        v = v + dt * a

        return x, v

