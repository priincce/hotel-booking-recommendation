from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
      name="mlops-01",
      version="0.1.0",
      author="Prince Kumar",
      packages=find_packages(),
      install_requires=requirements,
)