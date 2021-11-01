#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-py
Version  : 5.0.3
Release  : 74
URL      : https://files.pythonhosted.org/packages/ab/d2/45ea0ee13c6cffac96c32ac36db0299932447a736660537ec31ec3a6d877/docker-5.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ab/d2/45ea0ee13c6cffac96c32ac36db0299932447a736660537ec31ec3a6d877/docker-5.0.3.tar.gz
Summary  : A Python library for the Docker Engine API.
Group    : Development/Tools
License  : Apache-2.0
Requires: docker-py-license = %{version}-%{release}
Requires: docker-py-python = %{version}-%{release}
Requires: docker-py-python3 = %{version}-%{release}
Requires: appdirs
Requires: asn1crypto
Requires: cffi
Requires: cryptography
Requires: docker-pycreds
Requires: idna
Requires: packaging
Requires: paramiko
Requires: pyOpenSSL
Requires: pycparser
Requires: pyparsing
Requires: requests
Requires: urllib3
Requires: websocket_client
BuildRequires : appdirs
BuildRequires : asn1crypto
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : cryptography
BuildRequires : docker-pycreds
BuildRequires : idna
BuildRequires : packaging
BuildRequires : paramiko
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : pycparser
BuildRequires : pyparsing
BuildRequires : requests
BuildRequires : setuptools-python
BuildRequires : urllib3
BuildRequires : websocket_client

%description
# Docker SDK for Python
[![Build Status](https://github.com/docker/docker-py/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/docker/docker-py/actions/workflows/ci.yml/)

%package license
Summary: license components for the docker-py package.
Group: Default

%description license
license components for the docker-py package.


%package python
Summary: python components for the docker-py package.
Group: Default
Requires: docker-py-python3 = %{version}-%{release}

%description python
python components for the docker-py package.


%package python3
Summary: python3 components for the docker-py package.
Group: Default
Requires: python3-core
Provides: pypi(docker)
Requires: pypi(requests)
Requires: pypi(websocket_client)

%description python3
python3 components for the docker-py package.


%prep
%setup -q -n docker-5.0.3
cd %{_builddir}/docker-5.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635725241
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/docker-py
cp %{_builddir}/docker-5.0.3/LICENSE %{buildroot}/usr/share/package-licenses/docker-py/48f08e3492b2d97883a8f5d1f7b92b7d30f11b2c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/docker-py/48f08e3492b2d97883a8f5d1f7b92b7d30f11b2c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
