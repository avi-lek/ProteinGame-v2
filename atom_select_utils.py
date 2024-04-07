import streamlit as st
import urllib
from Bio.PDB import PDBParser
from utils import *
from text_highlighter import text_highlighter

amino_acid_dict = {
    'ALA': 'A',  # Alanine
    'ARG': 'R',  # Arginine
    'ASN': 'N',  # Asparagine
    'ASP': 'D',  # Aspartic Acid
    'CYS': 'C',  # Cysteine
    'GLN': 'Q',  # Glutamine
    'GLU': 'E',  # Glutamic Acid
    'GLY': 'G',  # Glycine
    'HIS': 'H',  # Histidine
    'ILE': 'I',  # Isoleucine
    'LEU': 'L',  # Leucine
    'LYS': 'K',  # Lysine
    'MET': 'M',  # Methionine
    'PHE': 'F',  # Phenylalanine
    'PRO': 'P',  # Proline
    'SER': 'S',  # Serine
    'THR': 'T',  # Threonine
    'TRP': 'W',  # Tryptophan
    'TYR': 'Y',  # Tyrosine
    'VAL': 'V'   # Valine
}
def pdb_to_fasta(pdb_code):
    pdb_url = f'https://files.rcsb.org/download/{pdb_code}.pdb'
    pdb_file = urllib.request.urlopen(pdb_url).read()
    pdb_parser = PDBParser(QUIET=True)
    model = list(pdb_parser.get_structure(id=pdb_code, file=StringIO(pdb_file.decode('utf-8'))).get_models())[0]

    sequ = []
    sequence = ''


    for chain in model:
        for residue in chain:
            if residue.get_resname() in amino_acid_dict.keys():
                sequ.append(amino_acid_dict[residue.get_resname()])
        break
                    
    sequence = " ".join(str(x) for x in sequ)
    sequence = sequence.replace(" ", "")

    return(sequence)
def pdb_to_fasta_esm(pdb_code):    
    pdb_parser = PDBParser(QUIET=True)
    model = list(pdb_parser.get_structure(id=pdb_code, file="pdb\\sandbox.pdb").get_models())[0]
    chains_mask = {}
    sequence = {}
    for chain in model:
        chains_mask[chain.id] = []
        sequence[chain.id] = ''
        for residue in chain:
            if residue.get_resname() in amino_acid_dict.keys():
                chains_mask[chain.id].append(len(list(residue.get_atoms())))
                sequence[chain.id] = sequence[chain.id] + amino_acid_dict[residue.get_resname()]
    return sequence, chains_mask

def pdb_to_fasta_rcsb(pdb_code):    
    pdb_url = f'https://files.rcsb.org/download/{pdb_code}.pdb'
    pdb_file = urllib.request.urlopen(pdb_url).read()
    pdb_parser = PDBParser(QUIET=True)
    model = list(pdb_parser.get_structure(id=pdb_code, file=StringIO(pdb_file.decode('utf-8'))).get_models())[0]
    chains_mask = {}
    sequence = {}
    for chain in model:
        chains_mask[chain.id] = []
        sequence[chain.id] = ''
        for residue in chain:
            if residue.get_resname() in amino_acid_dict.keys():
                chains_mask[chain.id].append(len(list(residue.get_atoms())))
                sequence[chain.id] = sequence[chain.id] + amino_acid_dict[residue.get_resname()]
    return sequence, chains_mask

def select_atoms(system):
    colors = ['#00FFFF', '#FF00FF', '#FFFF00', '#00FF00', '#FFC0CB', '#FFA500', '#0000FF', '#800080', '#FF0000', '#008080']
    if st.session_state["use_esm"]:
        fasta, pdb_dict = pdb_to_fasta_esm(st.session_state["code"][0:5].upper())
    else:
        fasta, pdb_dict = pdb_to_fasta_rcsb(st.session_state["code"][0:5].upper())
    view_key = {}
    n=0

    with st.session_state["viz_settings"].expander("Visualize Subchains"):
        for key in fasta.keys():
            annotations = text_highlighter(text=fasta[key], labels=[("Chain " + key, colors[n])])
            if len(annotations)>0:
                start = annotations[0]['start']
                end = annotations[0]['end']
                view_key[key] = (start,end)
            else:
                start = 0
                end = len(fasta[key])
                view_key[key] = (start,end)
            n=n+1
    new_system = []
    i = 0
    for line in system.split('\n'):
        split = line.split()
        if len(split) == 0 or split[0] != "ATOM":
            continue
        if split[4] in view_key.keys() and int(split[5]) > view_key[split[4]][0] and int(split[5]) <= view_key[split[4]][1]:
            new_system.append(line)

    new_system="\n".join(new_system)
    return new_system

