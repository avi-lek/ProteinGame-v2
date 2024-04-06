import numpy as np
import streamlit as st
import requests
import urllib
import py3Dmol
from stmol import showmol
from utils import *
import os
import Bio
from Bio.PDB.PDBIO import PDBIO
from puzzles.puzzle_help import pdb_to_fasta
from Bio.PDB import PDBIO
from Bio.PDB.Atom import Atom

from Bio.PDB import *
from Bio.Seq import Seq

from Bio.PDB import PDBIO, Structure, Model, Chain, Atom
import numpy as np
import numpy as np

import math
# Function to generate PDB file
def generate_pdb(filename, sequence_length):
    helix_radius = 10.0  # Radius of the helix
    helix_rise_per_basepair = 3.4  # Distance between consecutive base pairs along the helix axis
    atom_counter = 1  # Counter for atom serial numbers
    residue_counter = 1  # Counter for residue numbers

    with open(filename, 'w') as pdb_file:
        # Header information
        pdb_file.write("HEADER    Double Helix DNA\n")
        
        # Generate coordinates for each base pair
        for i in range(sequence_length):
            # Calculate angle for each base pair
            angle = 2 * math.pi * (i / 10.0)
            
            # Calculate coordinates for strand 1
            z1 = helix_radius * math.cos(angle)
            y1 = helix_radius * math.sin(angle)
            x1 = i * helix_rise_per_basepair
            # Write atom lines for strand 1
            pdb_file.write(f"ATOM  {atom_counter:5}  P   DA A{residue_counter:4}    {x1:8.3f}{y1:8.3f}{z1:8.3f}  1.00  0.00           P\n")
            pdb_file.write(f"ATOM  {atom_counter+1:5}  S   DA A{residue_counter:4}    {x1-0.5:8.3f}{y1-0.5:8.3f}{z1-0.5:8.3f}  1.00  0.00           S\n")
            atom_counter += 2

            # Calculate coordinates for strand 2 (opposite strand)
            z2 = helix_radius * math.cos(angle + math.pi)
            y2 = helix_radius * math.sin(angle + math.pi)
            x2 = i * helix_rise_per_basepair
            # Write atom lines for strand 2
            #pdb_file.write(f"ATOM  {atom_counter:5}  P   DT B{(residue_counter+1):4}    {x2:8.3f}{y2:8.3f}{z2:8.3f}  1.00  0.00           P\n")
            #pdb_file.write(f"ATOM  {atom_counter+1:5}  S   DT B{(residue_counter+1):4}    {x2-0.5:8.3f}{y2-0.5:8.3f}{z2-0.5:8.3f}  1.00  0.00           S\n")
            atom_counter += 2

            residue_counter += 2

        # Write termination information
        pdb_file.write("TER\n")
        pdb_file.write("END\n")

def create_conect_line(atom_serial_numbers):
    conect_line = "CONECT"
    for serial_number in atom_serial_numbers:
        conect_line += f" {serial_number}"
    return conect_line



# Define DNA sequence length
sequence_length = 60

# Generate PDB file
generate_pdb("pdb//dna//rna.pdb", sequence_length)
'''with open("pdb//dna//dna.pdb") as ifile:
    system = "".join([x for x in ifile])



view = py3Dmol.view(width=600, height=800)
view.addModelsAsFrames(system)
color= ["red", "blue", "green", "yellow"]
i=0

for line in system.split('\n'):
    split = line.split()

    if len(split) == 0 or split[0] != "ATOM":
        continue
    view.setStyle({'model': -1, 'serial': i+1}, {"sphere": {'color': color[i%4]}})
    i += 1

view.zoomTo()

showmol(view, height=600, width=800)
st.write("working")'''