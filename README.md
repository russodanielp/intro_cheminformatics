


# Introduction

This repository contains a set of notebooks (organized into seperate topics by lab) for an introduction to cheminformatics in the Python programming language.  Introductions to programming using the Python programming language are included.  The notebooks rely on a set of both dependecies Python and other packages listed in the `environmental.yml`.  Thus, installing a Python environment using [conda](https://docs.conda.io/en/latest/) is required.  Conda installation can be done as described on the [conda website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).  Some notebooks are taken from the incredible [Teach Open Computer-aided Drug Design](https://github.com/volkamerlab/teachopencadd) course.  However, notebooks in this repository are geared to noive programmers.  

## Running the notebooks locally

After conda is properly installed, a new conda environment for these notebooks can be created by the command:
```bash
conda env create -f environment.yml -n intro-chem 
```
The environment can then be activated by:
```bash
conda activate intro-chem
```
And the notebooks can be opened via:
```bash
jupyter lab
```
or 
```bash
jupyter notebook
```

## Running the notebooks locally

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/russodanielp/intro_cheminformatics/HEAD)

Alternatively, the notebooks can be run on a server via binder by clicking the above binder tag or opening them up [here](https://mybinder.org/v2/gh/russodanielp/intro_cheminformatics/HEAD).  


## Overview

1) Course Introduction  
#TODO: This is empty

2)  Introduction to chemical structure annotations– 2D &3D  
Teach structure annotations: ChemBioOffice, SMILE, SDF and etc. First homework assignment
#TODO: This is empty

3) Basic Python, Pandas and matplotlib  
Introducet the basics of programming using the Python language.  Introduce popular data science and visualization packages, Pandas and matplotlib.

5) Advanced python and RDKit   
A brief introduction to Objects in Python.  Introduction to the cheminformatics Python library RDKit.

4) Molecular Descriptors   
Generating chemical descriptors - explores the basics of generting molecular descriptors and chemical fingerprints.

6) Chemical Similarity  
The basics of chemical similarities using different metrics and descriptor spaces.

7) Machine Learning Part I - Unsupervised ML  
The basics of unsupervised machine learning, including principal component analysis and chemical clustering. 

8) Machine Learning Part I - QSAR  
The basics of supervised machine learning and developing quantitative structure activity relationship (QSAR) models.  Develop classification and regression models on a set of benzodiazipines. 

9) Data science in chemistry  
Learning about web retrieval services and how to access chemistry databases via programmatic interfaces.

10) Predictive modeling  
#TODO: Maybe write a notebook that can be run on any dataset?  Not sure what needs to be done here just yet.  

11) Pharmacophores  
Generating pharmacophores using a ligand based approach for EGFR receptor

12) Structural-based Drug Discovery  
The use of commercial cheminformatics tool-CASE Ultra
  

13) Deep Learning   
Develop a deep learning model using data provided from the NICEATM acute oral toxicity challenge.
