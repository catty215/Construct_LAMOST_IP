"""
Predict normalized spectral line profiles using a neural network model.
"""
from .IP_construct import get_IP
from .utils import convert_minutes_to_datetime
from .nn_model import get_spectrum_from_neural_net