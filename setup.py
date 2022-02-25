import setuptools
from setuptools import setup


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
]

setup(
    name="hashily",
    version="0.0.6",
    description="A module that allows you to encode and decode text in numerous ciphers.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TrueMyst/hashily",
    project_urls={"Issue tracker": "https://github.com/TrueMyst/hashily/issues", "Documentation" : "https://hashily.readthedocs.io/en/latest/"},
    author="myst.67",
    license="MIT",
    classifiers=classifiers,
    keywords=["encryption", "utils", "encode", "ciphers", "decode"],
    packages=setuptools.find_packages(),
)
