Summary:	hdup backup utility
Summary(pl):	hdup - narzêdzie do kopii zapasowych
Name:		hdup
Version:	2.0.14
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.miek.nl/projects/hdup2/%{name}.tar.bz2
# Source0-md5:	7795ac9dd5a1ae40d330a54b6a6e91a3
URL:		http://miek.nl/projects/hdup2/index.html
BuildRequires:	glib2-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hdup2 is a backup utility, its aim is to make backup really simple.
The backup scheduling is done by means of a cronjob. Is supports a
include/exclude mechanism, remote backups, encrypted backups and split
backups (called chunks) to allow easy burning to CD/DVD.

%description -l pl
hdup2 to narzêdzie do wykonywania kopii zapasowych, którego celem jest
uczyniæ wykonywanie tego zadania naprawdê prostym. Kolejkowanie kopii
jest obs³ugiwane jako zadanie crona. hdup2 obs³uguje mechanizm
include/exclude, zdalne kopie, szyfrowanie kopii i dzielenie kopii na
czê¶ci, aby u³atwiæ wypalanie CD/DVD.

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
%dir %{_sysconfdir}/hdup
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hdup/hdup.conf
%{_sysconfdir}/hdup/postrun-warn-user
%attr(755,root,root) %{_sbindir}/hdup
%{_mandir}/man1/hdup.1*
%{_mandir}/man5/hdup.conf.5*
