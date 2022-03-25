#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which outputs Apple help books
Summary(pl.UTF-8):	Rozszerzenie Sphinksa zapisujące książki pomocy Apple
Name:		python3-sphinxcontrib-applehelp
Version:	1.0.2
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-applehelp/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-applehelp/sphinxcontrib-applehelp-%{version}.tar.gz
# Source0-md5:	3f2de7681e12dde031acee0497c3cc2b
URL:		https://pypi.org/project/sphinxcontrib-applehelp/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
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
%setup -q -n sphinxcontrib-applehelp-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/applehelp
%{py3_sitescriptdir}/sphinxcontrib_applehelp-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_applehelp-%{version}-py*-nspkg.pth
