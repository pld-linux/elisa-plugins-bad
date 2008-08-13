Summary:	"Bad" plugins for elisa
Summary(pl.UTF-8):	"Z³e" wtyczki dla elisy
Name:		elisa-plugins-bad
Version:	0.5.5
Release:	0.1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/elisa/%{name}-%{version}.tar.gz
# Source0-md5:	43b6c26f70b4065f05dd5e637f4700ad
URL:		http://www.fluendo.com/elisa/
BuildRequires:	elisa = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Bad" plugins for elisa

%description -l pl.UTF-8
"Z³e" wtyczki dla elisy


%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.pth
%{py_sitescriptdir}/elisa/plugins/*
