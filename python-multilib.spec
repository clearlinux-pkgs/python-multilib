#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-multilib
Version  : 1.2
Release  : 20
URL      : http://pypi.debian.net/python-multilib/python-multilib-1.2.tar.gz
Source0  : http://pypi.debian.net/python-multilib/python-multilib-1.2.tar.gz
Summary  : module for determining if a package is multilib
Group    : Development/Tools
License  : GPL-2.0
Requires: python-multilib-python3
Requires: python-multilib-license
Requires: python-multilib-python
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : six

%description
# python-multilib
A Python library for determining if a package is multilib or not

%package legacypython
Summary: legacypython components for the python-multilib package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the python-multilib package.


%package license
Summary: license components for the python-multilib package.
Group: Default

%description license
license components for the python-multilib package.


%package python
Summary: python components for the python-multilib package.
Group: Default
Requires: python-multilib-python3

%description python
python components for the python-multilib package.


%package python3
Summary: python3 components for the python-multilib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-multilib package.


%prep
%setup -q -n python-multilib-1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530376792
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1530376792
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/python-multilib
cp LICENSE %{buildroot}/usr/share/doc/python-multilib/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/python-multilib/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
