from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='splade',
    version='2.1',
    description='SParse Lexical AnD Expansion Model for First Stage Ranking',
    url='https://github.com/naver/splade',
    packages=find_packages(),
    license="Creative Commons Attribution-NonCommercial-ShareAlike",
    long_description=readme,
    install_requires=[
        'omegaconf==2.1.2' 
    ],
)
