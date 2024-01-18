import os
import sys
import glob
import time
import numba
import pickle
import skimage.io
import numpy as np
import pandas as pd
from tifffile import imsave

import img3

from data    import Data
from grid    import Grid
from markers import Markers


# File with marker coordinates
file_marker_coordinates = "data.csv"

# Pixel sizes in nano-meters (nm)
px=100
py=100
pz=100

# Image dimensions
Nx=500
Ny=500
Nz=50

# Instantiate grid
grid = Grid(px, py, pz, Nx, Ny, Nz)

# Instantiate markers
markers = Markers(grid)

# Read marker coordinates
marker.load_coordinates(file_marker_coordinates)

# Remove markers closer than Distance
Distance = px
percentage_removed = marker.duplicate_marker_exclusion(Distance)

# 3D Image reconstruction
img = marker.bin_marker_to_grid("out", file_marker_coordinates)

# Export to tif image stack
skimage.io.imsave("markers.tif", img.T, plugin="tifffile", check_contrast=False)

