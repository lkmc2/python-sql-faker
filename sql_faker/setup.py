# coding=utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# 注册：python setup.py register
# 上传并发布：python setup.py sdist upload

setuptools.setup(
    name="sql-faker",
    version="1.0.1",
    author="lkmc2",
    author_email="lkmc2@163.com",
    description="A lightweight SQL data creator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lkmc2/python-sql-faker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)