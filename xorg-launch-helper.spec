Summary:	Xorg wrapper
Name:		xorg-launch-helper
Version:	3
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://foo-projects.org/~sofar/xorg-launch-helper/%{name}-%{version}.tar.gz
# Source0-md5:	6a9fdde4d4b28fc775d0828f793edd52
BuildRequires:	pkg-config
BuildRequires:	systemd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A wrapper in C to make XOrg function as a proper systemd unit.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
/usr/lib/systemd/user/xorg.*

