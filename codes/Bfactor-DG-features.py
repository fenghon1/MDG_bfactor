from scipy.spatial import distance
import os
import argparse
import numpy as np
import utilities as ut
import DG_path
from Gaussian_mean_curvature import Curvature_Exp, Curvature_Lor


def main(args):

    mypath = DG_path.path_config()

    kappa = args.kappa
    Bfactor_fileid = args.Bfactor_fileid
    feature_path = f"{mypath['features_dir']}/{args.dataset_name}"
    os.makedirs(feature_path, exist_ok=True)

    pdbid = Bfactor_fileid.split(".")[0]
    Bfactor_file_path = f"{mypath['data_dir']}/{args.dataset_name}/{Bfactor_fileid}.pdb"

    CA_coors, labels = ut.get_protein_ca_atom_coordinate(pdbid, Bfactor_file_path)

    nrow, ncol = np.shape(CA_coors)
    Dists = distance.cdist(CA_coors, CA_coors)
    Dists_use = []
    for id, dists in enumerate(Dists):
        mask = [i for i in range(nrow) if i != id]
        dists_use = dists[mask]
        Dists_use.append(dists_use)

    etas = np.arange(5, 31, 4)

    indices = np.array([i for i in range(nrow)])
    for eta in etas:
        curvatures_K = []
        curvatures_H = []
        for ip, point in enumerate(CA_coors):
            mask = indices != ip
            density_cloudpoints = CA_coors[mask]
            if args.kernel_type == "exp":
                curvature_K, curvature_H = Curvature_Exp(
                    eta, [point], density_cloudpoints, kappa
                )
            elif args.kernel_type == "lor":
                curvature_K, curvature_H = Curvature_Lor(
                    eta, [point], density_cloudpoints, kappa
                )
            curvatures_K.append(curvature_K)
            curvatures_H.append(curvature_H)

        save_feature_path = f"{feature_path}/{pdbid}"
        os.makedirs(save_feature_path, exist_ok=True)

        curvature_type = "gaussian"
        save_path = f"{save_feature_path}/DGGL-{curvature_type}-{args.kernel_type}-eta-{eta:.1f}-kappa-{kappa}.npy"
        np.save(save_path, curvatures_K)

        curvature_type = "mean"
        save_path = f"{save_feature_path}/DGGL-{curvature_type}-{args.kernel_type}-eta-{eta:.1f}-kappa-{kappa}.npy"
        np.save(save_path, curvatures_H)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="feature generation")
    parser.add_argument("--kernel_type", type=str)
    parser.add_argument("--dataset_name", type=str)
    parser.add_argument("--Bfactor_fileid", type=str)
    parser.add_argument("--kappa", type=int)
    args = parser.parse_args()

    print(args)

    main(args)
