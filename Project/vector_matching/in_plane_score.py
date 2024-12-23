from time import time
import numpy as np
import matplotlib.pyplot as plt
import pyxem as pxm
from pyxem.utils.indexation_utils import njit

new_params ={'font.size':18}
plt.rcParams.update(new_params)

@njit()
def get_in_plane_score(exp_peaks, sim_peaks,cut_off):
    """
    Calculates the in-plane score between an experimental dataset
    and a simulated dataset, by comparing one experimental frame to
    all simulated frames and finding the best fit.
    Parameters
    ----------
    exp_peaks: (N,2) ndarray
        Experimental r and theta values from one frame
    sim_peaks: (M,N,2) ndarray
        Simulated r and theta values
    cut_off: float 
        Distance cut-off to indicate similar values
    
    Returns
    ----------
    rot_cand: float
        The min difference in theta values for one frame
    """
    # List to store possible theta values
    rot_cand = []
    # Assume we take in one frame
    # Go through all values in exp_peaks
    for exp_peak in exp_peaks:
        # Compare to all frames in sim_peaks
        for sim_peak in sim_peaks:
            # Compare to all values in sim_peaks
            for sp in sim_peak:
                # Check distance requirement 
                if np.abs(exp_peak[0]-sp[0]) < cut_off:
                    # Get theta values at current iteration
                    ind_theta = np.abs(exp_peak[1]-sp[1])
                    # Disregard zero-values
                    if ind_theta > 0.0:
                        # Append the dTheta
                        rot_cand.append(ind_theta)
    # Return the lowest value of dtheta, this is the in-plane score 
    return min(rot_cand) 

def plot_in_plane_score(vecs):

    plt.figure(figsize=(8,6))
    for i in range(len(vecs)):
        plt.scatter(i,vecs[i],s=34,color='black')

    plt.grid(True)
    plt.ylabel(r'$\phi$',fontsize='26')
    plt.xlabel('Tilt Step', fontsize='26')
    plt.xticks()
    plt.yticks()
    # plt.legend()
    plt.tight_layout()
    plt.show()

def get_all_phis(p,sim,cut_off):
    # Store in-plane score 
    in_planes = []

    t1 = time()
    # Calculate in-plane-score for all experimental peaks 
    for i in range(len(p)):
        # Get in-plane score one frame at a time
        rot_i = get_in_plane_score(p[i],sim,cut_off)
        # Convert from radians to degrees
        rot_i = np.rad2deg(rot_i)
        # Save the rotation
        in_planes.append(rot_i)
    t2 = time()
    print(f'Computation time: {(t2-t1)} sec')

    return in_planes


if __name__ == '__main__':
    DIR_HSPY = 'HSPY_files/'
    DIR_NPY = 'NPY_files/'
    FILE_EXP_L = 'LeftPeaks_xy.npy'
    FILE_EXP_U = 'UnderPeaks_xy.npy'
    FILE_SIM = 'r_theta_sim.npy'

    # Load experimental peaks
    p = np.load(DIR_NPY+FILE_EXP_U, allow_pickle=True)
    # Convert to polar
    p = pxm.signals.DiffractionVectors(p)
    p = p.to_polar()
    # Back to ndarray
    p = p.data
    # Load simulated peaks 
    sim = np.load(DIR_NPY+FILE_SIM, allow_pickle=True)
    
    dist_cutoff = 7e-2 # Subject to change

    
    phis = get_all_phis(p,sim,dist_cutoff)
    plot_in_plane_score(phis)
    
