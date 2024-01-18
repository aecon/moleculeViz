import numpy as np

class Grid():
    def __init__(self, px, py, pz, Nx, Ny, Nz):
        """
            (px, py, pz): pixel size in um
            (Nx, Ny, Nz): number of pixels per direction
        """
        self.px = px
        self.py = py
        self.pz = pz
        self.shape = np.asarray([Nx, Ny, Nz])

