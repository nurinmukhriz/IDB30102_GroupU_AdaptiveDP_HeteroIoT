# Arafeh et al. (2023)

## Paper Title
Efficient Privacy-Preserving ML for IoT: Cluster-Based Split Federated Learning Scheme for Non-IID Data

## Author(s)
Mohamad Arafeh, Mohamad Wazzeh, Hani Sami, Hakima Ould-Slimane, Chamseddine Talhi, Azzam Mourad, and Hadi Otrok

## Year
2023

## Research Problem
The study addresses non-IID data, device heterogeneity, limited resources, and stragglers in Federated Learning for IoT environments.

## Method / Technique
The approach uses Split Federated Learning with client clustering and asynchronous aggregation. The approach groups clients according to data and execution characteristics to reduce the effects of heterogeneity and stragglers.

## Dataset / Tools
The experiments use a simulated FL environment with Python and PyTorch.

## Main Findings
The approach improves the handling of non-IID data and differences in client resources while reducing the impact of stragglers.

## Limitation
The study mainly evaluates simulated heterogeneous conditions. Privacy is considered through the FL/Split Learning architecture but is not directly measured as a privacy metric.

## Relevance to Proposed Research
This paper supports the proposed research by demonstrating that device and data heterogeneity affect FL performance. It provides a basis for considering these heterogeneous conditions when designing adaptive privacy mechanisms.