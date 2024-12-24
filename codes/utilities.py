from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
from Bio import PDB
import numpy as np
from sklearn.metrics import mean_squared_error


def normalize_feature(X):
    scaler = StandardScaler()
    scaler.fit(X)
    return scaler.transform(X)


def fitting(X_norm, labels, model):
    regressor = model.fit(X_norm, labels)
    y_pred = regressor.predict(X_norm)
    rmse = np.sqrt(mean_squared_error(y_pred, labels))
    return pearsonr(y_pred, labels)[0]


def get_protein_ca_atom_coordinate(pdbid, filepath):
    parser = PDB.PDBParser()
    struct = parser.get_structure(pdbid, filepath)

    CA_coordinates = np.array([])

    for model in struct:
        coor = []
        labels = np.array([])
        for chain in model:
            for residue in chain:
                for atom in residue:
                    if atom.id == "CA":
                        XYZ = atom.get_coord()
                        bfactor = atom.bfactor
                        labels = np.append(labels, bfactor)
                        CA_coordinates = np.hstack([CA_coordinates, XYZ])

        break

    return CA_coordinates.reshape(-1, 3), labels
