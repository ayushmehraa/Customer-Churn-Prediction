from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if "-e ." in requirements:
            requirements.remove("-e .")
            # update the requirements to include the local package
    return requirements

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)