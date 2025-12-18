Construct_LAMOST_IP

Tools for interpolating the IP of LAMOST with neural networks.

git clone https://github.com/catty215/Construct_LAMOST_IP.git

Example:
from Construct_LAMOST_IP.IP_construct import get_IP
wl, flux = get_IP(spec_id, label1_time, label2_fiber, label3_line)
