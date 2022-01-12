import pandas as pd
import numpy as np
import time

output_df = pd.read_csv('outputs.csv', encoding='utf-8', header=None)
output_df = output_df.drop([output_df.columns[0]], axis='columns')  # remove index column
output_df = output_df.drop(0, axis='rows')  # remove column name (first row)
output_df.reset_index(drop=True, inplace=True)

output_df.columns -= 1

result_f = open('results.txt', 'r', encoding='utf-8')  # MOT

csi_times = output_df[0].tolist()
csi_times = list(map(float, csi_times))

# MOT를 다 읽고, CSI는 한 줄씩 읽기
# Read all Mot,  csi line by line
mot_times = dict()

while result_f:  # MOT
    line = result_f.readline().split()
    if len(line) != 0:
        mot_times[line[0]] = line[1]
    else:
        break

label = {}
threshold = 0.5  # error threshold

# ================ new =========================
'''
  Aftermoon-dev's code
'''
# Datalist에서 Value와 가장 유사한 값을 찾음
# Find the most similer value to value in the dataset
def matching_values(datalist, value):
    datalist = list(map(float, datalist))
    value = float(value)

    # Threshold 범위 내의 값만 Numpy Array에 담음
    array = np.asarray(list(filter((lambda x: abs(x - value) < threshold), datalist)))

    # 해당하는 값이 하나 이상이면
    # one or more corresponding
    if array.size > 0:
        # 그 중 가장 작은 값의 Index를 리턴
        # Return index of the smallest value
        minvalue = (np.abs(array - value)).argmin()
        return datalist.index(array[minvalue])
    else:
        # 하나도 없다면 -1
        #
        return -1


mot_time_list = list(mot_times.keys())

for csi_time in csi_times:
    # 두 값을 비교해 현재 CSI Time과 가장 유사한 MOT Time을 구함
    # Compare the two value to find the MOT frame most similar to the csi time
    compare = matching_values(mot_time_list, csi_time)

    # -1이면 매칭 실패
    #when match failed
    if compare == -1:
        label[csi_time] = -1
    # 그 외에는 해당하는 MOT Timestamp가 Return 되므로 그 값을 Label에 담음
    # Corresponding MOT times is returned so that the label is stored
    else:
        label[csi_time] = mot_times[mot_time_list[compare]]
        del mot_time_list[compare]

output_df['label'] = label.values()
output_df.to_csv('train_data.csv')
# ======================================================