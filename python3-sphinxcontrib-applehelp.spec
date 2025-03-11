#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which outputs Apple help books
Summary(pl.UTF-8):	Rozszerzenie Sphinksa zapisujące książki pomocy Apple
Name:		python3-sphinxcontrib-applehelp
Version:	2.0.0
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-applehelp/
Source0:	https://pypi.debian.net/sphinxcontrib-applehelp/sphinxcontrib_applehelp-%{version}.tar.gz
# Source0-md5:	e16bb1d6199f686d411c180e64a8e831
URL:		https://pypi.org/project/sphinxcontrib-applehelp/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-build
BuildRequires:	python3-installer
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-applehelp is a sphinx extension which outputs
Apple help books.

%description -l pl.UTF-8
sphinxcontrib-applehelp to rozszerzenie Sphinksa, zapisujące
książki pomocy Apple.

%prep
%setup -q -n sphinxcontrib_applehelp-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENCE.rst README.rst
%{py3_sitescriptdir}/sphinxcontrib/applehelp
%{py3_sitescriptdir}/sphinxcontrib_applehelp-%{version}.dist-info
