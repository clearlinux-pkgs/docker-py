#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-py
Version  : 3.7.2
Release  : 55
URL      : https://github.com/docker/docker-py/archive/3.7.2.tar.gz
Source0  : https://github.com/docker/docker-py/archive/3.7.2.tar.gz
Summary  : No detailed summary available
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
Requires: six
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
BuildRequires : six
BuildRequires : urllib3
BuildRequires : websocket_client

%description
# Docker SDK for Python
[![Build Status](https://travis-ci.org/docker/docker-py.svg?branch=master)](https://travis-ci.org/docker/docker-py)

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

%description python3
python3 components for the docker-py package.


%prep
%setup -q -n docker-py-3.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571089656
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
mkdir -p %{buildroot}/usr/share/package-licenses/docker-py
cp %{_builddir}/docker-py-3.7.2/LICENSE %{buildroot}/usr/share/package-licenses/docker-py/48f08e3492b2d97883a8f5d1f7b92b7d30f11b2c
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
