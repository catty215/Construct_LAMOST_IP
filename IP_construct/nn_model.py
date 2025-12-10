import numpy as np


def leaky_relu(z):
    """
    Leaky ReLU activation function.
    """
    return z * (z > 0) + 0.01 * z * (z < 0)


def get_spectrum_from_neural_net(scaled_labels, NN_coeffs):
    """
    Predict a normalized spectrum given scaled input labels and neural network coefficients.
    """

    w_array_0, w_array_1, w_array_2, b_array_0, b_array_1, b_array_2, x_min, x_max = NN_coeffs

    inside = np.einsum('ij,j->i', w_array_0, scaled_labels) + b_array_0
    outside = np.einsum('ij,j->i', w_array_1, leaky_relu(inside)) + b_array_1
    spectrum = np.einsum('ij,j->i', w_array_2, leaky_relu(outside)) + b_array_2

    return spectrum