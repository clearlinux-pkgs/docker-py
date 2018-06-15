#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-py
Version  : 3.3.0
Release  : 39
URL      : https://github.com/docker/docker-py/archive/3.3.0.tar.gz
Source0  : https://github.com/docker/docker-py/archive/3.3.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: docker-py-python3
Requires: docker-py-python
Requires: appdirs
Requires: asn1crypto
Requires: cffi
Requires: cryptography
Requires: dockerpy-creds
Requires: idna
Requires: packaging
Requires: pyOpenSSL
Requires: pycparser
Requires: pyparsing
Requires: requests
Requires: six
Requires: websocket_client
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pip-legacypython

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : setuptools-python
BuildRequires : websocket_client

%description
# Docker SDK for Python
[![Build Status](https://travis-ci.org/docker/docker-py.svg?branch=master)](https://travis-ci.org/docker/docker-py)

%package python
Summary: python components for the docker-py package.
Group: Default
Requires: docker-py-python3

%description python
python components for the docker-py package.


%package python3
Summary: python3 components for the docker-py package.
Group: Default
Requires: python3-core

%description python3
python3 components for the docker-py package.


%prep
%setup -q -n docker-py-3.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528560944
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
