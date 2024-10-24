import os
import gc
import time
import json
import hyperspy.api as hs
import matplotlib.pyplot as plt
import pyxem as pxm
import numpy as np

# Loading the files
DIR_TILTS = 'SPED_tilt/'

# Save ROIs to folder
# DIR_ROIS = 'SPED_tilt_series_ROIs/'
# DIR_ROIS = 'ROI_LeftFish/'
DIR_ROIS = 'ROI_UnderFish/'

# Save .hspy files
# DIR_HSPY = 'SPED_tilt_hspy/'
# DIR_HSPY = 'LeftFish/'
DIR_HSPY = 'UnderFish/'

vbfs_series = []
file_names = []


# Change these depending on file names and types
PREFIX = '20230426_'
EXTENSION = '.png'

def load_files() -> None:
    for root, _, files in os.walk(DIR_TILTS):
        # Combine filtering and sorting in one step
        filtered_files = [file for file in files if file.startswith(PREFIX) 
            and file.endswith(EXTENSION)]
        # Sort the files
        filtered_files.sort(key=lambda f: f.split(".")[0])

        # Loop over the sorted files
        for file in filtered_files:
            try:
                # Print for debug
                print("used: ",file)

                # Construct filepath
                file_path = os.path.join(root, file)

                # Load files
                vbfs_data = hs.load(file_path)

                # Append to list
                vbfs_series.append(vbfs_data.data)

                # Get filename without extension
                file_name, _ = os.path.splitext(file)

                # Append to list
                file_names.append(file_name)
            except Exception as e:
                print(f"Error loading file {file}: {e}")

if __name__ == '__main__':
    load_files()
    
    vbfs_series_s = hs.signals.Signal2D(vbfs_series)
    # Update left, top, right, bottom for faster processing

    i = 0
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi0 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi0.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 1
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi1 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi1.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 2
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi2 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi2.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 3
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi3 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi3.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 4
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi4 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi4.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 5
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi5 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi5.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 6
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi6 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi6.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 7
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi7 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi7.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 8
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi8 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi8.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 9
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi9 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi9.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 10
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi10 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi10.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 11
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi11 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi11.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 12
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi12 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi12.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 13
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi13 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi13.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 14
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi14 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi14.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 15
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi15 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi15.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 16
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi16 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi16.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 17
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi17 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi17.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 18
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi18 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi18.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 19
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi19 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi19.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')


    i = 20
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi20 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi20.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 21
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi21 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi21.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 22
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi22 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi22.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 23
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi23 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi23.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 24
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi24 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi24.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 25
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi25 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi25.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 26
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi26 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi26.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 27
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi27 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi27.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 28 
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi28 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi28.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 29
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi29 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi29.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 30
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi30 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi30.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 31
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi31 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi31.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 32
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi32 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi32.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 33
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi33 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi33.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 34
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi34 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi34.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 35
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi35 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi35.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 36
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi36 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi36.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 37
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi37 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi37.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 38
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi38 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi38.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 39
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi39 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi39.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 40
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi40 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi40.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 41
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi41 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi41.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 42
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi42 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi42.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 43
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi43 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi43.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 44
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi44 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi44.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 45
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi45 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi45.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 46
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi46 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi46.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 47
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi47 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi47.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 48
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi48 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi48.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 49
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi49 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi49.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 50
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi50 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi50.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 51
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi51 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi51.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 52
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi52 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi52.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 53
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi53 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi53.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 54
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi54 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi54.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 55
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi55 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi55.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 56 
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi56 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi56.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 57
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi57 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi57.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 58
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi58 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi58.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    i = 59
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi59 = hs.roi.RectangularROI(left=4, top=14, right=10, bottom=19)
    roi59.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')

    # Debug statement
    print("All files handled")
    roi_list = [roi0, roi1, roi2, roi3, roi4, roi5, roi6, roi7, roi8, roi9,
        roi10, roi11, roi12, roi13, roi14, roi15, roi16, roi17, roi18, roi19,
        roi20, roi21, roi22, roi23, roi24, roi25, roi26, roi27, roi28, roi29,
        roi30, roi31, roi32, roi33, roi34, roi35, roi36, roi37, roi38, roi39,
        roi40, roi41, roi42, roi43, roi44, roi45, roi46, roi47, roi48, roi49,
        roi50, roi51, roi52, roi53, roi54, roi55, roi56, roi57, roi58, roi59,
        ]


    # Parameters for mask to improve centering (processed in other file)
    r,cx,cy = 7.5,122,125
    tilt_series_av = []
    # s_shifts=None
    t1 = time.time()
    for n, file in zip(range(len(file_names)), file_names):
        print('no.',n, 'file:', file,)
        roi = roi_list[n]
        tilt_data = hs.load(DIR_TILTS+file+'.hspy')
        # if n == 0:
        #     s_shifts = tilt_data.get_direct_beam_position(
        #         method="interpolate", 
        #         half_square_width=30,
        #         sigma=1.5, 
        #         upsample_factor=2, 
        #         kind="nearest"
        #         )

        # tilt_data.center_direct_beam(method="center_of_mass", mask=(cx,cy,r),threshold=750, inplace=False)
        tilt_data.center_direct_beam(
                method="interpolate", 
                half_square_width=30,
                sigma=1.5, 
                upsample_factor=2, 
                kind="nearest",
                inplace=False,
                )

        # tilt_data.center_direct_beam(shifts=s_shifts)
        tilt_roi_av = np.average(roi(tilt_data).data,axis=(0,1))
        tilt_series_av.append(tilt_roi_av)
        # Free memory
        del tilt_data
        gc.collect()
    t2 = time.time()
    print(f'Computation time {(t2-t1)/60} min')

    tilt_series_av_s = pxm.signals.ElectronDiffraction2D(tilt_series_av)
    tilt_series_av_s.plot(cmap='magma_r', norm='log')
    tilt_series_av_s.save(DIR_HSPY+'UnderFish_interpolate_hsw30_subpixelTrue_sigma1_5_uf2_nearest_inplaceFalse.hspy')
    
    # Save roi data to a dir. to keep track
    roi_data=[]
    for roi in roi_list:
        roi_data.append({
            'left': roi.left,
            'top': roi.top,
            'right': roi.right,
            'bottom': roi.bottom,
        })
    
    # Save roi to jéson file
    with open('ROI_UnderFish_json/roi_list_interpolate_s_shifts_hsw30_inplaceFalse_etc.json', 'w') as f:
        json.dump(roi_data, f, indent=4)

    # Debug statement
    print("Done!")
