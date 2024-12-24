import os
import pandas as pd
import numpy as np

os.chdir("/Users/hongsongfeng/Desktop/B-factor-DG/8-Bfactor-DGGL-standalone")

kernel_types = ["exp"]
dataset_names = ["365"]
curvature_typess = ["gaussian-mean"]
curvature_types_map = {"gaussian": "G", "mean": "M", "gaussian-mean": "G-M"}

use_delta_filters = [0]
dxs = [4]
upper_etas = [30]

for dataset_name in dataset_names:
    for kernel_type in kernel_types:
        for curvature_types in curvature_typess:
            for use_delta_filter in use_delta_filters:
                for dx in dxs:
                    for upper_eta in upper_etas:
                        cmd = f"python bin/model-Bfactor-DG.py --dataset_name {dataset_name} --kernel_type {kernel_type} --upper_eta {upper_eta} --dx {dx} --curvature_types {curvature_types}\n"

                        os.system(cmd)
