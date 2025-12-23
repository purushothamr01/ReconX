from setuptools import setup, find_packages


setup(
name="reconkit",
version="1.0.0",
author="Purushotham R",
description="ReconKit - A personal reconnaissance framework for bug bounty",
long_description=open("README.md", "r", encoding="utf-8").read(),
long_description_content_type="text/markdown",
url="https://github.com/purushothamr01/reconkit",
packages=find_packages(),
py_modules=["reconkit"],
python_requires=">=3.8",
install_requires=[
"requests",
"httpx",
"aiohttp",
"beautifulsoup4",
"colorama",
"rich",
"slack_sdk",
"discord-webhook",
"pyjsparser",
"pyyaml",
"tqdm",
"packaging",
"regex",
],
entry_points={
"console_scripts": [
"reconkit = reconkit:main",
],
},
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
)
