import numpy as np
from .utils import convert_minutes_to_datetime, wl_range
from .nn_model import get_spectrum_from_neural_net

def get_lsf(spec_id, label1_time, label2_fiber, label3_line):
    """
    Retrieve the LSF profile

    Parameters:
        spec_id (str or int): Spectrograph ID, a two-digit string or int ranging from '01' to '16',
                       representing one of the 16 LAMOST spectrographs.
        label1_time (int): Time label in minutes since 00:00:00 on November 17, 1858.
                             This value corresponds to the timestamp in the LAMOST spectrum filename.
        label2_fiber (int): Fiber ID ranging from 1 to 250, representing one of the fibers
                            in a spectrograph.
        label3_line (float): Central wavelength of the LSF profile. Valid values include:
                             For blue arm: 4046.565, 4358.335, 4678.149, 4799.912, 5085.822, 5460.750, 5790.670
                             For red arm:  5944.834, 6096.163, 6143.063, 6266.495, 6334.428, 6402.248,
                                           6506.528, 6598.953, 6678.276, 6929.467, 7173.938, 7245.167,
                                           7438.898, 7635.106, 8377.6065, 8495.3598
                     In theory, any wavelength can be used; however, some wavelengths do not correspond
                     to real emission lines and are thus meaningless. Others may correspond to actual lines,
                     but were not included in the training and therefore may yield unreliable results.
                     The set of wavelengths we trained on is well distributed across the full spectral range
                     and should be sufficient for most practical applications.

    Return:
        wl (np.ndarray): Wavelength array.
        flux (np.ndarray): Flux array of the predicted LSF profile, normalized such that the peak value is 1.
    """

    date = convert_minutes_to_datetime(label1_time)

    # Determine the neural network file:
    # For each year, spectrograph, and spectral arm (blue or red),
    # the neural network coefficients are stored in a single file.
    # This part selects the appropriate file based on the input parameters.
    if date.month >= 9:
        file_year = date.year + 1
    else:
        file_year = date.year

    if label3_line > 5800:
        NN_path = f'/data/liuqian/NN_training/{file_year}/NN_normalized_spectra_{spec_id}_r_{file_year}.npz'
    else:
        NN_path = f'/data/liuqian/NN_training/{file_year}/NN_normalized_spectra_{spec_id}_b_{file_year}.npz'

    # get the wavelength range for the profile
    a, b = wl_range()[label3_line]
    wl = np.linspace(a, b, 600)

    # load the neural network coefficients
    try:
        with np.load(NN_path) as tmp:
            w_array_0 = tmp["w_array_0"]
            w_array_1 = tmp["w_array_1"]
            w_array_2 = tmp["w_array_2"]
            b_array_0 = tmp["b_array_0"]
            b_array_1 = tmp["b_array_1"]
            b_array_2 = tmp["b_array_2"]
            x_min = tmp["x_min"]
            x_max = tmp["x_max"]

        NN_coeffs = (w_array_0, w_array_1, w_array_2, b_array_0, b_array_1, b_array_2, x_min, x_max)

        real_labels = np.array([label1_time, label2_fiber-1, label3_line])
        scaled_labels = (real_labels - x_min) / (x_max - x_min) - 0.5

        # get the flux
        flux = get_spectrum_from_neural_net(scaled_labels=scaled_labels, NN_coeffs=NN_coeffs)

        return wl, flux

    except Exception as e:
        print(f"Error loading model from {NN_path}: {str(e)}")
        return None, None