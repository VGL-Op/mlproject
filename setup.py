# Responsible for creating this project as a package
# We can also deploy this in PyPI

from setuptools import find_packages, setup             # type: ignore  
from typing import List 

HYPEN_E_DOT = '-e .'

def get_requirements(file_path : str)-> List[str]:
    '''
    This function will return the list of requirements          
    '''
    requirements = []
    with open(file_path) as file_obj : 
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Vishal',
    author_email = 'vglinfinity010@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)