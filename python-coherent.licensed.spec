Name:		python-coherent.licensed
Version:	0.5.2
Release:	1
Summary:	License management tooling for Coherent System projects
License:	MIT
Group:		Development/Python
URL:		https://github.com/coherent-oss/coherent.licensed
Source0:	https://files.pythonhosted.org/packages/source/c/coherent.licensed/coherent_licensed-%{version}.tar.gz
BuildRequires:	python
BuildRequires:	python%{pyver}dist(flit-core)
BuildSystem:	python
BuildArch:	noarch

%description
Setuptools plugin that injects license files into Python distributions
built from the Coherent System skeleton. keyring's build loads it.

%files
%doc README.md
%license LICENSE
%{python_sitelib}/coherent
%{python_sitelib}/coherent_licensed-%{version}.dist-info
