# mGLI-KDA

<div align='center'>
 
<!-- [![preprint](https://img.shields.io/static/v1?label=arXiv&message=2310.12508&color=B31B1B)](https://www.google.com/) -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

**Title** - Knot data analysis using multiscale Gauss link integral.

**Authors** - Li Shen, Hongsong Feng, Fengling Li, Fengchun Lei, Jie Wu, and Guo-Wei Wei

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Model Architecture](#model-architecture)
- [Prerequisites](#prerequisites)
- [Visualization tools](#Visualization-tools)
- [Datasets](#datasets)
- [Modeling with mGLI-based features](#Modeling-with-mGLI-based-features)
    - [mGLI-based B-factor prediction](#i-mgli-based-b-factor-prediction)
    - [Generation of mGLI-based features for protein-ligand complex](#II-Generation-of-mGLI-based-features-for-protein-ligand-complex)
    - [Generation of mGLI-based features for small molecule](#III-Generation-of-mGLI-based-features-for-small-molecule)
    - [Generation of sequence-based features for protein or small molecules](#IV-Generation-of-sequence-based-features-for-protein-or-small-molecules)

- [Results](#results)
    - [I. Modeling the B-factor datasets]()
    - [II. Modeling the PDBbind datasets]()
- [License](#license)
- [Citation](#citation)

---

## Introduction

Protein flexibility is crucial for understanding protein structures, functions, and dynamics, and it can be measured through experimental methods such as X-ray crystallography. Theoretical approaches have also been developed to predict B-factor values, which reflect protein flexibility. Previous models have made significant strides in analyzing B-factors by   fitting experimental data. In this study, we propose a novel approach for B-factor prediction using differential geometry theory, based on the assumption that the intrinsic properties of proteins reside on a family of low-dimensional manifolds embedded within the high-dimensional space of protein structures. By analyzing the mean and Gaussian curvatures of a set of kernel-function-defined low-dimensional manifolds, we develop effective and robust multiscale differential geometry (mDG) models. Our mDG model demonstrates a 27\% increase in accuracy compared to the classical Gaussian network model (GNM) in predicting B-factors for a dataset of 364 proteins. Additionally, by incorporating both global and local protein features, we construct a highly effective machine learning model for the blind prediction of B-factors. Extensive   least-squares approximations and machine learning-based blind predictions    validate the effectiveness of the mDG modeling approach for B-factor prediction.

> **Keywords**: Knot data analysis, Gauss link integral, multiscale analysis.

---

## Model Architecture

Schematic illustration of the overall mGLI-based knot data analysis (KDA) platform is shown in below.

![Model Architecture](concepts.png)

Further explain the details in the [paper](https://github.com/WeilabMSU/mGLI-KDA), providing context and additional information about the architecture and its components.

---

## Prerequisites

- numpy                     1.21.0
- scipy                     1.7.3
- scikit-learn              1.0.2
- python                    3.10.12
- biopandas                 0.4.1
- Biopython                 1.75

---
## Visualization tools

- vispy 0.12.1

- [pyknotid](https://github.com/SPOCKnots/pyknotid)

- pymol

--- 

## Datasets

A brief introduction about the benchmarks.

| Datasets                |Total    | Training Set                 | Test Set                                             |
|-|-----------------------------|------------------------------|------------------------------                        |
| Bfactor-Set364 | 364  [Data](./datasets)     |   -    |      -                                                            |
| Bfactor-small | 30     [Data](./datasets)  |   -    |      -                                                            |
| Bfactor-medium | 36    [Data](./datasets)  |   -    |      -                                                            |
| Bfactor-large | 34   [Data](./datasets)    |   -    |      -                                                            |

- Data for B-factor datasets: molecular 3D structures
---

## Modeling with mGLI-based features
### I. mGLI-based B-factor prediction

```shell
# examples, dataset_name options: Bfactor-Set364, Bfactor-large, Bfactor-medium, Bfactor-small
python codes/mGLI-Bfactor.py --dataset_name Bfactor-small
```
---
## Results

### I. Modeling the Set-364 b-factor dataset
| Models       | [GNM](https://dyn.life.nthu.edu.tw/oGNM/oGNM.php) [result](./Results)  | pfFRI [result](./Results)| ASPH | opFRI [result](./Results)| EH   | mGLI [result](./Results)|
|--------------|-------|-------|------|-------|------|------|
| PCC          | 0.565 | 0.626 | 0.65 | 0.673 | 0.698| 0.762|

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Citation

- Hongsong Feng, Jeffrey Y. Zhao, and Guo-Wei Wei, "Multiscale differential geometry learning for protein flexibility analysis"

---
