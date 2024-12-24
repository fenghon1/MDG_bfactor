import os
import multiprocessing
from multiprocessing import Pool
import time

dataset_name = "365"
kernel_types = ["exp"]
kappas = [2, 5]

dataset_path = "datasets"
Bfactor_fileids = open(f"{dataset_path}/list-{dataset_name}.txt").read().splitlines()


def run_command(args):
    kernel_type, kappa, Bfactor_fileid, dataset_name = args
    cmd = f"python codes/Bfactor-DG-features.py --kernel_type {kernel_type} --dataset_name {dataset_name} --Bfactor_fileid {Bfactor_fileid} --kappa {kappa}"
    os.system(cmd)


tasks = [
    (kernel_type, kappa, Bfactor_fileid, dataset_name)
    for kernel_type in kernel_types
    for kappa in kappas
    for Bfactor_fileid in Bfactor_fileids
]

if __name__ == "__main__":

    start_time = time.time()
    with Pool(multiprocessing.cpu_count()) as pool:
        pool.map(run_command, tasks)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time:.2f} seconds")
