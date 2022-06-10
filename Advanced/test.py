import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import random


def random2d(pixels):
    noise_array = np.random.rand(pixels ** 2)
    noise_array = noise_array.reshape([pixels, pixels])
    return noise_array


def random_vector():
    vectors = np.array([[1, 1], [-1, 1], [1, -1], [-1, -1], [math.sqrt(2), 0], [0, math.sqrt(2)], [-math.sqrt(2), 0],
                        [0, -math.sqrt(2)]])

    random_vector = vectors[np.random.choice(8, size=1, replace=False)]

    return random_vector.flatten()


def define_gradients_2d(matrix, quadrants):
    """
    The function takes the matrix, considers its shape and lenght and 
    returns lattice point coordinates and random vector value 
    for each gradient vector for this matrix in the shape
    [...[(x, y), (u, v)]...], where x, y are origin points and u, v are the axis values for each vector
    """
    split = math.sqrt(quadrants)
    lenght = len(matrix)
    gradient_list = []
    quad_info = dict()
    step = int(lenght / split)
    for i in range(0, lenght + 1, step):
        for j in range(0, lenght + 1, step):
            coordinates = (i, j)
            value = tuple(random_vector())
            gradient_list.append(coordinates + value)

    for q in range(0, lenght, step):
        for r in range(0, lenght, step):
            for t in gradient_list:
                x, y, u, v = t
                if (x == q or x - step == q) and (y == r or y - step == r):
                    if (q, r) not in quad_info.keys():
                        quad_info[(q, r)] = list()
                    quad_info[(q, r)].append((u, v))

    print(quad_info)
    print(len(quad_info))
    print(len(quad_info[(0,0)]))


    # return gradient_list

pixels = 256
quadrants = 16
initial_matrix = random2d(pixels)
define_gradients_2d(initial_matrix, quadrants)