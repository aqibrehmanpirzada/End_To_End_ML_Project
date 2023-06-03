from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This Function Will Return the List of Requirements which are necessary for the project
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="END-TO-END-ML_PROJECT",
    version='0.0.1',
    author='aqibrehmanpirzada',
    author_email='aqibrehmanpirzada75@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
