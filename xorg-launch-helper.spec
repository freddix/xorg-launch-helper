Summary:	Xorg wrapper
Name:		xorg-launch-helper
Version:	4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://foo-projects.org/~sofar/xorg-launch-helper/%{name}-%{version}.tar.gz
# Source0-md5:	074e81a0817e460e1fefa738ee9c3cbb
Source1:	xsession@.service
BuildRequires:	pkg-config
BuildRequires:	systemd-devel
Requires:	systemd
Requires:	xorg-xserver-server
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

install -D %{SOURCE1} $RPM_BUILD_ROOT%{systemdunitdir}/xsession@.service

# run as a system service
mv $RPM_BUILD_ROOT%{_prefix}/lib/systemd/user/xorg.service \
	$RPM_BUILD_ROOT%{systemdunitdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{systemdunitdir}/xorg.service
%{systemdunitdir}/xsession@.service

