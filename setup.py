from setuptools import setup
from typing import List
 
# def get_requirements(filepath:str)->List[str]:
#     with open(filepath) as f:
#         requirements = [req.strip() for req in f.readlines()]
 
#         if '-e .' in requirements:
#             requirements.remove('-e .')
 
#     return requirements
 
setup(
    name='netcdf_unpacker',
    packages = ['netcdf_unpacker'],
    package_dir = {'netcdf_unpacker':'netcdf_unpacker'},
    version='1.0.0',
    license= 'MIT',
    author='Ananya Giliyal, Atishay Gwari, Isha Paranjpe, Mansi Katgire',
    description = 'Introducing the nc_unpack tool! Simplify NetCDF data extraction and analysis. Explore and unpack NETCDF files effortlessly.',
    author_email='giliyal.ananya@gmail.com, atishay345@gmail.com, ishaparanjpe28@gmail.com, katgiremansi@gmail.com',
    url = 'https://github.com/Ananya0703/NetCDF_Unpacker',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    download_url = 'https://github.com/Ananya0703/NetCDF_Unpacker/archive/refs/tags/1.0.0.tar.gz',
    install_requirements= ['pandas','openpyxl','numpy','netCDF4']
)
