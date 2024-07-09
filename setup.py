from setuptools import setup,find_packages
from typing import List
EDITABLE_VARIABLE='-e .'
def get_requirements(file_path:str)->List[str]:
    '''Function Used for Getting all the Requirements from Requirement.txt'''
    requirement : List[str]=[]
    with open(file_path)as obj:
        requirement=obj.readlines()
        requirement=[req.replace("\n"," ") for req in requirement]
    if(EDITABLE_VARIABLE in requirement):
        requirement.remove(EDITABLE_VARIABLE)
    return requirement

setup(
    name='Calorie Predictor App',
    version="0.0.1",
    author="Sushant Gangwar",
    author_email="gangwarsushant776@gmail.com",
    packages=find_packages(),

    install_requires=get_requirements('requirements.txt'),
)