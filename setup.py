from setuptools import find_packages,setup

from typing import List

HYPHEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This will return the list of lib to install given in requirement.txt
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
name='Vehicle_prediction',
version='0.0.1',
author='Ankit',
author_email='ankit.ghai@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') # Earlier we have given ['pandas','numpy','seaborn'] as possible pkgs to install but sometimes we need large number of pkgs to install for that we create function like this where we pass requirements.txt file which list all the pkges we needed.   




)