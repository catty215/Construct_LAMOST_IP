from setuptools import setup, find_packages

setup(
    name='Construct_LAMOST_IP',
    version='0.1.0',
    description="LAMOST's IP recover using neural networks",
    author='Qian Liu',
    author_email='liuqian@bao.ac.cn',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
    ],
)