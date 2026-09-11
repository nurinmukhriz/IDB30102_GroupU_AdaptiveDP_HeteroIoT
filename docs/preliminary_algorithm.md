## Preliminary Code

The following pseudocode represents the preliminary logic of the proposed Adaptive Differential Privacy (ADP) module. It is provided as an initial representation of the proposed solution and does not represent the final implementation.

### Adaptive Differential Privacy for Federated Learning

```text

Algorithm: Adaptive Differential Privacy for FL

Input:
    Client data D_i
    Device capability C_i
    Data heterogeneity H_i
    Privacy range ε_min, ε_max

1. Initialise FL clients
2. Distribute non-IID data among clients
3. For each FL round:
      a. Train local model on client i
      b. Assess device capability C_i
      c. Assess data heterogeneity H_i
      d. Determine adaptive privacy parameter ε_i
      e. Clip local model update
      f. Add DP noise according to ε_i
      g. Send protected update to server
4. Aggregate protected updates using FedAvg
5. Distribute global model to clients
6. Repeat until training completes
7. Evaluate privacy, performance and resource efficiency

```

Output: Evaluated Adaptive DP-FL model

