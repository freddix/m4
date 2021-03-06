# based on PLD Linux spec git://git.pld-linux.org/packages/.git
Summary:	GNU Macro Processor
Name:		m4
Version:	1.4.17
Release:	2
Epoch:		2
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/m4/%{name}-%{version}.tar.xz
# Source0-md5:	12a3c829301a4fd6586a57d3fcf196dc
URL:		http://www.gnu.org/software/m4/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	gmp-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GNU implementation of the traditional UNIX macro processor. M4 is
useful for writing text files which can be logically parsed, and is
used by many programs as part of their build process. M4 has built-in
functions for including files, running shell commands, doing
arithmetic, etc. The autoconf program needs m4 for generating
configure scripts, but not for running configure scripts.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	PACKAGE=m4 \
	--without-dmalloc
%{__make}

%check
%{__make} check tests

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/m4
%{_infodir}/*.info*
%{_mandir}/man1/*

