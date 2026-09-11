Expected Output

Baseline Comparison

The proposed ADP approach will be compared with Fixed DP-FedAvg, where the same privacy setting is applied across all simulated clients. Both approaches will use the same dataset, FL model, number of clients, data distribution, and experimental environment to ensure a fair comparison. The main difference is that ADP adjusts privacy settings according to client conditions, while Fixed DP maintains a uniform privacy configuration.

Table 3.3: Baseline Comparison

| Aspect | Fixed DP-FedAvg | Adaptive DP-FedAvg |
|---|---|---|
| Privacy setting | Same for all clients | Adjusted by client conditions |
| Device capabilities | Not considered | Considered |
| Resources | Not considered | Considered |
| Data distribution | Same non-IID setup | Same non-IID setup |
| Dataset | Same | Same |
| FL model | Same | Same |
| Number of simulated IoT clients | Same | Same |
| Environment | Same | Same |


Evaluation Metrics

| Category | Evaluation Metric | Purpose |
|---|---|---|
| Privacy Protection | Privacy Budget (ε) | Measures the privacy level applied to the clients. A smaller ε value generally represents stronger privacy protection, while a larger ε value provides weaker privacy protection but may improve utility. |
| Model Performance | Accuracy | Measures the overall correctness of model predictions. |
| Model Performance | Precision | Measures the proportion of correct positive predictions. |
| Model Performance | Recall | Measures the ability to correctly identify positive cases. |
| Model Performance | F1-score | Provides a balance between precision and recall. |
| Resource Efficiency | Computation Time | Measures the time required for model training and processing. |
| Resource Efficiency | Communication Overhead | Measures the communication cost during Federated Learning. |
| Resource Efficiency | Latency | Measures the delay during the Federated Learning process. |


Explanation of Expected Research Outcomes

The proposed ADP approach is expected to provide a better balance trade-off between privacy protection, model performance, and resource efficiency than Fixed DP under heterogeneous IoT conditions. The evaluation will determine whether adapting privacy settings to client conditions can reduce the performance and resource costs associated with uniform privacy protection while maintaining an appropriate level of privacy.
