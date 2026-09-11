1. Data / Sample Input

1.1 Proposed Dataset

The proposed proof-of-concept evaluation will use a publicly available IoT cybersecurity dataset to evaluate the proposed Adaptive Differential Privacy (ADP) approach in a heterogeneous Federated Learning environment.

N-BaIoT and ToN-IoT are potential dataset candidates because they contain IoT-related network and cybersecurity data.

The final dataset will be selected based on:

- Relevance to IoT security
- Data characteristics
- Feature suitability
- Availability of sufficient data samples
- Presence of different traffic or attack categories
- Suitability for non-IID partitioning across simulated clients


1.2 Intended Use

The selected dataset will be used as input for the proposed Federated Learning experiment.

The dataset will be:

1. Obtained from a publicly available source.
2. Preprocessed before model training.
3. Distributed among multiple simulated IoT clients.
4. Partitioned to create heterogeneous and non-IID conditions.
5. Used to evaluate the proposed Adaptive Differential Privacy approach.


1.3 Data Preprocessing

The selected dataset will be checked for:

- Missing values
- Duplicate records
- Inconsistent data
- Irrelevant information

Unnecessary records and features will be removed. Categorical data will be encoded, and numerical features may be scaled when required.


1.4 Non-IID Data Distribution

After preprocessing, the dataset will be distributed among multiple simulated IoT clients.

Different clients will receive different:

- Proportions of attack types
- Numbers of samples
- Data distributions

For example, some clients may contain predominantly one attack type, while others may contain mixed data or fewer samples.

This distribution will represent statistical heterogeneity among IoT clients.


1.5 Sample Input

The Sample_Input.csv file provides an illustrative example of the proposed data structure and client distribution.

It is not extracted from the final dataset.

The actual dataset will be selected and obtained during the implementation stage.


1.6 Dataset Sources

1.6.1 N-BaIoT

N-BaIoT is a potential dataset candidate for the proposed research.

Official source:
https://archive.ics.uci.edu/dataset/442/detection_of_iot_botnet_attacks_n_baiot


1.6.2 ToN-IoT

ToN-IoT is another potential dataset candidate for the proposed research.

Official source:
https://research.unsw.edu.au/projects/toniot-datasets


1.7 Data Privacy

Only publicly available data will be considered.

No confidential, private, sensitive, or restricted dataset will be uploaded to the GitHub repository.
