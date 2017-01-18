Aliyun Ansible Modules Documentation
=============================================

This project contains the source code of Module Documentation for Aliyun Ansible. 
Follow below instructions to generated documentation from `DOCUMENTATION` string in the modules.

1) Install sphinx and theme:
To install sphinx and the required theme, install pip and then 

```
pip install sphinx sphinx_rtd_theme
```

2) Build the documentation
To build module documentation you'll need to run below command at the top level of the repository. 

```
make webdocs 
```
The generated html files are in `_build/html/` folder
