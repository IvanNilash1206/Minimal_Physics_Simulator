import time

def measure_ns_per_step(sim,state,dt,steps):
    start= time.pref_counter()
    sim.run(state,dt,steps)
    end = time.pref_counter()

    total_ns = (end-start)*1e9

    return total_ns / steps
