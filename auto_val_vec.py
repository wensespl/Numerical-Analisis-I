import numpy as np

#np.dot()

mat = np.array([[3, 2],
                [2, 6]])

print(np.linalg.inv(mat))

#eigenvalue, featurevector = np.linalg.eig(mat)

#print("Autovalores:", eigenvalue)
#print("Vector de características:\n", featurevector)
