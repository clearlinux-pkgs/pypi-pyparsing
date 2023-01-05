#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyparsing
Version  : 3.0.9
Release  : 108
URL      : https://files.pythonhosted.org/packages/71/22/207523d16464c40a0310d2d4d8926daffa00ac1f5b1576170a32db749636/pyparsing-3.0.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/71/22/207523d16464c40a0310d2d4d8926daffa00ac1f5b1576170a32db749636/pyparsing-3.0.9.tar.gz
Summary  : pyparsing module - Classes and methods to define and execute parsing grammars
Group    : Development/Tools
License  : MIT
Requires: pypi-pyparsing-license = %{version}-%{release}
Requires: pypi-pyparsing-python = %{version}-%{release}
Requires: pypi-pyparsing-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi-nose
BuildRequires : pypi-py
BuildRequires : pypi-pytest

%description
PyParsing -- A Python Parsing Module
====================================
|Build Status| |Coverage|

%package license
Summary: license components for the pypi-pyparsing package.
Group: Default

%description license
license components for the pypi-pyparsing package.


%package python
Summary: python components for the pypi-pyparsing package.
Group: Default
Requires: pypi-pyparsing-python3 = %{version}-%{release}

%description python
python components for the pypi-pyparsing package.


%package python3
Summary: python3 components for the pypi-pyparsing package.
Group: Default
Requires: python3-core
Provides: pypi(pyparsing)

%description python3
python3 components for the pypi-pyparsing package.


%prep
%setup -q -n pyparsing-3.0.9
cd %{_builddir}/pyparsing-3.0.9
pushd ..
cp -a pyparsing-3.0.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656399380
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyparsing
cp %{_builddir}/pyparsing-3.0.9/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyparsing/df156c6a0a89ed2a3bd4a473c68cf85907509ca0
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyparsing/df156c6a0a89ed2a3bd4a473c68cf85907509ca0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
