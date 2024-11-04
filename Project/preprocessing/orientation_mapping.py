import hyperspy.api as hs
import pyxem as pxm
import numpy as np
import matplotlib.pyplot as plt
import orix
from diffpy.structure import Atom, Lattice, Structure
from diffsims.generators.simulation_generator import SimulationGenerator


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

def get_simulation_generator(precession_angle=1.0, minimum_intensity=1e-5):
# Define a simulation generator that takes the precession angle (1 degree)
    return SimulationGenerator(precession_angle=precession_angle,
                               minimum_intensity=minimum_intensity)

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
    pol = s.get_azimuthal_integral2d(npt=npt)
    pol.plot()
    plt.show()
    return pol

def polar_match(pol, simulations, grid_size, frac_keep=1.0):
    return pol.get_orientation(simulations, n_best=grid_size, frac_keep=1.0)

def plot_results(pol, results, s):
    pol.plot()
    pol.add_marker(results.to_single_phase_polar_markers(
        signal_axes=pol.axes_manager.signal_axes))

    s.plot(cmap='magma_r', norm='log')
    s.add_marker(results.to_markers(annotate=True))
    plt.show()

def run_prev_stuff(s) -> None:
    phase = unit_cell() 
    
    grid, orientation = gen_orientation_grid(phase)

    simgen = get_simulation_generator()

    simulations = compute_simulations(simgen, phase, grid)

    pol = azimuthal_integration(s)

    results = polar_match(pol, simulations, grid.size)

    plot_results(pol, results,s)

def apply_mask(s,min_dist, threshold, filename=None) -> None:

    st = s.template_match_disk(disk_r=2.2, subtract_min=False)

    # hs.plot.plot_signals([s,st])

    i,j = 1,50 
    s_i = s.inav[i:i+j]
    st_i = st.inav[i:i+j]

    st_i_peaks = st_i.get_diffraction_vectors(min_distance=min_dist, threshold_abs=threshold)

    m = st_i_peaks.to_markers(sizes=3, color='cyan')
    s_i.plot(cmap='magma',norm='log')
    s_i.add_marker(m)
    plt.show()

    # Test masking!
    vectors = st.get_diffraction_vectors(min_distance=min_dist, threshold_abs=threshold)
    vectors_masks = vectors.to_mask(disk_r = 4)
    s_masked = s*vectors_masks
    hs.plot.plot_signals([s,s_masked], norm='log', cmap='magma')
    if filename is not None:
        s_masked.save(filename)
    plt.show()


if __name__ == "__main__":
    file = 'UnderFish_strict_mask.hspy'
    s = hs.load(file)
    apply_mask(s, 8, 0.785)

    # s.set_diffraction_calibration(0.0107)
    ### Orientation simulations ####
    # s_pol = s.get_azimuthal_integral2d(npt=112)
    # s_pol.plot()

    # phase = unit_cell()
    # grid, orientation = gen_orientation_grid(phase)
    # simgen = get_simulation_generator()
    # simulation_zone_axes = compute_simulations(simgen, phase, grid, reciprocal_radius=1.8, 
    #                                  max_excitation_error=0.008)
    #
    # s_results= s_pol.get_orientation(simulation_zone_axes, n_best =1, frac_keep=0.5)
    # s_pol.plot()
    # s_pol.add_marker(s_results.to_single_phase_polar_markers(signal_axes=s_pol.axes_manager.signal_axes))
    # plt.show()
    #
