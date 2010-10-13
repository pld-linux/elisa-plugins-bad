Summary:	"Bad" plugins for elisa
Summary(pl.UTF-8):	"Złe" wtyczki dla elisy
Name:		elisa-plugins-bad
Version:	0.5.31
Release:	3
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	1df4d3144b1d4999dfe471571aab71d8
URL:		http://www.fluendo.com/elisa/
BuildRequires:	elisa = %{version}
Requires:	python-simplejson
Provides:	elisa-plugins = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Bad" plugins for elisa

%description -l pl.UTF-8
"Złe" wtyczki dla elisy

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

#py_postclean

install -p elisa/plugins/amp/slave.py $RPM_BUILD_ROOT%{py_sitescriptdir}/elisa/plugins/amp/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.pth
%{py_sitescriptdir}/elisa/plugins/*
