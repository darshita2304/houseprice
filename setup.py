from setuptools import setup,find_packages
from  typing import List

# HYPEN_E_DOT = '-e .'

# # file_path is string argument list of string return by this fn
# def get_requirements(file_path:str)->List[str]:
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines() # with reading \n will be returned also...
#         requirements = [req.replace("\n","") for req in requirements]#  replace \n in raw text

#         # if HYPEN_E_DOT in requirements:
#         #     requirements.remove(HYPEN_E_DOT)

#     return requirements 


setup(name="reGRESSORpROJECT",
    version="0.0.1", 
    author="Darshita",
    author_email="dppaghadal@gmail.com", 
    packages = find_packages(),
    # install_requires=get_requirements("requirements.txt"))
    install_requires=["pandas", "numpy", "flask"])