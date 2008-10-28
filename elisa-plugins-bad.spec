Summary:	"Bad" plugins for elisa
Summary(pl.UTF-8):	"Złe" wtyczki dla elisy
Name:		elisa-plugins-bad
Version:	0.5.16
Release:	2
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	38b16c8fbc6f5aa8fb550bb94d157907
URL:		http://www.fluendo.com/elisa/
BuildRequires:	elisa = %{version}
Requires:	python-simplejson
Provides:	elisa-plugins = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Bad" plugins for elisa

%description -l pl.UTF-8
"Z?e" wtyczki dla elisy

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

#py_postclean

install elisa/plugins/amp/slave.py $RPM_BUILD_ROOT%{py_sitescriptdir}/elisa/plugins/amp/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.pth
%{py_sitescriptdir}/elisa/plugins/*
