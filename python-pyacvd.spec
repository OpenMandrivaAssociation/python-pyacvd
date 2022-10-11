%global module	pyacvd
%global fname %(m=%{module}; echo ${m:0:1})

Summary:	A Python implementation of surface mesh resampling algorithm ACVD
Name:		python-%{module}
Version:	0.2.8
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/pyvista/pyacvd
Source0:	https://github.com/pyvista/%{module}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/%{fname}/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(cython)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

%files
%license LICENSE
%doc README.rst
%{py_platsitedir}/%{module}/
%{py_platsitedir}/%{module}-%{version}.dist-info/

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

