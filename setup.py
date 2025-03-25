from setuptools import setup

setup(
    name="my-python-app",
    version="0.1",
    py_modules=["main"],  # Directly reference main.py
    install_requires=["Flask"],
)