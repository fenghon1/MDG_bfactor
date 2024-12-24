import sys
from multiprocessing import Pool
import multiprocessing
import time
import numpy as np
import os
from sklearn.linear_model import LinearRegression
import argparse
import utilities as ut

my_path = {}
my_path["bin_dir"] = "bin"
my_path["src_dir"] = "src"
my_path["data_dir"] = "datasets"
my_path["features_dir"] = "features"
my_path["results_dir"] = "results"

parser = argparse.ArgumentParser(description="modeling")
parser.add_argument("--dataset_name", type=str)
parser.add_argument("--kernel_type", type=str)
parser.add_argument("--kappas", type=str, default="2-5")
parser.add_argument("--curvature_types", type=str)
parser.add_argument("--use_delta_filter", type=int, default=0)
parser.add_argument("--upper_eta", type=int)
parser.add_argument("--lower_eta", type=int, default=5)
parser.add_argument("--dx", type=int)

args = parser.parse_args()

dataset_name = args.dataset_name
upper_eta = args.upper_eta
lower_eta = args.lower_eta
curvature_types = args.curvature_types.split("-")

curvature_types_map = {"gaussian": "G", "mean": "M", "gaussian-mean": "G-M"}

results_path = f"{my_path['results_dir']}/{dataset_name}"
os.makedirs(results_path, exist_ok=True)

dataset_path = f"{my_path['data_dir']}"
pdb_path = f"{my_path['data_dir']}/{dataset_name}"
feature_path = f"{my_path['features_dir']}/{dataset_name}"

list_pdbids = open(f"{dataset_path}/list-{dataset_name}.txt").read().splitlines()

kappas = np.array(args.kappas.split("-")).astype(int)

etas = np.arange(args.lower_eta, upper_eta, args.dx)


def process_pdbid(pdbid):
    # print(pdbid)
    filepath = f"{pdb_path}/{pdbid}.pdb"
    save_feature_path = f"{feature_path}/{pdbid}"

    X_train = []
    for kappa in kappas:
        for curvature_type in curvature_types:
            for eta in etas:
                save_path = f"{save_feature_path}/DGGL-{curvature_type}-{args.kernel_type}-eta-{eta:.1f}-kappa-{kappa}.npy"
                X_train.append(np.load(save_path))

    X_train = np.concatenate(X_train, axis=1)

    CA_coor, labels = ut.get_protein_ca_atom_coordinate(pdbid, filepath)

    X_norm = ut.normalize_feature(X_train)

    model = LinearRegression()

    return ut.fitting(X_norm, labels, model)


if __name__ == "__main__":

    start_time = time.time()

    with Pool(multiprocessing.cpu_count()) as pool:
        results = pool.map(process_pdbid, list_pdbids)

    print(results_path)
    fw = open(
        f"{results_path}/R-kappas-{args.kappas}-lower-eta-{args.lower_eta}-upper-eta-{upper_eta}-k{args.kernel_type[0]}-dx-{args.dx}-curv_type-{curvature_types_map[args.curvature_types]}.csv",
        "w",
    )
    for pdbid, r in zip(list_pdbids, results):
        print(f"{pdbid},{r:.3f}", file=fw)
    fw.close()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time:.2f} seconds")
