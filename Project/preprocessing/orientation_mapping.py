import hyperspy.api as hs
import pyxem as pxm
import numpy as np
import matplotlib.pyplot as plt
import orix
from orix.plot import IPFColorKeyTSL
from orix.vector import Vector3d
from diffpy.structure import Atom, Lattice, Structure
from diffsims.generators.simulation_generator import SimulationGenerator
from numpy import log10

# Fiks denne til å bare ta akser og scalebar
# plt.rcParams.update({'font.size':18})
plt.rcParams.update({'font.size':18})
def unit_cell(a=4.0495):
    atoms = [Atom('Al', [0,0,0]), Atom('Al', [0.5,0.5,0]),
             Atom('Al', [0.5, 0, 0.5]), Atom('Al', [0,0.5,0.5])]

    lattice = Lattice(a,a,a,90,90,90)
    phase = orix.crystal_map.Phase(name='Al', space_group=225, structure=Structure(atoms, lattice))
    return phase

def gen_orientation_grid(phase, angular_resolution=0.5):
    grid = orix.sampling.get_sample_reduced_fundamental(
        angular_resolution,
        point_group=phase.point_group,
    )

    orientations = orix.quaternion.Orientation(grid, symmetry=phase.point_group)
    orientations.scatter('ipf')
    
    return grid, orientations

def get_simulation_generator(precession_angle=1.0, 
                             minimum_intensity=1e-5,
                             approximate_precession=False):

    return SimulationGenerator(precession_angle=precession_angle,
                               minimum_intensity=minimum_intensity,
                               approximate_precession=approximate_precession)

def compute_simulations(simgen,phase,grid,reciprocal_radius=1.5, 
                        max_excitation_error=0.01,with_direct_bream=False):
    return simgen.calculate_diffraction2d(
        phase=phase,                                 # phase to simulate for
        rotation=grid,                               # orientations to simulate for
        reciprocal_radius=reciprocal_radius,         # max radius to consider in [Å^-1]
        with_direct_beam=with_direct_bream,         # option to include direct beam
        max_excitation_error=max_excitation_error,   # max excitation error, s
    )

def azimuthal_integration(s, npt=112):
    pol = s.get_azimuthal_integral2d(npt=npt, radial_range=1.35)
    return pol

def polar_match(pol, simulations, grid_size, frac_keep=1.0):
    return pol.get_orientation(simulations, n_best=grid_size, frac_keep=1.0)

def apply_mask(s,min_dist=20, threshold=0.2, filename=None,save=False) -> None:

    st = s.template_match_disk(disk_r=2.2, subtract_min=False)

    # hs.plot.plot_signals([s,st])

    # Check for a range of dimensions
    i,j = 1,59
    # i,j = 50,59
    s_i = s.inav[i:i+j]
    st_i = st.inav[i:i+j]

    st_i_peaks = st_i.get_diffraction_vectors(min_distance=min_dist, threshold_abs=threshold)

    # m = st_i_peaks.to_markers(sizes=3, color='cyan')
    m = st_i_peaks.to_markers(sizes=5, color='red')
    # s_i.plot(cmap='magma',norm='log',title='',colorbar=False)
    s_i.plot(cmap='viridis_r',norm='log',title='',colorbar=False,
             scalebar=True,scalebar_color='black', axes_ticks='off')
    s_i.add_marker(m)
    plt.show()

    # Apply mask
    vectors = st.get_diffraction_vectors(min_distance=min_dist, threshold_abs=threshold, get_intensity=False)
    print(type(vectors))
    if save:
        # np.save(file='LeftPeaks_xy.npy', arr=vectors.data, allow_pickle=True)
        np.save(file='UnderPeaks_xy.npy', arr=vectors.data, allow_pickle=True)
    vectors_masks = vectors.to_mask(disk_r = 4)
    s_masked = s*vectors_masks
    # hs.plot.plot_signals([s,s_masked], norm='log', cmap='magma',title='',colorbar=False)
    # For workflow_fig
    hs.plot.plot_signals([s,s_masked],norm='log',cmap='viridis_r',colorbar=False,scalebar=False,axes_ticks='off')
    if filename is not None:
        s_masked.save(filename)
    plt.show()


def log_shift(raw,base=10,shift=0.1):
    log_shift = log10(raw+shift) - log10(shift)
    return log_shift

def plot_found_orientation(results,lst):
    loris = results.to_single_phase_orientations()
    loris_best = loris[:,0]
    print(type(loris_best))
    loris_ang = loris_best.angle_with_outer(loris_best,degrees=True)

    # Scatter plot
    colors = ['red', 'purple', 'blue']
    c = 0
    plt.figure(figsize=(8,6))
    # plt.scatter(range(len(loris_ang[:,0])), loris_ang[:,0])
    for i in range(len(loris_ang)-1):
        if i in lst:
            plt.scatter(i, loris_ang[i,i+1],marker='o',s=54*4,c=colors[c], label='Frame: '+str(i))
            c +=1
        else:
            plt.scatter(i, loris_ang[i,i+1], s=34,c='black')

    # Add a hline to indicate 1 deg
    plt.axhline(y=1, color='red',label=r'1$\degree$',linestyle='dashed')
    plt.grid(True)
    plt.ylabel(r'Misorientation$\degree$',fontsize='26')
    plt.xlabel('Tilt Step',fontsize='26')
    plt.xticks(fontsize='18')
    plt.yticks(fontsize='18')
    plt.legend(fontsize='18', loc='center left')
    plt.tight_layout()
    plt.show()

def get_reciprocal_radius(s):
    circ = hs.roi.CircleROI(cx=0,cy=0,r=1.35355)
    s.plot(norm='log')
    circ.add_widget(s)
    plt.show()
    print(circ)

def plot_data_set_with_markers(s,s_results, lst):
    i,j = lst[0],lst[-1]
    s = s.inav[i:j]
    s_results=s_results.inav[i:j]
    s.plot(cmap='viridis_r', norm='log',title='', colorbar=False, scalebar_color='black',axes_ticks='off')
    s.add_marker(s_results.to_markers(annotate=True))
    plt.show()

def get_simulation_polar(sim,filename):
    # Get simulations
    r,theta,_ = sim.polar_flatten_simulations()
    # Combine to a (M,N,2) ndarray
    rt = np.stack([r,theta],axis=-1)
    # Save coords
    np.save(file=filename, arr=rt, allow_pickle=True)
    print(rt[0])
    print(rt.shape)
    print(rt[0].shape)



if __name__ == "__main__":
    FILE = 'UnderFish_masked_log_calibrated.hspy'
    # FILE = 'UnderFish_calibrated.hspy'
    # FILE = 'LeftFish_masked_log_calibrated.hspy'
    # FILE = 'LeftFish_unmasked.hspy'
    # FILE = 'UnderFish_unmasked.hspy'
    # Load file
    s = hs.load(FILE)

    ### Orientation simulations ####

    s_pol = s.get_azimuthal_integral2d(npt=112)
    phase = unit_cell()
    grid, orientation = gen_orientation_grid(phase)

    simgen = get_simulation_generator(precession_angle=1., minimum_intensity=1e-4,approximate_precession=True)
    simulations = compute_simulations(simgen, phase, grid, reciprocal_radius=1.35, 
                                     max_excitation_error=0.05)
    s_results= s_pol.get_orientation(simulations, n_best =1, frac_keep=1.)
    get_simulation_polar(simulations,'UnderPeaks_sim.npy')

    # s_results= s_pol.get_orientation(simulations, n_best =grid.size, frac_keep=1.)    # for NCC score
    # s_pol.add_marker(s_results.to_single_phase_polar_markers(signal_axes=s_pol.axes_manager.signal_axes))
    # lst = [29,48,56]    # LeftFish
    # lst = [8,21,37]     # UnderFish
    # lst = [4,25,34]     # UnderFish prøv denne istedet!
    # plot_found_orientation(s_results,lst)
    # plt.show()

    # s = hs.load('UnderFish_unmasked.hspy')
    # lst1 = [3,5]
    # lst2 = [23,26]
    # lst3 = [33,35]
    # plot_data_set_with_markers(s,s_results,lst1)
    # plot_data_set_with_markers(s,s_results,lst2)
    # plot_data_set_with_markers(s,s_results,lst3)
    # Only plot selected areas
    # Plot on original dataset
    # s = hs.load('LeftFish_unmasked.hspy')
    s = hs.load('UnderFish_unmasked.hspy')
    i,j =29,31
    s = s.inav[i:j]
    s_results=s_results.inav[i:j]
    s.plot(cmap='viridis_r', norm='log',title='', colorbar=True, scalebar_color='black',axes_ticks='off')
    s.add_marker(s_results.to_markers(annotate=True))
    plt.show()
    # s.add_marker(s_results.to_ipf_markers())
    # i =  34
    # fig = plt.figure()
    # ax=fig.add_subplot(111, projection='ipf', symmetry=phase.point_group)
    # correlations_i = s_results.inav[i].data[:,1]
    # tm_indices_i = (s_results.inav[i].data[:,0]).astype('int16')
    # orientations_i = orientation[tm_indices_i]
    # euler_angles_i = orientations_i.to_euler()
    # loris= s_results.to_single_phase_orientations()
    # loris_best = loris[i,0]
    # ax.scatter(orientations_i ,c=correlations_i, cmap='viridis')
    # ax.scatter(loris_best, c='blue', marker='o', s=100)
    # plt.show()
    # print(loris_best)
