# src/mpe/batch/base.py

from abc import ABC, abstractmethod

class BatchIntegrator(ABC):
    @abstractmethod
    def step(self, x, v, dt):
        """
        Perform one integration step for batched particles
        Return:
            (x, v)
        """
        pass
