# Oladele et al. (2026)

## Paper Title
G-PFL-ID: Graph-Driven Personalized Federated Learning for Unsupervised Intrusion Detection in Non-IID IoT Systems

## Author(s)
Daniel Ayo Oladele, Ayokunle Ige, Olatunbosun Agbo-Ajala, Olufisayo Ekundayo, Sree Ganesh Thottempudi, Malusi Sibiya, and Ernest Mnkandla

## Year
2026

## Research Problem
The study addresses data heterogeneity, label scarcity, and privacy challenges in IoT intrusion detection. Conventional FL approaches may struggle with non-IID data and limited labelled data.

## Method / Technique
The proposed G-PFL-ID framework combines graph-based learning, personalized Federated Learning, and FedProx. A global graph encoder is trained using a federated regularizer, followed by lightweight local personalization.

## Dataset / Tools
The study evaluates the approach using the IoT-23 and N-BaIoT datasets.

## Main Findings
The proposed approach achieved strong intrusion detection performance, including AUROC values of up to 99.46% on IoT-23 and 97.74% on N-BaIoT.

## Limitation
The approach is relatively complex, and its evaluation focuses on intrusion detection scenarios. Privacy is not directly evaluated using an adaptive privacy mechanism.

## Relevance to Proposed Research
This paper supports the proposed research by demonstrating how data heterogeneity and personalization can be handled in IoT Federated Learning. However, privacy adaptation according to heterogeneous conditions remains an area for further investigation.