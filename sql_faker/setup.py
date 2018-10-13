# coding=utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# 注册：python setup.py register
# 上传并发布：python setup.py sdist upload
# 注册并发布：python setup.py register sdist upload

# 打包wheel：python setup.py bdist_wheel --universal
# 上传wheel：python setup.py bdist_wheel upload

setuptools.setup(
    name="sql-faker",
    version="1.1.7",
    author="lkmc2",
    author_email="lkmc2@163.com",
    description="A lightweight SQL data creator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lkmc2/python-sql-faker",
    packages=setuptools.find_packages(),
    platforms=["all"],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2.7',
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'DBUtils>=1.3',
        'pymysql>=0.9.2'
    ],
    data_files=[('', ['README.md'])]
)