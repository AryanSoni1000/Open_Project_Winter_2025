import numpy as np
import matplotlib.pyplot as plt

# Example dummy results (replace with real values if available)
fidelities = np.random.normal(0.98, 0.01, 100)
trace_distances = np.random.normal(0.02, 0.005, 100)
runtimes = np.random.normal(0.3, 0.05, 10)

# Fidelity Plot
plt.figure()
plt.plot(fidelities)
plt.title("Fidelity per Sample")
plt.xlabel("Sample Index")
plt.ylabel("Fidelity")
plt.savefig("../results/fidelity_plot.png")
plt.close()

# Trace Distance Plot
plt.figure()
plt.plot(trace_distances)
plt.title("Trace Distance per Sample")
plt.xlabel("Sample Index")
plt.ylabel("Trace Distance")
plt.savefig("../results/trace_distance_plot.png")
plt.close()

# Runtime Plot
plt.figure()
plt.plot(runtimes)
plt.title("Runtime per Training Run")
plt.xlabel("Run Index")
plt.ylabel("Runtime (seconds)")
plt.savefig("../results/runtime_plot.png")
plt.close()

print("Plots generated successfully.")

