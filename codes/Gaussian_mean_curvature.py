import numpy as np


def Curvature_Exp(etaij, X, XI, k):
    XI = np.array(XI)
    xi, yi, zi = XI.T

    X = np.array(X)
    x, y, z = X[:, 0][:, None], X[:, 1][:, None], X[:, 2][:, None]

    # x, y, z = X
    dx, dy, dz = x - xi, y - yi, z - zi
    r2 = dx**2 + dy**2 + dz**2
    r = np.sqrt(r2)
    r_k = r / etaij
    exp_term = np.exp(-(r_k**k))
    common = r_k ** (k - 1) / (etaij * r)
    common_2k_minus_2 = exp_term * (common) ** 2
    common_k_minus_1 = exp_term * common
    common_k_minus_2 = exp_term / (etaij**2 * r2) * r_k ** (k - 2)

    # Compute fx, fy, fz
    fx = -k * np.sum(common_k_minus_1 * dx, axis=1)
    fy = -k * np.sum(common_k_minus_1 * dy, axis=1)
    fz = -k * np.sum(common_k_minus_1 * dz, axis=1)

    # Compute fxx, fyy, fzz
    fxx = (
        k**2 * np.sum(common_2k_minus_2 * dx**2, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dx**2, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dx**2 / r2), axis=1)
    )
    fyy = (
        k**2 * np.sum(common_2k_minus_2 * dy**2, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dy**2, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dy**2 / r2), axis=1)
    )
    fzz = (
        k**2 * np.sum(common_2k_minus_2 * dz**2, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dz**2, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dz**2 / r2), axis=1)
    )

    # Compute fxy, fxz, fyz
    fxy = (
        k**2 * np.sum(common_2k_minus_2 * dx * dy, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dx * dy, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dx * dy / r2), axis=1)
    )
    fxz = (
        k**2 * np.sum(common_2k_minus_2 * dx * dz, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dx * dz, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dx * dz / r2), axis=1)
    )
    fyz = (
        k**2 * np.sum(common_2k_minus_2 * dy * dz, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dy * dz, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dy * dz / r2), axis=1)
    )

    # F2 = np.array([fx**2 + fy**2 + fz**2])
    F2 = fx**2 + fy**2 + fz**2
    mask = F2 < 1e-20
    K = np.zeros_like(F2)
    H = np.zeros_like(F2)

    K[~mask] = (
        2 * fx[~mask] * fy[~mask] * fxz[~mask] * fyz[~mask]
        + 2 * fx[~mask] * fz[~mask] * fxy[~mask] * fyz[~mask]
        + 2 * fy[~mask] * fz[~mask] * fxy[~mask] * fxz[~mask]
        - 2 * fx[~mask] * fz[~mask] * fxz[~mask] * fyy[~mask]
        - 2 * fy[~mask] * fz[~mask] * fxx[~mask] * fyz[~mask]
        - 2 * fx[~mask] * fy[~mask] * fxy[~mask] * fzz[~mask]
        + fz[~mask] ** 2 * fxx[~mask] * fyy[~mask]
        + fx[~mask] ** 2 * fyy[~mask] * fzz[~mask]
        + fy[~mask] ** 2 * fxx[~mask] * fzz[~mask]
        - fx[~mask] ** 2 * fyz[~mask] ** 2
        - fy[~mask] ** 2 * fxz[~mask] ** 2
        - fz[~mask] ** 2 * fxy[~mask] ** 2
    ) / F2[~mask] ** 2

    H[~mask] = (
        2 * fx[~mask] * fy[~mask] * fxy[~mask]
        + 2 * fx[~mask] * fz[~mask] * fxz[~mask]
        + 2 * fy[~mask] * fz[~mask] * fyz[~mask]
        - (fy[~mask] ** 2 + fz[~mask] ** 2) * fxx[~mask]
        - (fx[~mask] ** 2 + fz[~mask] ** 2) * fyy[~mask]
        - (fx[~mask] ** 2 + fy[~mask] ** 2) * fzz[~mask]
    ) / (2 * F2[~mask] ** 1.5)

    return K, H


def Curvature_Lor(etaij, X, XI, k):
    XI = np.array(XI)
    xi, yi, zi = XI.T

    X = np.array(X)
    x, y, z = X[:, 0][:, None], X[:, 1][:, None], X[:, 2][:, None]

    # x, y, z = X
    dx, dy, dz = x - xi, y - yi, z - zi
    r2 = dx**2 + dy**2 + dz**2
    r = np.sqrt(r2)
    r_k = r / etaij
    lor_term = 1 / (1 + r_k**k)
    common = r_k ** (k - 1) / (etaij * r)
    common_2k_minus_2 = lor_term**3 * (common) ** 2
    common_k_minus_1 = lor_term**2 * common
    common_k_minus_2 = lor_term**2 / (etaij**2 * r2) * r_k ** (k - 2)

    # Compute fx, fy, fz
    fx = -k * np.sum(common_k_minus_1 * dx, axis=1)
    fy = -k * np.sum(common_k_minus_1 * dy, axis=1)
    fz = -k * np.sum(common_k_minus_1 * dz, axis=1)

    # Compute fxx, fyy, fzz
    fxx = (
        2 * k**2 * np.sum(common_2k_minus_2 * dx**2, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dx**2, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dx**2 / r2), axis=1)
    )
    fyy = (
        2 * k**2 * np.sum(common_2k_minus_2 * dy**2, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dy**2, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dy**2 / r2), axis=1)
    )
    fzz = (
        2 * k**2 * np.sum(common_2k_minus_2 * dz**2, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dz**2, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dz**2 / r2), axis=1)
    )

    # Compute fxy, fxz, fyz
    fxy = (
        2 * k**2 * np.sum(common_2k_minus_2 * dx * dy, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dx * dy, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dx * dy / r2), axis=1)
    )
    fxz = (
        2 * k**2 * np.sum(common_2k_minus_2 * dx * dz, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dx * dz, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dx * dz / r2), axis=1)
    )
    fyz = (
        2 * k**2 * np.sum(common_2k_minus_2 * dy * dz, axis=1)
        - k * (k - 1) * np.sum(common_k_minus_2 * dy * dz, axis=1)
        - k * np.sum(common_k_minus_1 * (1 - dy * dz / r2), axis=1)
    )

    # F2 = np.array([fx**2 + fy**2 + fz**2])
    F2 = fx**2 + fy**2 + fz**2
    mask = F2 < 1e-20
    K = np.zeros_like(F2)
    H = np.zeros_like(F2)

    K[~mask] = (
        2 * fx[~mask] * fy[~mask] * fxz[~mask] * fyz[~mask]
        + 2 * fx[~mask] * fz[~mask] * fxy[~mask] * fyz[~mask]
        + 2 * fy[~mask] * fz[~mask] * fxy[~mask] * fxz[~mask]
        - 2 * fx[~mask] * fz[~mask] * fxz[~mask] * fyy[~mask]
        - 2 * fy[~mask] * fz[~mask] * fxx[~mask] * fyz[~mask]
        - 2 * fx[~mask] * fy[~mask] * fxy[~mask] * fzz[~mask]
        + fz[~mask] ** 2 * fxx[~mask] * fyy[~mask]
        + fx[~mask] ** 2 * fyy[~mask] * fzz[~mask]
        + fy[~mask] ** 2 * fxx[~mask] * fzz[~mask]
        - fx[~mask] ** 2 * fyz[~mask] ** 2
        - fy[~mask] ** 2 * fxz[~mask] ** 2
        - fz[~mask] ** 2 * fxy[~mask] ** 2
    ) / F2[~mask] ** 2

    H[~mask] = (
        2 * fx[~mask] * fy[~mask] * fxy[~mask]
        + 2 * fx[~mask] * fz[~mask] * fxz[~mask]
        + 2 * fy[~mask] * fz[~mask] * fyz[~mask]
        - (fy[~mask] ** 2 + fz[~mask] ** 2) * fxx[~mask]
        - (fx[~mask] ** 2 + fz[~mask] ** 2) * fyy[~mask]
        - (fx[~mask] ** 2 + fy[~mask] ** 2) * fzz[~mask]
    ) / (2 * F2[~mask] ** 1.5)

    return K, H
