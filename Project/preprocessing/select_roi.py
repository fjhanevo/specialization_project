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
DIR_ROIS = 'ROI_LeftFish/'
# DIR_ROIS = 'ROI_UnderFish/'

# Save .hspy files
# DIR_HSPY = 'SPED_tilt_hspy/'
DIR_HSPY = 'LeftFish/'
# DIR_HSPY = 'UnderFish/'

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
    roi0 = hs.roi.RectangularROI(left=23, top=18, right=29, bottom=23)
    roi0.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi0)

    i = 1
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi1 = hs.roi.RectangularROI(left=22, top=10, right=28, bottom=15)
    roi1.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi1)

    i = 2
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi2 = hs.roi.RectangularROI(left=23, top=3, right=29, bottom=8)
    roi2.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi2)

    i = 3
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi3 = hs.roi.RectangularROI(left=26, top=1, right=32, bottom=6)
    roi3.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi3)

    i = 4
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi4 = hs.roi.RectangularROI(left=4, top=25, right=10, bottom=30)
    roi4.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi4)

    i = 5
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi5 = hs.roi.RectangularROI(left=18, top=29, right=24, bottom=34)
    roi5.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi5)

    i = 6
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi6 = hs.roi.RectangularROI(left=18, top=23, right=24, bottom=28)
    roi6.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi6)

    i = 7
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi7 = hs.roi.RectangularROI(left=14, top=15, right=20, bottom=20)
    roi7.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi7)

    i = 8
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi8 = hs.roi.RectangularROI(left=13, top=11, right=19, bottom=16)
    roi8.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi8)

    i = 9
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi9 = hs.roi.RectangularROI(left=10, top=3, right=16, bottom=8)
    roi9.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi9)

    i = 10
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi10 = hs.roi.RectangularROI(left=18, top=29, right=24, bottom=34)
    roi10.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi10)

    i = 11
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi11 = hs.roi.RectangularROI(left=20, top=19, right=26, bottom=24)
    roi11.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi11)

    i = 12
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi12 = hs.roi.RectangularROI(left=16, top=8, right=22, bottom=13)
    roi12.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi12)

    i = 13
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi13 = hs.roi.RectangularROI(left=14, top=13, right=20, bottom=18)
    roi13.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi13)

    i = 14 
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi14 = hs.roi.RectangularROI(left=13, top=10, right=19, bottom=15)
    roi14.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi14)

    i = 15
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi15 = hs.roi.RectangularROI(left=9, top=2, right=15, bottom=7)
    roi15.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi15)

    i = 16
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi16 = hs.roi.RectangularROI(left=4, top=1, right=10, bottom=6)
    roi16.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi16)

    i = 17
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi17 = hs.roi.RectangularROI(left=9, top=21, right=15, bottom=26)
    roi17.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi17)

    i = 18
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi18 = hs.roi.RectangularROI(left=11, top=21, right=17, bottom=26)
    roi18.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi18)

    i =19 
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi19= hs.roi.RectangularROI(left=9, top=20, right=15, bottom=25)
    roi19.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi19)


    i = 20
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi20 = hs.roi.RectangularROI(left=11, top=16, right=17, bottom=21)
    roi20.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi20)

    i = 21
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi21 = hs.roi.RectangularROI(left=13, top=11, right=19, bottom=16)
    roi21.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi21)

    i = 22
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi22 = hs.roi.RectangularROI(left=15, top=23, right=21, bottom=28)
    roi22.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi22)

    i = 23
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi23 = hs.roi.RectangularROI(left=16, top=21, right=22, bottom=26)
    roi23.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi23)

    i = 24
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi24 = hs.roi.RectangularROI(left=16, top=19, right=22, bottom=24)
    roi24.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi24)

    i = 25
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi25 = hs.roi.RectangularROI(left=11, top=14, right=17, bottom=19)
    roi25.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi25)

    i = 26
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi26 = hs.roi.RectangularROI(left=15, top=11, right=21, bottom=16)
    roi26.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi26)

    i = 27
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi27 = hs.roi.RectangularROI(left=10, top=9, right=16, bottom=14)
    roi27.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi27)

    i = 28 
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi28 = hs.roi.RectangularROI(left=5, top=25, right=11, bottom=30)
    roi28.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi28)

    i = 29
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi29 = hs.roi.RectangularROI(left=7, top=24, right=13, bottom=29)
    roi29.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi29)

    i = 30
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi30 = hs.roi.RectangularROI(left=10, top=16, right=16, bottom=21)
    roi30.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi30)

    i = 31
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi31 = hs.roi.RectangularROI(left=6, top=12, right=12, bottom=17)
    roi31.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi31)

    i = 32
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi32 = hs.roi.RectangularROI(left=17, top=14, right=23, bottom=19)
    roi32.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi32)

    i = 33
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi33 = hs.roi.RectangularROI(left=16, top=13, right=22, bottom=18)
    roi33.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi33)

    i = 34
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi34 = hs.roi.RectangularROI(left=17, top=8, right=23, bottom=13)
    roi34.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi34)

    i = 35
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi35 = hs.roi.RectangularROI(left=18, top=5, right=24, bottom=10)
    roi35.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi35)

    i = 36
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi36 = hs.roi.RectangularROI(left=8, top=16, right=14, bottom=21)
    roi36.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi36)

    i = 37
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi37 = hs.roi.RectangularROI(left=9, top=14, right=15, bottom=19)
    roi37.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi37)

    i = 38
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi38 = hs.roi.RectangularROI(left=6, top=16, right=12, bottom=21)
    roi38.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi38)

    i = 39
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi39 = hs.roi.RectangularROI(left=5, top=18, right=11, bottom=23)
    roi39.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi39)

    i = 40
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi40 = hs.roi.RectangularROI(left=2, top=2, right=8, bottom=7)
    roi40.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi40)

    i = 41
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi41 = hs.roi.RectangularROI(left=3, top=30, right=9, bottom=35)
    roi41.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi41)

    i = 42
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi42 = hs.roi.RectangularROI(left=6, top=29, right=12, bottom=34)
    roi42.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi42)

    i = 43
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi43 = hs.roi.RectangularROI(left=8, top=25, right=14, bottom=30)
    roi43.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi43)

    i = 44
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi44 = hs.roi.RectangularROI(left=5, top=20, right=11, bottom=25)
    roi44.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi44)

    i = 45
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi45 = hs.roi.RectangularROI(left=3, top=11, right=9, bottom=16)
    roi45.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi45)

    i = 46
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi46 = hs.roi.RectangularROI(left=3, top=35, right=9, bottom=40)
    roi46.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi46)

    i = 47
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi47 = hs.roi.RectangularROI(left=2, top=32, right=8, bottom=37)
    roi47.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi47)

    i = 48
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi48 = hs.roi.RectangularROI(left=1, top=32, right=7, bottom=37)
    roi48.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi48)

    i = 49
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi49 = hs.roi.RectangularROI(left=4, top=31, right=10, bottom=36)
    roi49.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi49)

    i = 50
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi50 = hs.roi.RectangularROI(left=6, top=35, right=12, bottom=40)
    roi50.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi50)

    i = 51
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi51 = hs.roi.RectangularROI(left=6, top=33, right=12, bottom=38)
    roi51.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi51)

    i = 52
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi52 = hs.roi.RectangularROI(left=3, top=31, right=9, bottom=36)
    roi52.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi52)

    i = 53
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi53 = hs.roi.RectangularROI(left=3, top=28, right=9, bottom=33)
    roi53.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi53)

    i = 54
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi54 = hs.roi.RectangularROI(left=1, top=6, right=7, bottom=21)
    roi54.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi54)

    i = 55
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi55 = hs.roi.RectangularROI(left=8, top=36, right=14, bottom=41)
    roi55.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi55)

    i = 56 
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi56 = hs.roi.RectangularROI(left=12, top=36, right=18, bottom=41)
    roi56.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi56)

    i = 57
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi57 = hs.roi.RectangularROI(left=5, top=33, right=11, bottom=38)
    roi57.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi57)

    i = 58
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi58 = hs.roi.RectangularROI(left=6, top=28, right=12, bottom=33)
    roi58.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi58)

    i = 59
    vbfs_series_i = vbfs_series_s.inav[i]
    vbfs_series_i.plot(cmap='viridis_r', title=str(i), interpolation='none', axes_ticks='off',
                       scalebar=False, colorbar=False)
    roi59 = hs.roi.RectangularROI(left=11, top=24, right=17, bottom=29)
    roi59.add_widget(vbfs_series_i)
    plt.show()
    plt.savefig(DIR_ROIS+file_names[i]+'_roi.png')
    print(roi59)
    plt.close('all')

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
    tilt_series_av_s.save(DIR_HSPY+'LeftFish_interpolate_hsw30_subpixelTrue_sigma1_5_uf2_nearest_inplaceFalse.hspy')
    
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
    with open('ROI_UnderFish_json/LeftFish_roi_list_interpolate_s_shifts_hsw30_inplaceFalse_etc.json', 'w') as f:
        json.dump(roi_data, f, indent=4)

    # Debug statement
    print("Done!")
