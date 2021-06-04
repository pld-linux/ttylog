Summary:	Serial port logger
Name:		ttylog
Version:	0.31
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://downloads.sourceforge.net/ttylog/%{name}-%{version}.tar.gz
# Source0-md5:	00721be52a9f61c951065f932c41f16a
Patch0:		%{name}-more_bauds.patch
URL:		https://ttylog.sourceforge.net/
BuildRequires:	cmake >= 2.8
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Print everything that comes from a serial device to stdout. The device
as well as the baud rate can be specified and a timeout can be set
instead of just killing the process in order to stop it.

%prep
%setup -q
%patch0 -p1

%build
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md TODO
%attr(755,root,root) %{_sbindir}/ttylog
%{_mandir}/man8/ttylog.8*
