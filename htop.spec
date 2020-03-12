%define _without_docs	1

Summary:	interactive processes viewer
Name:		htop
Version:	2.2.0
Release:	1%{?dist}
License:	GPL
Source:		htop-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Requires:	ncurses

%description
Interactive process viewer

%prep
%setup -q

%build
./autogen.sh
%configure --prefix=%_prefix --sysconfdir=%_sysconfdir --mandir=%_mandir
%__make %_smp_mflags

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%__make %_smp_mflags DESTDIR=$RPM_BUILD_ROOT install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/*
%_datadir/*

%changelog
* Wed Mar 11 2020 Enrico Weigelt <info@metux.net>
- Packaging for SLES12
