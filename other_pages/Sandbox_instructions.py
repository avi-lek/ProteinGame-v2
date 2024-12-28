import streamlit as st
from st_pages import hide_pages

st.set_page_config(page_title="My Protein Is Broken!", page_icon=":dna:", layout="wide")
hide_pages(["Transcription", "Identify Mutations", "Translation", "Sandbox Instructions"])
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.header("Sandbox Instructions")
layout, gen_settings, viz_settings = st.tabs(["Layout", "General Settings", "Visualization Settings"])

if st.sidebar.button("Go To Sandbox"):
    st.switch_page("other_pages//Sandbox.py")

with layout:
    st.markdown('''With the Sandbox, users are able to visualize protein structures and experiment with their amino acid sequences.''')
    st.image("screenshots//sandbox_diagram1.png")
    st.markdown('''
            1. Select the current page here.
            2. Toggle between settings here.
            3. Settings are displayed here.
            4. The Protein is displayed here.
    ''')

with gen_settings:
    with st.expander("Protein Selection"):
        st.image("screenshots//choose_protein.png")
        st.markdown('''
            The first step to using the Sandbox is choosing which protein to visualize. The website offers several preloaded proteins, such as Glucagon, Insulin, and Myoglobin. 
            However, users can also view the structure of any protein by passing in the PDB ID. All proteins visualized on this website are sourced from the Protein Data Bank (PDB), which is a database of protein structures in which each protein is assigned a four letter ID. To find this ID, simply search the protein name and then “pdb” into a web browser. For example, the search “Insulin pdb” returns “3I40”, which is its ID. 
        ''')
    with st.expander("ML Structure Prediction"):
        st.image("screenshots//esm_use.png")
        st.markdown('''
            Users are also able to view a potential impact of changes to the amino acid sequence in a protein, predicted through Meta’s ESMFold, an AI model that predicts protein structure. Once user’s toggle on this option, a text box will appear at the bottom of this sidebar, allowing the user to type in or delete amino acids.
            
            ** Since ESMFold structures are predictions, they are not guaranteed to match with structures determined through other methods. 
            
            ** The version of ESMFold implemented in this website views all inputted sequences as a single continuous chain.

        ''')
    with st.expander("Overlaid Structures"):
        st.image("screenshots//overlay.png")
        st.markdown('''
            While viewing the impact of amino acid changes to protein structure, it may be helpful for users to visualize multiple structures superimposed onto each other. This can be done through toggling on the “Overlay Structures” switch. Using this option results in an editable table appearing above the protein and two new buttons appearing in the sidebar. Each column of the table represents a protein, each column controlling different aspects of the visualization: the “Color” column denotes the color of each overlaid structure, the user is able to edit the sequence column to alter  proteins’  amino acids, and clicking off the checkboxes in the “Show” column will hide proteins. The “Add Protein” button adds a new row to the table, and the “Restart” button clears the table.
        ''')
    with st.expander("Hover Tags"):
        st.image("screenshots//tags.png")
        
with viz_settings:
    with st.expander("Model Type"):
        st.image("screenshots//model_type.png")
    with st.expander("Ribbon Model Opacity"):
        st.image("screenshots//ribbon_opacity.png")
    with st.expander("Ribbon Highlighting"):
        st.image("screenshots//ribbon_highlighting.png")
    with st.expander("Van Der Waals Surface"):
        st.image("screenshots//vdw_surface.png")
    with st.expander("Subchain Selection"):
        st.image("screenshots//subchain.png")

st.markdown("**To go to sandbox, click the 'Go To Sandbox' button in the sidebar.**")


