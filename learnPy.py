import numpy as np
from sklearn.datasets import fetch_openml  

# descargamos los datos y les asignamos la varible dist

mnist = fetch_openml('mnist_784', version=1)
X, y = mnist["data"].values.astype(np.float32), mnist["target"].values.astype(int)
print(mnist)