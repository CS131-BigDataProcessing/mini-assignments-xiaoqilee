from setuptools import setup, find_packages

setup(
    name="crime_test",  
    version="1.0",  
    packages=find_packages(),  
    install_requires=[
        "pandas>=1.0" 
    ],
    description="Validating crime victim data package",
    author="Xiao Qi Lee",
    author_email="xiaoqi.lee@sjsu.edu",
)
