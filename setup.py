from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    Returns the list of requirements .
    '''
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="my_package",
    version="0.1.0",
    author="kkb",
    author_email="krishnakantabera03@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)