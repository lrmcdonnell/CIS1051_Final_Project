# CIS 1051 FINAL PROJECT: PROTEIN VISUALIZATION

    # Credit: Data used from Protein Data Bank (PDB)
    # Credit: Premise based on ESMFold: https://esmatlas.com/about
    # Credit: This app is inspired by https://huggingface.co/spaces/osanseviero/esmfold
    # Credit: App Setup Template from Chanin Nantasenamat (Data Professor) https://youtube.com/dataprofessor

# Import relevant modules:
import py3Dmol
import streamlit as st
from stmol import showmol
import requests

# Sidebar Layout using streamlit:
st.sidebar.title('Protein Visualization 🧑‍🔬🧪')
st.sidebar.write("This app predicts protein structures given a single amino acid sequence. It is based on Alphafold and ESMFold, which are protein structure predictors that use AI. Try inputting a sequence below!")

# Protein sequence default input using streamlit:
default_sequence = "DTHKSEIAHRFKDLGEEHFKGLVLIAFSQYLQQCPFDEHVKLVNELTEFAKTCVADESHAGCEKSLHTLFGDELCKVASLRETYGDMADCCEKQEPERNECFLSHKDDSPDLPKLKPDPNTLCDEFKADEKKFWGKYLYEIARRHPYFYAPELLYYANKYNGVFQECCQAEDKGACLLPKIETMREKVLASSARQRLRCASIQKFGER"
text = st.sidebar.text_area('Input sequence', default_sequence, height = 175) # create textbox with title, containing the above 'default' sequence
st.sidebar.write('For more info, check out [Alpha Fold](https://www.deepmind.com/research/highlighted-research/alphafold), [ESM Fold](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v1), and [this article](https://www.nature.com/articles/d41586-022-03539-1).')

# Create structure Using Input text:
def visualize(sequence = text):
    headers = {'Content-Type': 'application/x-www-form-urlencoded',} 
    data_url = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers = headers, data = sequence) #Fetch PDB data
    pdb_str = data_url.content.decode('utf-8') #get PDB data string
    
    # Set up Structure using py3Dmol & stmol:
    structure = py3Dmol.view()  #set up structure object
    structure.addModel(pdb_str,'pdb') 
    structure.setStyle({'cartoon':{'color':'spectrum'}})  #appearance of protein
    structure.zoomTo()     #zoom feature
    stop_spin = st.button('Stop Spin')
    if stop_spin:
        structure.spin(False) #This was a fail
    else:
         structure.spin(True)    #spin structure
    showmol(structure, height = 550, width = 900)  #show protein structure

predict = st.sidebar.button('Predict')     # Make button 
if predict:     # If button is pressed, show structure of input sequence
    st.subheader('Predicted protein structure')
    visualize(text)
else:
    st.warning('← Please enter a protein sequence.')
