from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

testing = ["pytest", "pytest-django", "pytest-cov", "pytest-sugar"]

debugging = ["django-debug-toolbar"]

setup(
    name="zootable",
    author="Benjamin Falk",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={"test": testing, "debug": debugging, "all": testing + debugging},
)
