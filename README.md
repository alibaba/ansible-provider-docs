Aliyun Ansible Modules Documentation
=============================================

This project contains the source code of Module Documentation for Aliyun Ansible. 
Follow below instructions to generate documentation from `DOCUMENTATION` string in the modules.


## Pre-Requisites (Ubuntu OS)

* `make` utility <br/><br/>
 Make utility is required to generate html docs. Install `make` utility by running below command on Ubuntu.
```sh
sudo apt-get -y install make 
```
* `python` version 2.7.X<br/><br/>
 Run below command to install `python`.
```sh
sudo apt-get -y install python2.7
```
Check python installation by running below command.
```sh
python --version
```
* Install `pip`<br/><br/>
 Run below command to install `pip` and other packages.
```sh
sudo apt-get -y install python-pip python-dev dos2unix
```

* Install sphinx and theme: 

```sh
pip install sphinx==1.4.8 sphinx_rtd_theme
```

## Formatting pulled files
Run below command in `ansible-provider-docs` folder to fix this issue.
```sh
find . -type f -name '*' -exec dos2unix '{}' +
```

## Build the documentation
To build module documentation you'll need to run below command in `ansible-provider-docs` folder. 

```
make webdocs 
```
The generated html files are in `_build/html/` folder
