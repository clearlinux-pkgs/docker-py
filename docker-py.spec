#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-py
Version  : 1.9.0
Release  : 23
URL      : http://pypi.debian.net/docker-py/docker-py-1.9.0.tar.gz
Source0  : http://pypi.debian.net/docker-py/docker-py-1.9.0.tar.gz
Summary  : Python client for Docker.
Group    : Development/Tools
License  : Apache-2.0
Requires: docker-py-legacypython
Requires: docker-py-python
Requires: requests
Requires: six
Requires: websocket_client
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : websocket_client

%description
docker-py
=========
|Build Status|
A Python library for the Docker Remote API. It does everything the
``docker`` command does, but from within Python âÂ run containers, manage
them, pull/push images, etc.

%package legacypython
Summary: legacypython components for the docker-py package.
Group: Default

%description legacypython
legacypython components for the docker-py package.


%package python
Summary: python components for the docker-py package.
Group: Default
Requires: docker-py-legacypython

%description python
python components for the docker-py package.


%prep
%setup -q -n docker-py-1.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505001969
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505001969
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
