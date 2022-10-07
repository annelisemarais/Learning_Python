from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#Condtion FAM CTRL

# load matlab file (as dictionnary)
aty_ML = loadmat('Atypical.mat')

#choose right variable in the mat file
aty_ML = aty_ML['ROI_stats_Atypical']

# load matlab file (as dictionnary)
ty_ML = loadmat('Typical.mat')

#choose right variable in the mat file
ty_ML = aty_ML['ROI_stats_Typical']


def rawmatrix2status(ROI_Matrix,Neurodev_status): #transforms matrix to data frame with added info
    #Example fam_somato_aty = rawmatrix2status(annots_[0,2],'atypical')
    Cond_ROI_NS = pd.DataFrame(ROI_Matrix) #Matrix to data frame
    Cond_ROI_NS["sub"] = Cond_ROI_NS.index +1 #add index
    Cond_ROI_NS['status'] = Neurodev_status #add neurodevelopmental status
    return Cond_ROI_NS


aty_status = [[],[]] #create an array of arrays
for ind_row,row in enumerate(aty_ML): #get index and row data of matrix (2*7 arrays)
    for ind_col, matrix in enumerate(row): #get index and column data (1*7*2 arrays)
        transformed_matrix = rawmatrix2status(matrix,'atypical') #Use function
        aty_status[ind_row].append(transformed_matrix) #add each transformed matrix in the new array of arrays


#display aty_status[1][5]