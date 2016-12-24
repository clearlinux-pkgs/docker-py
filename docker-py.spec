#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docker-py
Version  : 1.9.0
Release  : 15
URL      : http://pypi.debian.net/docker-py/docker-py-1.9.0.tar.gz
Source0  : http://pypi.debian.net/docker-py/docker-py-1.9.0.tar.gz
Summary  : Python client for Docker.
Group    : Development/Tools
License  : Apache-2.0
Requires: docker-py-python
BuildRequires : flake8-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : requests-python
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
Requires: requests-python

%description python
python components for the docker-py package.


%prep
%setup -q -n docker-py-1.9.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
