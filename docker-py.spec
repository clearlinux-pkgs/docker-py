#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-py
Version  : 1.9.0
Release  : 17
URL      : http://pypi.debian.net/docker-py/docker-py-1.9.0.tar.gz
Source0  : http://pypi.debian.net/docker-py/docker-py-1.9.0.tar.gz
Summary  : Python client for Docker.
Group    : Development/Tools
License  : Apache-2.0
Requires: docker-py-python
Requires: backports.ssl_match_hostname
Requires: ipaddress
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

%package python
Summary: python components for the docker-py package.
Group: Default

%description python
python components for the docker-py package.


%prep
%setup -q -n docker-py-1.9.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489348711
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489348711
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
