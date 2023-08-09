from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of required libraries from requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] 

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
        
setup(
name = 'dsproject',
version = '0.0.1',
Summary = 'end to end data science project',
author = 'Priyanka Katre',
author_email = 'katre.priyanka1710@gmail.com',
license = 'N/A',
Platform = 'vscode',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
