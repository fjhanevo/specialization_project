import hyperspy.api as hs
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sps

def get_trace(dp,i,x1,y1,x2,y2) -> None:

    img = dp.inav[i]

    img.plot(cmap='magma', norm='log')
    
    # Draw a line between DPs
    line = hs.roi.Line2DROI(x1=x1, y1=y1, x2=x2, y2=y2,linewidth=5)
    line.add_widget(img)
    plt.show()
    print(line)

    # Trace img to find peak positions
    trace=line(img).as_signal1D(0)
    trace.plot(norm='log')
    trace=np.log(trace)
    plt.show()

    # Find peaks
    print(sps.find_peaks(trace.data))

def get_diffraction_calibration(peaks, g_dist):
    return g_dist/peaks

def set_calibration(dp, diffraction_calibration,save=False, name=None) -> None:
    dp.set_diffraction_calibration(diffraction_calibration)
    dp.plot(cmap='magma')
    if save and name is not None:
        dp.save(name)
    plt.show()

if __name__ == "__main__":
    # Load dataset
    dp = hs.load('UnderFish/SPED_FCC_Al_60_tilts.hspy')
    # Al lattice parameter
    a=4.0495
    # dp = hs.load('UnderFish_calibrated.hspy')

    #### Image 10 ####
    # i = 10
    # x1, y1, x2, y2 = 123, 18, 27,165 
    # get_trace(dp,i,x1,y1,x2,y2)
    # dist_200_peaks = (162-10)/2
    # g_dist_001_axis = np.sqrt(2)/a
    # diffraction_calibration = get_diffraction_calibration(dist_200_peaks, g_dist_001_axis)
    # print(diffraction_calibration)

    #### Image 37 ####
    # This was the best match
    i = 37
    x1, y1, x2, y2 = 190, 27, 65, 230
    get_trace(dp,i,x1,y1,x2,y2)
    dist_111_peaks = (158-79)/2
    g_dist_112_axis = (np.sqrt(8)/np.sqrt(3))/a
    diffraction_calibration = get_diffraction_calibration(dist_111_peaks,g_dist_112_axis)
    print(diffraction_calibration)
    
    set_calibration(dp, diffraction_calibration,True,'UnderFish_calibrated.hspy')
    #### Image 40 ####
    # i = 40
    # x1, y1, x2, y2 = 196, 17, 61, 238
    # get_trace(dp, i, x1,y1,x2,y2)
    # dist_111_peaks2 = (170-89)/2
    # diffraction_calibration = get_diffraction_calibration(dist_111_peaks2, g_dist_112_axis)
    # print(diffraction_calibration)


