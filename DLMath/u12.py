import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import sklearn.datasets
import sklearn.linear_model
from sklearn.neural_network import MLPClassifier
import matplotlib.colors

def plot_decision_boundary(model, X, y , sklearn = False):
    # Set min and max values and give it some padding
    x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1
    y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1
    h = 0.1
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid
    if sklearn:
      Z = model(np.c_[xx.ravel(), yy.ravel()])
    else:
      Z = model((np.c_[xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["lightyellow","lightskyblue"])
    plt.contourf(xx, yy, Z, cmap=cmap)
    #plt.contourf(xx, yy, Z, color = ['yellow' , 'pink'])
    plt.ylabel('x2')
    plt.xlabel('x1')
    XT = X.T
    red_mask = y[0 , :] == 0
    red_dots = XT[red_mask , :]
    blue_mask = y[0 , :] == 1
    blue_dots = XT[blue_mask , :]
    plt.scatter(red_dots[:, 0], red_dots[:, 1], c='darkorange')
    plt.scatter(blue_dots[:, 0], blue_dots[:, 1], c='darkblue')

def load_planar_dataset():
    np.random.seed(1)
    m = 400 # number of examples
    N = int(m/2) # number of points per class
    D = 2 # dimensionality
    X = np.zeros((m,D)) # data matrix where each row is a single example
    Y = np.zeros((m,1), dtype='uint8') # labels vector (0 for red, 1 for blue)
    a = 1 # maximum ray of the flower

    for j in range(2):
        ix = range(N*j,N*(j+1))
        t = np.linspace(j*3.12,(j+1)*3.12,N) + np.random.randn(N)*0.2 # theta
        r = a*np.sin(4*t) + np.random.randn(N)*0.2 # radius
        X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
        Y[ix] = j
        
    X = X.T
    Y = Y.T

    return X, Y