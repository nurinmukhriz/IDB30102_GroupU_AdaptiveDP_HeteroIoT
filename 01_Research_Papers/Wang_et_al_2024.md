# Wang et al. (2024)

## Paper Title
RPIFL: Reliable and Privacy-Preserving Federated Learning for the Internet of Things

## Author(s)
Ruijin Wang, Jinshan Lai, Xiong Li, Donglin He, and Muhammad Khurram Khan

## Year
2024

## Research Problem
The study addresses privacy disclosure and model reliability problems in Federated Learning for IoT. Differential Privacy can improve privacy but may negatively affect model accuracy and reliability.

## Method / Technique
The proposed RPIFL framework combines a lightweight local network, multi-modal fine-grained model optimisation, and adaptive Differential Privacy.

## Dataset / Tools
CIFAR-10 and CIFAR-100 datasets were used. Non-IID data was simulated using a Dirichlet distribution with multiple FL clients.

## Main Findings
The proposed approach provides privacy protection while maintaining accuracy close to FedAvg. It achieved an average accuracy improvement of 1.1% compared with two privacy-preserving FL methods and reduced convergence time by more than 9%.

## Limitation
The adaptive privacy mechanism focuses mainly on privacy and model reliability rather than adapting privacy according to heterogeneous device resource conditions.

## Relevance to Proposed Research
This paper is highly relevant because it demonstrates the use of Adaptive Differential Privacy in IoT Federated Learning. It provides a foundation for further investigating adaptive privacy under heterogeneous device and environmental conditions.