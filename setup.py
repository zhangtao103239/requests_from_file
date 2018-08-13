import setuptools

with open ( "README.md" , "r",encoding="utf-8" ) as fh :
    long_description = fh . read ()

setuptools . setup (
    name = "requests_from_file" ,
    version = "0.0.1" ,
    author = "zhangtao103239" ,
    author_email = "zhangtao103239@163.com" ,
    description = "create requests params from file,file is created by Firefox Header" ,
    long_description = long_description ,
    long_description_content_type = "text/markdown" ,
    url = "https://github.com/zhangtao103239/requests_from_file" ,
    packages = setuptools . find_packages (),
    classifiers = (
        "Programming Language :: Python :: 3" ,
        "License :: OSI Approved :: MIT License" ,
        "Operating System :: OS Independent" ,
    ),
)
