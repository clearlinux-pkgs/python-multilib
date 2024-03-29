#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-multilib
Version  : 1.3
Release  : 46
URL      : https://files.pythonhosted.org/packages/7b/04/4b874882aba1fb4fe505e8d1e2b136cbd25a07944ba919d3f7ee0915851e/python-multilib-1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/7b/04/4b874882aba1fb4fe505e8d1e2b136cbd25a07944ba919d3f7ee0915851e/python-multilib-1.3.tar.gz
Summary  : module for determining if a package is multilib
Group    : Development/Tools
License  : GPL-2.0
Requires: python-multilib-license = %{version}-%{release}
Requires: python-multilib-python = %{version}-%{release}
Requires: python-multilib-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
# python-multilib
A Python library for determining if a package is multilib or not

%package license
Summary: license components for the python-multilib package.
Group: Default

%description license
license components for the python-multilib package.


%package python
Summary: python components for the python-multilib package.
Group: Default
Requires: python-multilib-python3 = %{version}-%{release}

%description python
python components for the python-multilib package.


%package python3
Summary: python3 components for the python-multilib package.
Group: Default
Requires: python3-core
Provides: pypi(python_multilib)
Requires: pypi(six)

%description python3
python3 components for the python-multilib package.


%prep
%setup -q -n python-multilib-1.3
cd %{_builddir}/python-multilib-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583541665
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-multilib
cp %{_builddir}/python-multilib-1.3/LICENSE %{buildroot}/usr/share/package-licenses/python-multilib/2f7458fd0e7cb17d3e9393379f3eb3434c91a978
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-multilib/2f7458fd0e7cb17d3e9393379f3eb3434c91a978

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
