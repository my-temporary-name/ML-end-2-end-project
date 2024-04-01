from setuptools import find_packages, setup
from typing import List

Hypen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)



setup(
    name="ML_Project1",
    version="0.0.1",
    author="Ankit",
    author_email="ankityadav123774@gmail.com",
    packages=find_packages(), # it will automatically include all the packages in the directory by reading the __init__.py file in all the directories
    # install_requires=['pandas','numpy','seaborn']
    # or we can do
    install_requires=get_requirements('requirements.txt')
)