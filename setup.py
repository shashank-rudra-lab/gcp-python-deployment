from setuptools import setup

setup(
    name="my-python-app",
    version="0.1",
    packages=["."],  # Include current directory
    install_requires=["Flask"],
)