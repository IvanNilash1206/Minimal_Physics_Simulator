# src/mpe/batch/benchmark.py

import time
import numpy as np

def benchmark_backend(integrator, x, v, dt, steps):
    start = time.perf_counter()

    for _ in range(steps):
        x, v = integrator.step(x, v, dt)

    end = time.perf_counter()

    total_time = end - start

    steps_per_sec = steps/total_time

    return steps_per_sec, total_time

