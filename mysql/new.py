import numpy as np
import sklearn.preprocessing as sp
Input_data = ([2.1, -1.9, 5.5],
                      [-1.5, 2.4, 3.5],
                      [0.5, -7.9, 5.6],
                      [5.9, 2.3, -5.8])

proc = np.array(Input_data)

data_binarized = sp.Binarizer(threshold = 0.5).transform(proc)
print("\nBinarized data:\n", data_binarized)