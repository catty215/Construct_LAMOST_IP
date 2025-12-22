## Construct_LAMOST_IP

Tools for interpolating the IP of LAMOST with neural networks.


## 1.Download and Install:

git clone https://github.com/catty215/Construct_LAMOST_IP.git

pip install -e .


## 2.Usage Example (in python):

from IP_construct import get_IP

wl, flux = get_IP(spec_id, label1_time, label2_fiber, label3_line)

Note:

* spec_id (int): Spectrograph ID, ranging from 1 to 16, representing one of the 16 LAMOST spectrographs.

* label1_time (int): Time label in minutes since 00:00:00 on November 17, 1858. This value corresponds to the timestamp in the LAMOST spectrum filename.

* label2_fiber (int): Fiber ID ranging from 1 to 250, representing one of the fibers in a spectrograph.

* label3_line (float): Central wavelength of the IP. Valid values include:
In the blue arm: 4046.565, 4358.335, 4678.149, 4799.912, 5085.822, 5460.750, 5790.670.
In the red arm:  5944.834, 6096.163, 6143.063, 6266.495, 6334.428, 6402.248, 6506.528, 6598.953, 6678.276, 6929.467, 7173.938, 7245.167, 7438.898, 8377.6065, 8495.3598

In theory, any wavelength can be used; however, some wavelengths do not correspond to real emission lines and are thus meaningless. Others may correspond to actual lines, but were not included in the training and therefore may yield unreliable results. The set of wavelengths we trained on is well distributed across the full spectral range and should be sufficient for most practical applications.

## 3.Citation

This package is developed based on our ongoing research. If you use this package or related code in your research work, please cite our upcoming paper once it is published. The citation information will be updated here promptly after submission and acceptance.





