import streamlit as st
import urllib
from Bio.PDB import PDBParser
from utils import *
from text_highlighter import text_highlighter

annotations = text_highlighter(text='catcatcatcatcatcatcatcatcatcatcatcatcatbatbatbatbatbatbatbatbatbatbatbatbatratratratratratratratratratratratratrat', labels=[("Chain ", 'blue')])
st.write(annotations)
annotations2 = text_highlighter(text='', labels=[("Chain ", 'blue')])
st.write(annotations2)