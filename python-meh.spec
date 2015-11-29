#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		libreportver 2.0.18-1
%define 	module	meh
Summary:	A python library for handling exceptions
Name:		python-%{module}
Version:	0.24
Release:	1
License:	GPL v2+
# This is a Red Hat maintained package which is specific to
# it's distribution. Thus the source is only available from
# within this srpm.
# This tarball was created from upstream git:
#   git clone git://git.fedoraproject.org/git/python-meh.git
#   cd python-meh && make archive
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/python-meh/%{name}-%{version}.tar.gz/b1ee671f891a970dfd92a541a6b23cbc/python-%{module}-%{version}.tar.gz
# Source0-md5:	b1ee671f891a970dfd92a541a6b23cbc
Group:		Libraries
URL:		http://git.fedorahosted.org/git/?p=python-meh.git
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libreport-cli >= %{libreportver}
BuildRequires:	libreport-gtk >= %{libreportver}
BuildRequires:	python-dbus
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	gtk+3
Requires:	libreport-cli >= %{libreportver}
Requires:	libreport-gtk >= %{libreportver}
Requires:	openssh-clients
Requires:	python
Requires:	python-dbus
Requires:	python-libreport >= %{libreportver}
Requires:	python-pygobject3
Requires:	python-rpm
Requires:	yum
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The python-meh package is a Python library for handling, saving, and
reporting exceptions.

%prep
%setup -q

%build
%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# redo python install to get optimize=2
%py_install

%py_postclean
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%{py_sitescriptdir}/meh
%{py_sitescriptdir}/python_meh-%{version}-py*.egg-info
%{_datadir}/%{name}
