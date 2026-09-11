# Hidayat et al. (2023)

## Paper Title
Privacy-Preserving Federated Learning With Resource-Adaptive Compression for Edge Devices

## Author(s)
Muhammad Ayat Hidayat, Yugo Nakamura, and Yutaka Arakawa

## Year
2023

## Research Problem
The study addresses the high computational and communication costs of privacy-preserving Federated Learning on resource-constrained devices. Conventional encryption and blockchain techniques may be too expensive for devices with limited resources.

## Method / Technique
The study combines Differential Privacy with compressive sensing. A weight-pruning-based compression method is used with an adaptive compression ratio based on resource availability.

## Dataset / Tools
MNIST, Fashion-MNIST, and Human Activity Recognition datasets were used. The study also evaluated resource-constrained devices such as Raspberry Pi and Android devices.

## Main Findings
The proposed approach achieved slightly better accuracy than several existing DP-based methods while reducing total communication cost and training time. The study also evaluated resistance against poisoning attacks.

## Limitation
The study focuses mainly on resource-adaptive compression and privacy protection rather than adapting the privacy configuration itself according to different clients.

## Relevance to Proposed Research
This paper demonstrates that device resource differences should be considered in Federated Learning. It supports the proposed research by showing the importance of resource-aware mechanisms for privacy-preserving FL in heterogeneous IoT environments.