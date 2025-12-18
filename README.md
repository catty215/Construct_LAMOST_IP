Construct_LAMOST_IP

Tools for interpolating the IP of LAMOST with neural networks.


Download and Install:

git clone https://github.com/catty215/Construct_LAMOST_IP.git

pip install -e .


Usuage Example:

from IP_construct import get_IP

wl, flux = get_IP(spec_id, label1_time, label2_fiber, label3_line)



