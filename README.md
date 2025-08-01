# MDG_Bfactor

<div align='center'>
 
<!-- [![preprint](https://img.shields.io/static/v1?label=arXiv&message=2310.12508&color=B31B1B)](https://www.google.com/) -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

**Title** - Multiscale differential geometry learning for protein flexibility analysis.

**Authors** - Hongsong Feng, Jeffrey Y. Zhao, and Guo-Wei Wei

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Datasets](#datasets)
- [Modeling with mDG-based features](#modeling-with-mdg-based-features)
  - [I. mDG feature generation for 365 proteins](#i-mdg-feature-generation-for-365-proteins)
  - [II. mDG-based B-factor least square approximation](#ii-mdg-based-b-factor-least-square-approximation)
- [Results](#results)
  - [Modeling the Set-364 B-factor dataset](#modeling-the-set-364-b-factor-dataset)
- [License](#license)
- [Citation](#citation)

---

## Introduction

Protein flexibility is crucial for understanding protein structures, functions, and dynamics, and it can be measured through experimental methods such as X-ray crystallography. Theoretical approaches have also been developed to predict B-factor values, which reflect protein flexibility. Previous models have made significant strides in analyzing B-factors by   fitting experimental data. In this study, we propose a novel approach for B-factor prediction using differential geometry theory, based on the assumption that the intrinsic properties of proteins reside on a family of low-dimensional manifolds embedded within the high-dimensional space of protein structures. By analyzing the mean and Gaussian curvatures of a set of kernel-function-defined low-dimensional manifolds, we develop effective and robust multiscale differential geometry (mDG) models. Our mDG model demonstrates a 27\% increase in accuracy compared to the classical Gaussian network model (GNM) in predicting B-factors for a dataset of 364 proteins. Additionally, by incorporating both global and local protein features, we construct a highly effective machine learning model for the blind prediction of B-factors. Extensive   least-squares approximations and machine learning-based blind predictions    validate the effectiveness of the mDG modeling approach for B-factor prediction.

> **Keywords**: Multiscale differential geometry; protein flexibility; blind prediction.

---

## Prerequisites

- numpy                     1.21.0
- scipy                     1.7.3
- scikit-learn              1.0.2
- python                    3.10.12
- biopandas                 0.4.1
- Biopython                 1.75

--- 

## Datasets


| Datasets         | Total | Set                      |
|-------------------|-------|--------------------------|
| Bfactor-Set364   | 364   | [Data](./datasets)       |
| Bfactor-small    | 30    | [Data](./datasets)       |
| Bfactor-medium   | 36    | [Data](./datasets)       |
| Bfactor-large    | 34    | [Data](./datasets)       |


- Data for B-factor datasets: molecular 3D structures [Data](./datasets/365)
- Global features used for blind predictions [Data](./features/features-blind-prediction/)


---

## Modeling with mDG-based features

### I. mDG feature generation for 365 proteins

```shell
python codes/run_Bfactor-DG-features.py
```
---

### II. mDG-based B-factor least square approximation
```shell
python codes/run_model-Bfactor-DG.py --dataset_name Bfactor-small
```
---
## Results

### Modeling the Set-364 b-factor dataset
| Models       | [GNM](https://dyn.life.nthu.edu.tw/oGNM/oGNM.php)  | pfFRI | ASPH | opFRI | EH   | mDG [result](./Results)|
|--------------|-------|-------|------|-------|------|------|
| PCC          | 0.565 | 0.626 | 0.65 | 0.673 | 0.698| 0.715|

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Citation

- Hongsong Feng, Jeffrey Y. Zhao, and Guo-Wei Wei, "Multiscale differential geometry learning for protein flexibility analysis", Journal of Computational Chemistry, 2025

---
