# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import Tk, filedialog
import numpy as np
import os, qml 

root = Tk()
root.withdraw()
inp_dir = filedialog.askopenfilename(title = 'Input directory')
#os.chdir(inp_dir)

root.destroy()

mol = qml.Compound(xyz=inp_dir)

#%%

atoms = len (mol.coordinates)

mol.generate_atomic_coulomb_matrix(size=atoms)

print ('Coulomb Matrix :',  mol.representation.shape)

#%%
from qml.representations import get_slatm_mbtypes

mbtypes = get_slatm_mbtypes([mol.nuclear_charges])

mol.generate_slatm(mbtypes, local= True)

print ('SLATM Matrix :',  mol.representation.shape)

#%%

mol.generate_fchl_representation(max_size= atoms,cut_distance=10.0 )

print ('FCHL Matrix :',  mol.representation.shape)

new = mol.representation.reshape((atoms,-1))

print (new.shape)