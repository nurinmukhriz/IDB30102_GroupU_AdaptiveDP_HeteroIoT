# CHAPTER 2: LITERATURE REVIEW

## 2.1 Introduction
This chapter reviews existing literature related to IoT environments, Federated Learning, privacy-preserving techniques, Differential Privacy, and adaptive privacy mechanisms. The review compares findings from the selected studies to identify existing approaches, challenges, and research gaps relevant to privacy protection in heterogeneous IoT environments.

## 2.2 Internet of Things and Heterogeneous IoT Environments

### 2.2.1 IoT Environments
The Internet of Thing (IoT) consists of interconnected devices that collect, process, and exchange data to support diverse applications and services. Based on the reviewed literature, IoT is implemented across healthcare, smart cities, industrial systems, and wearable or sensor-based application. These environments differ in their device characteristics, data types, operational requirements, and resource constraints.

Healthcare and Internet of Medical Things (IoMT) represent important IoT environment involving medical sensors, wearable devices, and sensitive patient information. Sharma and Guleria (2023) examined FL for healthcare applications involving chest X-ray and larynx cancer data, while Prasanna et al. (2024) and Revathy et al. (2024) investigated healthcare and wearable IoT data. Smart city applications were examined by Sundaram and Jayaprakash (2025) and Ushasree et al. (2026), whereas Ennaji et al. (2024) and Chen et al. (2023) focused on IoT environments. Wearable and sensor-based devices were investigated by Kumar et al. (2025) and Hidayat et al. (2023)
Overall, these studies demonstrate that IoT is not a uniform environment, creating different forms of heterogeneity that must be considered when applying FL.

### 2.2.2 Heterogeneity in IoT Environments
Heterogeneity is a fundamental characteristic of IoT environments because participating devices may differ in their capabilities and operating conditions. The reviewed literature identifies several dimensions, including computational capability, resource availability, and data distribution.

IoT devices may have different processing capabilities and resource limitations. Hidayat et al. (2023), for example, evaluated FL using Raspberry Pi and Android clients, while Ogundipe and Shi (2024) reported that their FL-based IoT approach was resource-intensive. Energy availability also varies among devices, with Nambiar et al. (2026) addressing energy and communication constraints through resource-aware aggregation and client selection. In addition, data may be distributed unevenly across clients, resulting in non-IID data. Arafeh et al. (2023) addressed this issue together with device heterogeneity and stragglers.

Therefore, these variations indicate that IoT devices cannot always be treated as having identical operating conditions, which may affect FL performance and resource requirements.

## 2.3 Federated Learning in IoT Environments

### 2.3.1 Federated Learning Approaches
FL enables multiple clients to collaboratively train a shared model while keeping their local training data on their respective devices. The reviewed literature demonstrates that different FL approaches have been deployed to address the operational characteristics of IoT environments, particularly aggregation, heterogeneity, personalisation and adaptive training.

FedAvg is a fundamental FL approach that aggregates model updates from participating client to construct a global model. Karimy and Reddy (2024) applied CNN-based FL with FedAvg to IoT intrusion detection, while Ennaji et al. (2024) used DNN-based FL with FedAvg for IoT traffic. However, conventional aggregation may be less suitable when client conditions vary. FedProx addresses client differences, as demonstrated by Sharma and Guleria (2023) and Oladele et al. (2026), who combined FedProx with personalized graph FL for IoT heterogeneity and label scarcity.

Personalized FL allows model to adapt to individual clients with different data distributions, while hierarchical FL introduces multiple aggregation levels. Sandilya et al. (2025), for example, implemented a three-layer hierarchical FL approach. Asynchronous FL accommodates differences in client participation and processing time; Arafeh et al. (2023) combined client clustering with FedAsync to address non-IID data, heterogeneity, and stragglers.

Other approaches focus on resource and energy efficiency. Nambiar et al. (2026) proposed Energy-Aware FL using resource-aware aggregation and client selection. Meanwhile, privacy-preserving and adaptive FL approaches integrate additional mechanisms to address security and constraints of participating clients.

### 2.3.2 Challenges of Federated Learning in IoT
Despite the development of various FL approaches, several challenges remain in IoT environments. Non-IID data is major challenge because clients may possess different data distributions. Arafeh et al. (2023) identified non-IID data alongside device heterogeneity and stragglers as key challenges in IoT FL.

Device heterogeneity also affects FL because participating devices differ in computational capability, available resources, and participation conditions. In addition, communication overhead remains a concern because clients must repeatedly exchange model updates, particularly in resource-constrained environments. Computational limitations and energy consumption may further restrict participation, while increasing number of clients create scalability challenges. Existing studies have therefore explored asynchronous aggregation, hierarchical FL, energy-aware client selection, and other resource-efficient approaches to address these limitations.

Overall, existing FL approaches address operational challenges such as data heterogeneity, resource constraints and scalability. However, these approaches do not eliminate privacy risks associated with collaborative model training. Therefore, the following section examines privacy-preserving techniques and Differential Privacy used to strengthen FL in IoT environments.

## 2.4 Privacy-Preserving Techniques in Federated Learning

### 2.4.1 Differential Privacy
DP is a mathematical privacy-preserving technique that limits the extent to which individual data can be inferred from a model or computation. In FL, DP is commonly implemented by clipping model updates and adding controlled noise before updates are shared with other participants. The level of privacy is generally controlled through a privacy budget, where stronger privacy protection requires greater noise. Fang et al. (2024), for example applied LIP-adaptive DP to protect healthcare data against gradient leakage while maintaining model performance. Similarly, Rawat and Singal (2025) combined DP with anonymisation for privacy-aware IoT intrusion detection. These studies demonstrate that DP can be integrates into FL without requiring the raw data to leave local devices. However, increasing the level of noise can affect model accuracy and training performance, creating a trade-off that must be considered in IoT environments.

### 2.4.2 Other Privacy-Preserving Techniques
Besides DP, several alternative techniques have been explored in FL. Homomorphic Encryption (HE) enables computation to be performed on encrypted data, while secure aggregation prevents the server directly observing individual client updates. For example, combined DP and HE to provide privacy protection for healthcare IoT data (Saidi et al., 2026). Khalaifat et al. (2025) investigated secure aggregation using ECDH and masking to protect client updates while reducing communication overhead. Blockchain-based approaches have also been used to provide integrity, traceability, and decentralized coordination in IoT FL (Chen et al., 2023; Ganapathy et al., 2024). However, these alternatives may introduce additional overhead for resource-constrained IoT devices. Therefore, DP is particularly relevant to this study because its privacy level can be controlled through noise and privacy parameters, supporting adaptive privacy mechanisms without relying on additional cryptographic infrastructure.

## 2.5 Differential Privacy in Federated Learning

### 2.5.1 Fixed Differential Privacy
In conventional DP-based FL, a predetermined privacy configuration is applied throughout the training process. The same privacy setting is generally used across participating clients, resulting in a consistent level of noise during model updates. For example, Rawat and Singal (2025) apply DP in IoT intrusion-detection setting and observed a reduction in accuracy when privacy protection was introduced. Although fixed DP is relatively simple to implement and evaluate, it does not explicitly account for differences in client conditions, such as computational capability, resource availability, or data characteristic. This limitation becomes more relevant in heterogeneous IoT environments

### 2.5.2 Adaptive Differential Privacy
Adaptive DP extends conventional DP by allowing privacy protection to change according to selected conditions rather than remaining fixed through training. The privacy budget or noise level can be adjusted according to factors such as training progress or other system conditions. For example, Wang et al. (2023) incorporated adaptive DP into RPIFL for IoT and investigated different privacy settings while maintaining accuracy close to FedAvg. Fang et al. (2024) also applied LIP-adaptive DP to address gradient leakage in healthcare FL. These studies demonstrate that adaptive DP can provide more flexible privacy control than a fixed configuration. However, the criteria used for adaptation differ between approaches, indicating the need to examine how privacy adaptation can respond to heterogeneous IoT conditions.

### 2.5.3 Existing Adaptive Differential Privacy Approaches
Existing literature demonstrates that adaptive DP has already been explored in several FL settings. Wang et al. (2023) proposed RPIFL for IoT, incorporating adaptive DP to balance privacy and reliability while evaluating different privacy settings. Fang et al. (2024) introduced LIP-adaptive DP for healthcare FL, focusing on reducing gradient leakage while maintaining model performance. Saidi et al. (2026) further combined DP with HE and provided tunable privacy-sharing for heterogeneous healthcare IoT environments. These studies show that adaptive privacy mechanisms can improve flexibility in privacy protection. However, their adaptation objectives differ, with emphasis placed on reliability, gradient leakage, or healthcare-specific privacy requirement. Limited investigation remains on adapting privacy protection according to heterogeneous IoT device and environmental conditions while jointly evaluating privacy, model performance, and resource efficiency.

## 2.6 Privacy-Performance Trade-offs in Federated Learning

### 2.6.1 Privacy and Model Performance
Increasing privacy protection through stronger DP generally introduces a performance trade-odd because greater noise can reduce the accuracy of the trained model. Rawat and Singal (2025) reported a decrease in accuracy once DP and anonymisation were applied to IoT intrusion detection. Fang et al. (2024) similarly demonstrated the need to balance privacy protection against model performance when applying adaptive DP. Therefore, selecting an appropriate privacy level is important to prevent excessive degradation in FL model performance.

### 2.6.2 Privacy and Computational Efficiency
Privacy-preserving mechanisms can also increase computational cost. DP requires additional processing for operations such as gradient clipping and noise generation, while cryptographic approaches such as HE and secure aggregation may introduce greater computational overhead. Saidi et al. (2026) reported increasing overhead when privacy mechanisms were combined with HE. This is particularly relevant for resource-constrained IoT devices with limited processing capabilities.

### 2.6.3 Privacy and Communication Efficiency
Privacy mechanisms may also affect communication in efficiency FL. Secure aggregation and cryptographic techniques can introduce additional communication requirements, particularly when multiple operations are performed during update exchange. Khalaifat et al. (2025), for example, evaluated communication overhead associated with secure aggregation in resource-limited IoT environments. Consequently, privacy mechanism must protect and be considered alongside communication efficiency when designing FL for distributed IoT devices. 

### 2.6.4 Privacy and Resource Efficiency in IoT
The privacy-resource trade-off becomes more significant in heterogeneous IoT environments because devices have different computational and energy capabilities. Nambiar et al. (2026) focuses energy and communication constraints through resource-aware FL in IoT, while Hidayat et al. (2024) demonstrated differences in computational requirements among Raspberry Pi and Android clients. These findings suggest that privacy mechanisms should consider device limitations to avoid imposing excessive resource costs on constrained clients.

## 2.7 Adaptive Differential Privacy for Heterogeneous IoT

### 2.7.1 Privacy Adaptation and IoT Device Conditions
Heterogenous IoT devices differ in computational capability, energy availability, and communication conditions, which may affect the cost of applying privacy protection. Existing adaptive DP studies demonstrate that privacy settings can be adjusted according to selected training or data conditions. However, Wang et al. (2023) primarily address privacy and reliability, while Fang et al. (2024) focus on gradient leakage in healthcare FL. These approaches do not explicitly establish device capability as a basis for privacy adaptation.\

### 2.7.2 Resource-Aware Federated Learning
Resource-aware FL addresses limitations in IoT devices by considering energy, computation, or communication requirements. Nambiar et al. (2026) used resource-aware client selection and aggregation to address energy and communication constraints, while Hidayat et al. (2023) proposed DP with compressive sensing for resource-constrained devices. However, resource awareness is generally applied to FL training or communication rather than directly determining privacy parameters.

### 2.7.3 Data Heterogeneity in Federated Learning
Data heterogeneity is another important consideration in IoT FL because clients may have different data distributions. Arafeh et al. (2023) addressed non-IID data through client clustering and asynchronous aggregation, while Oladele et al. (2026) used personalised graph FL and FedProx to address heterogeneous IoT data. These studies show that heterogeneity can influence FL performance, but it is not consistently incorporated into privacy adaptation.

### 2.7.4 Comparison of Existing Approaches
Overall, existing studies address privacy adaptation, resource constraints, and data heterogeneity as related but largely separate considerations. Adaptive DP provides flexible privacy control, while resource-aware and heterogeneity-aware FL approaches address device and data differences. Therefore, there remains limited investigation into whether privacy parameters can be adapted according to heterogeneous IoT conditions while jointly evaluating privacy, model performance, and resource efficiency. This forms the focus of the proposed study.

## 2.8 Comparative Literature Review Table

**Table 2.2: Comparative Analysis of Existing Privacy-Preserving Federated Learning Approaches**

| Author/Year | IoT Context | FL Approach | Privacy Technique | Adaptive Privacy | Heterogeneity | Resource Consideration | Key Limitation |
|---|---|---|---|---|---|---|---|
| Rawat and Singal (2025) | IoT IDS | FedAvg | DP + anonymisation | No | Limited | Limited | Privacy reduces accuracy |
| Hidayat et al. (2023) | Resource-constrained IoT | FL | DP + compressive sensing | No | Device/resource | Yes | Privacy setting not client-adaptive |
| Wang et al. (2024) | IoT | RPIFL | Adaptive DP | Yes | Limited | Yes | Adaptation focuses on privacy/reliability |
| Fang et al. (2024) | Healthcare IoT | FL | LIP-adaptive DP | Yes | Limited | Limited | Focuses on gradient leakage |
| Kumar et al. (2025) | IoT / wearable | Hierarchical FL | DP + HE | Limited | Yes | Yes | No adaptive privacy mechanism |
| Nambiar et al. (2026) | Energy-constrained IoT | Energy-Aware FL | - | No | Yes | Yes | Privacy does not address |
| Saidi et al. (2026) | Healthcare IoT | FL | DP + HE | Tunable | Yes / non-IID | Partial | Privacy-sharing remains constrained by overhead |
| Arafeh et al. (2023) | IoT | C-SplitFed / Split FL + FedAsync | - | No | Yes / non-IID | Stragglers | Simulated heterogeneity; privacy not directly measured |
| Oladele et al. (2026) | IoT cybersecurity | Personalised Graph FL + FedProx | - | No | Yes / non-IID | Limited | Complex approach; benign-only data may not capture novel attacks |
| Khailafat et al. (2025) | Resource-limited IoT | FL | Secure aggregation using ECDH + masking | No | Yes / non-IID | Yes | Cryptographic overhead; limited dynamic real-world scalability |
| **Proposed Study** | Heterogeneous IoT | FL | Adaptive DP | Yes | Device + data | Yes | To be evaluated |

## 2.9 Research Gap

### 2.9.1 Limitations of Existing Adaptive Approaches
Existing adaptive DP approaches demonstrate flexible privacy control, but their adaptation is primarily based on specific factors such as privacy requirements, training conditions, or data characteristics rather than heterogeneous device conditions.

### 2.9.2 Limited Consideration of Heterogeneous IoT Conditions
Although existing studies address device, resource, and data heterogeneity through aggregation, client selection, or personalized learning, limited attention is given to incorporating these conditions directly into privacy adaptation.

### 2.9.3 Privacy-Performance-Resource Trade-off
Existing work addresses trade-offs among privacy, model performance, and resource efficiency, but these factors are rarely evaluated jointly under heterogeneous IoT conditions. Therefore, limited investigation remains into adapting privacy protection according to device and data conditions while explicitly evaluating this combined trade-off.

## 2.10 Chapter Summary
This chapter reviewed IoT environments, FL approaches, privacy-preserving techniques, and Differential Privacy, with emphasis on fixed and adaptive mechanisms. The literature show that IoT heterogeneity and privacy protection introduce performance and resource trade-offs. Although adaptive DP has been explored, limited research jointly considers device and data heterogeneity when adapting privacy protection. The next chapter presents the methodology for the proposed Adaptive DP module. 


