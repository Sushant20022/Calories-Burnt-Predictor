from setuptools import setup,find_packages
from typing import List
setup(
    name='Calorie Predictor App',
    version="0.0.1",
    author="Sushant Gangwar",
    author_email="gangwarsushant776@gmail.com",
    packages=find_packages(),

    requires=["Pymongo"],
)