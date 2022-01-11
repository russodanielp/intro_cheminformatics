from rdkit import Chem
from rdkit.ML.Descriptors import MoleculeDescriptors
from rdkit.Chem import AllChem
from rdkit.Chem import MACCSkeys
from rdkit.Chem import Descriptors
import os
from typing import List

import pandas as pd, numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


import plotly.graph_objects as go
import plotly.express as px

DATA_DIR = 'data'

def calc_descriptors_from_mol(mol):
    """
    Encode a molecule from a RDKit Mol into a set of descriptors.

    Parameters
    ----------
    mol : RDKit Mol
        The RDKit molecule.

    Returns
    -------
    list
        The set of chemical descriptors as a list.

    """
    calc = MoleculeDescriptors.MolecularDescriptorCalculator([desc[0] for desc in Descriptors.descList])
    return list(calc.CalcDescriptors(mol))

def read_mols(filepath: str):
    """ read an sdf file as mols """
    assert os.path.exists(filepath), "Check SDFile name"
    mols = [mol for mol in Chem.SDMolSupplier(filepath)]
    return mols


def read_sdfile_from_data(sdfilename: str):
    """ reads the sdfile in the data dir thats configured above """
    mols = read_mols(os.path.join(DATA_DIR, sdfilename))
    return mols

def get_principal_components(mols: List[Chem.Mol], n: int, act_col: None) -> pd.DataFrame:

    desc_list = []


    for mol in mols:
        desc = calc_descriptors_from_mol(mol)
        desc_list.append(desc)

        
    desc_frame = pd.DataFrame(desc_list)

    scaler = StandardScaler()

    desc_frame_std = pd.DataFrame(scaler.fit_transform(desc_frame))



    pca = PCA()

    latent_space = pca.fit_transform(desc_frame_std)
    latent_space = pd.DataFrame(latent_space[:, 0:n])
    latent_space.columns = ['PC{}'.format(i+1) for i in range(latent_space.shape[1])]

    if act_col:
        latent_space[act_col] = [float(mol.GetProp(act_col)) for mol in mols]

    
    return latent_space, pca.explained_variance_ratio_[:n]


def plot_pca(p_components: pd.DataFrame, act_col, ev):

    labels=dict(PC1="PC1: ({:.2f}%)".format(ev[0]),
                PC2="PC2: ({:.2f}%)".format(ev[1]),
                PC3="PC3: ({:.2f}%)".format(ev[2]))

    if act_col: 
        fig = px.scatter_3d(p_components, x='PC1', y='PC2', z='PC3', 
                            color=act_col, color_continuous_scale='rdylbu_r',
                            labels=labels)
    else:
        fig = px.scatter_3d(p_components, x='PC1', y='PC2', z='PC3', labels=labels)

    return fig