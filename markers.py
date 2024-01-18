import os
import sys
import numpy as np
import pandas as pd
import skimage.io

from grid import Grid



class Markers:


    def __init__(self, grid):
        self.x  = []
        self.y  = []
        self.z  = []
        self.xu = []
        self.yu = []
        self.zu = []
        self.grid = grid


    def load_coordinates(self, fm):
        datafile = pd.read_csv(fm)
        self.x = np.asarray(datafile['x [nm]'])
        self.y = np.asarray(datafile['y [nm]'])
        self.z = np.asarray(datafile['z [nm]'])


    def duplicate_marker_exclusion(self, Distance):
        """
            Find unique marker coordinates, up to a threshold (Distance)
        """
        zmin = abs(np.min(self.z))
        zres = Distance
        xt = np.floor(self.x / zres)
        yt = np.floor(self.y / zres)
        zt = np.floor((self.z+zmin)/zres)
        M = (np.vstack([xt,yt,zt])).T
        unique_M, indices = np.unique(M, axis=0, return_index=True)

        # keep unique markers
        self.xu = self.x[indices]
        self.yu = self.y[indices]
        self.zu = self.z[indices]

        percentage_removed = (len(M)-len(unique_M)) / len(M) * 100.
        return percentage_removed


    def bin_marker_to_grid(self, odir, marker_file):

        shape = self.grid.shape
        spacings = (self.grid.px, self.grid.py, self.grid.pz)
        limits = (shape[0]*self.grid.px*1.e3, shape[1]*self.grid.py*1.e3, shape[2]*self.grid.pz*1.e3)
        minz = self.grid.pz * shape[2] * 0.5
        sample = (np.vstack([self.xu, self.yu, self.zu+minz])).T

        H, edges = np.histogramdd(sample, range=( (0,limits[0]), (0,limits[1]), (0,limits[2]) ), bins=shape )

        return H

