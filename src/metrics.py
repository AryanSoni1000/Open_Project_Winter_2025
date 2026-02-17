import torch
import time

# -----------------------------
# Approximate Quantum Fidelity
# -----------------------------
def quantum_fidelity(rho, sigma):
    """
    Approximate fidelity for PSD density matrices
    F ≈ (Tr(rho @ sigma))^2
    """
    return (torch.trace(rho @ sigma).real ** 2).item()


# -----------------------------
# Trace Distance
# -----------------------------
def trace_distance(rho, sigma):
    diff = rho - sigma
    eigvals = torch.linalg.eigvals(diff)
    return 0.5 * torch.sum(torch.abs(eigvals)).item()


# -----------------------------
# Inference Latency
# -----------------------------
def inference_latency(model, x, runs=100):
    model.eval()
    start = time.time()
    with torch.no_grad():
        for _ in range(runs):
            _ = model(x)
    end = time.time()
    return (end - start) / runs
