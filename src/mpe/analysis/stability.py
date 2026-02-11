import numpy as np
from src.mpe.core.state import State1D


def is_unstable(positions,threshold = 1e6):
    """
    detect numerical instability .
    Criteria:
        -NaN od Inf present
        - Magnitude exceedes threshold
    """
    
    if np.any(np.isnan(positions)):
        return True
    
    if np.any(np.isinf(positions)):
        return True

    if np.max(np.abs(positions)) > threshold:
        return True

    return False



def find_max_stable_dt(
        simulator_factory,
        integrator,
        force_model,
        mass,
        initial_state,
        dt_values,
        steps=10000,
        threshold = 1e6
    ):

    stability_result = {}
    max_stable_dt = None

    for dt in dt_values:
        sim = simulator_factory(integrator,force_model,mass)

        positions,_ = sim.run(initial_state,dt,steps)

        unstable = is_unstable(positions,threshold)

        stability_result[dt] = not unstable
    
        if not unstable:
            max_stable_dt = dt
        else:
            break
    return max_stable_dt , stability_result
