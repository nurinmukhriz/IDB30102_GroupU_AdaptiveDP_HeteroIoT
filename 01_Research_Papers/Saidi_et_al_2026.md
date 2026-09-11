# Saidi et al. (2026)

## Paper Title
A Privacy-Aware Federated Learning Framework for Collaborative Healthcare IoT Security

## Author(s)
Rihab Saidi, Tarek Moulahi, Salah Zidi, and Sami Mahfoudhi

## Year
2026

## Research Problem
The study addresses privacy, non-IID data, device heterogeneity, resource limitations, and unstable communication in healthcare IoT Federated Learning.

## Method / Technique
The framework integrates TensorFlow Federated, Differential Privacy, and Homomorphic Encryption. It also introduces a controlled data-sharing mechanism to balance privacy and model performance.

## Dataset / Tools
The study uses the IoT-Healthcare-Security dataset and TensorFlow Federated. The framework is compared with FedAvg, FedProx, and FedSGD.

## Main Findings
The proposed framework achieved 98.53% accuracy while maintaining strong privacy protection. The study also found an optimal privacy-accuracy balance using controlled data sharing.

## Limitation
The combination of Differential Privacy, Homomorphic Encryption, and federated orchestration introduces computational and operational overhead. The controlled data-sharing mechanism also requires careful governance in real healthcare deployment.

## Relevance to Proposed Research
This paper is highly relevant because it demonstrates privacy-preserving FL under heterogeneous healthcare IoT conditions. It supports the proposed research by showing the importance of jointly considering privacy, model performance, and resource constraints.