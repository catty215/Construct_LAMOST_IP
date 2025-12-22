Construct_LAMOST_IP

Tools for interpolating the IP of LAMOST with neural networks.


Download and Install:

git clone https://github.com/catty215/Construct_LAMOST_IP.git

pip install -e .


Usage Example:

from IP_construct import get_IP

wl, flux = get_IP(spec_id, label1_time, label2_fiber, label3_line)


## Citation

If you use the package or related code in your research work, please cite our paper:

> [Your Full Paper Title](Paper DOI or URL),
> [Author Names (Last Name, First Initial.)],
> *Monthly Notices of the Royal Astronomical Society* (MNRAS), [Year], [Volume], [Pages].

**BibTeX Entry:**
```bibtex
@article{your-bibtex-key,
  title={Your Full Paper Title},
  author={Lastname1, F. and Lastname2, S. and Lastname3, T.},
  journal={Mon. Not. R. Astron. Soc.},
  volume={XXX},
  pages={XXX--XXX},
  year={XXXX},
  doi={10.1093/mnras/xxxxxx}
}


