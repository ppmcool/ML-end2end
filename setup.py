from gettext import install
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(path:str)->List[str]:

    requirements=[]
    with open(path) as f:
        requirements=f.readlines()
        requirements=[i.replace('\n','') for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


    

setup(
    name='mlproj-end2end',
    version='0.0.1',
    author='ppmcool',
    author_email='pritampatra988@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
