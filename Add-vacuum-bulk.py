# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:27:57 2023

@author: zyj
"""

from ase import Atom
from ase.io import read, write
from ase.geometry import cell_to_cellpar

poscar = read('POSCAR')
new_atoms = []
for atom in poscar:
    if atom.position[2] == 0:
        new_atom = Atom(atom.symbol, (atom.position[0], atom.position[1], poscar.cell[2][2]))
        poscar.append(new_atom)
        
new_c_length = 20.0  # Vacuum length

shift = new_c_length/2 - poscar.cell[2][2]/2
cellpar = cell_to_cellpar(poscar.cell)
cellpar[2] = new_c_length
poscar.set_cell(cellpar)
for atom in poscar:
    atom.position[2] = atom.position[2] + shift
    
write('vacuum_POSCAR', poscar, format='vasp')

