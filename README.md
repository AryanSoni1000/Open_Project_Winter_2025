# Machine Learning for Scalable Quantum State Tomography  
### QCG × PaAC Open Project (Winter 2025–2026)

---

## 1. Overview

Quantum State Tomography (QST) aims to reconstruct the density matrix of an unknown quantum state from measurement data. Traditional tomography scales exponentially with the number of qubits, making it computationally expensive for larger systems.

This project explores a physics-informed and scalable machine learning pipeline for reconstructing valid quantum density matrices while preserving physical constraints and studying scalability behavior.

The work consolidates Assignments 1–3 into a unified, modular and reproducible research-style repository.



## 2. Problem Statement

Given limited measurement expectation values, reconstruct a valid quantum density matrix \( \rho \) such that:

- \( \rho = \rho^\dagger \) (Hermitian)
- \( \rho \succeq 0 \) (Positive Semi-Definite)
- \( \mathrm{Tr}(\rho) = 1 \) (Unit Trace)

The challenge lies in:
- Enforcing physical constraints
- Handling exponential state growth \( 2^n \)
- Maintaining reconstruction fidelity under limited observables



## 3. Physics-Informed Constraint Enforcement

Instead of predicting the density matrix directly, the neural network predicts a lower triangular matrix **L**.

The density matrix is reconstructed using a Cholesky-based parameterization:

\[
\rho = \frac{LL^T}{\mathrm{Tr}(LL^T)}
\]

This guarantees:

- Positive Semi-Definiteness by construction
- Hermiticity through matrix multiplication
- Unit trace via normalization

This removes the need for penalty-based constraint enforcement.



## 4. Model Architecture

- Model Type: Fully Connected Neural Network (MLP)
- Input: Measurement expectation values
- Output: Flattened lower-triangular matrix \( L \)
- Output dimension dynamically scales with \( 2^n \)

The model supports serialization via `pickle` for reproducibility.



## 5. Dataset Generation

No external dataset is used.

- Random valid density matrices are generated programmatically
- Measurement data is computed using selected Pauli observables:
  - ⟨Z ⊗ Z⟩  
  - ⟨Z ⊗ I⟩  
  - ⟨I ⊗ Z⟩  

Data is generated on-the-fly during training.



## 6. Training Pipeline

The training pipeline:
Generates random valid states
Computes measurement observables
Trains the neural network
Evaluates reconstruction metrics



## 7. Evaluation Metrics
7.1 Approximate Quantum Fidelity

Measures similarity between reconstructed and true states.

𝐹
(
𝜌
,
𝜎
)
F(ρ,σ)

7.2 Trace Distance

Measures distinguishability
	​
7.3 Inference Latency

Average reconstruction time per sample.



## 8. Results
8.1 Density Matrix Reconstruction

8.2 Fidelity vs Number of Qubits

As the number of qubits increases:
Fidelity generally decreases
The reconstruction problem becomes more underdetermined

8.3 Runtime vs Number of Qubits

For small systems (2–5 qubits), runtime remains negligible on standard CPU hardware. However, theoretical scaling is exponential due to Hilbert space growth.



## 9. Scalability Analysis

Experiments were conducted for 2–5 qubits.

Observations:
Output dimension scales as 
2
𝑛
2
n
Computational cost increases exponentially
Fidelity degrades for larger systems
Model capacity influences expressiveness (ablation study)



## 10. Ablation Study

An ablation study on hidden dimension shows:
Increased model capacity improves expressiveness
Performance is sensitive to random initialization
Over-parameterization does not guarantee monotonic improvement



## 11. Limitations

Limited measurement observables make reconstruction underdetermined
Model is lightweight and not heavily optimized
Scaling beyond small qubit systems remains computationally expensive
Surrogate fidelity metrics used in some experiments



## 12. Future Work

Classical shadow tomography
Parameter-efficient neural architectures
Transformer-based surrogates
Hardware validation
GPU acceleration
Scaling to 6+ qubits



## 13. Project Structure
Open_Project_Winter_2025/
│
├── data/
├── models/
├── notebooks/
├── results/
├── src/
├── README.md



## 14. Reproducibility

All models are stored in models/
Plots are stored in results/
Modular pipeline located in src/
The project runs on CPU and does not require GPU acceleration.



## 15. AI Usage Disclosure

AI tools were used for:
Debugging assistance
Code structuring
Documentation drafting

All conceptual design and implementation decisions were made independently.



## 16. Conclusion

This project demonstrates that physics-informed machine learning can reconstruct physically valid quantum states while maintaining scalability for small systems.
However, exponential growth of the Hilbert space remains the fundamental bottleneck, motivating further research into parameter-efficient and shadow-based approaches.


