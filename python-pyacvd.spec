%define module	pyacvd

Summary:	A Python implementation of surface mesh resampling algorithm ACVD
Name:		python-%{module}
Version:	0.2.7
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/pyvista/pyacvd
Source0:	https://pypi.io/packages/source/p/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

%files
%license LICENSE
%doc README.rst
%{py_platsitedir}/%{module}/
%{py_platsitedir}/%{module}-%{version}-py%{python_version}.egg-info/

#----------------------------------------------------------------------------

%description
This module takes a surface mesh and returns a uniformly meshed surface using
voronoi clustering. This approach is loosely based on research by S. Valette,
and J. M. Chassery in ACVD.

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install
