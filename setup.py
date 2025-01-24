from setuptools import find_packages,setup
from typing import List 
HYPER_PARA = '-e .'# this is used because we are using this -e .  in the requirements file to call or intitalize the setup.py file so if while  getting the list of the libraries and dependencies we get this -e. thing so if you get it then egnore it.

def get_requirements(file_path:str)->List[str]:
    """this function return list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('/n',"")for req in requirements]

        if HYPER_PARA in requirements:
            requirements.remove(HYPER_PARA)

    return requirements

setup(
    name = 'Db_chatbot',
    version = '0.1',
    author = 'saurabh_singh',
    author_email = 'ss1477889@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
    
    )