#
Summary:	hdup backup utility
Name:		hdup
Version:	2.0.14
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.miek.nl/projects/hdup2/%{name}.tar.bz2
# Source0-md5:	7795ac9dd5a1ae40d330a54b6a6e91a3
URL:		http://miek.nl/projects/hdup2/index.html
BuildRequires: glib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hdup2 is a backup utilty, it's aim is to make backup really simple.
The backup scheduling is done by means of a cronjob. Is supports a
include/exclude mechanism, remote backups, encrypted backups and split
backups (called chunks) to allow easy burning to CD/DVD.


%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/hdup/hdup.conf
%{_sysconfdir}/hdup/postrun-warn-user
%attr(755,root,root) %{_sbindir}/hdup
%{_mandir}/man1/hdup.1*
%{_mandir}/man5/hdup.conf.5*
