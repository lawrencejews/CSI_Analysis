import pandas as pd
from pandas import read_csv
import numpy as np
from csv import writer
from csv import reader

output_df = pd.read_csv('./data/outputs.csv', encoding='utf-8', header=None)
output_df = output_df.drop([output_df.columns[0]], axis='columns')  # remove index column
output_df = output_df.drop(0, axis='rows')  # remove column name (first row)
output_df.reset_index(drop=True, inplace=True)

output_df.columns -= 1
output_df.to_csv('./data/csi_outputs.csv',

# assign header columns
header = ['Time', 'Subcar_0','Subcar_1', 'Subcar_2', 'Subcar_3', 'Subcar_4', 'Subcar_5', 'Subcar_6',
            'Subcar_7', 'Subcar_8', 'Subcar_9', 'Subcar_10', 'Subcar_11', 'Subcar_12',
            'Subcar_13', 'Subcar_14', 'Subcar_15', 'Subcar_16', 'Subcar_17', 'Subcar_18',
            'Subcar_19', 'Subcar_20', 'Subcar_21', 'Subcar_22', 'Subcar_23', 'Subcar_24',
            'Subcar_25', 'Subcar_26', 'Subcar_27', 'Subcar_28', 'Subcar_29', 'Subcar_30',
            'Subcar_31', 'Subcar_32', 'Subcar_33', 'Subcar_34', 'Subcar_35', 'Subcar_36'
            'Subcar_37', 'Subcar_38', 'Subcar_39', 'Subcar_40', 'Subcar_41', 'Subcar_42',
            'Subcar_43', 'Subcar_44', 'Subcar_45', 'Subcar_46', 'Subcar_47', 'Subcar_48',
            'Subcar_49', 'Subcar_50', 'Subcar_51', 'Subcar_52', 'Subcar_53', 'Subcar_54',
            'Subcar_55', 'Subcar_56', 'Subcar_57', 'Subcar_58', 'Subcar_59', 'Subcar_60',
            'Subcar_61', 'Subcar_62', 'Subcar_63','Subcar_64',
], index=True)
