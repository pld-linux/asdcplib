# TODO: python (missing sources, specified as nodist???)
Summary:	The ASDCP library
Summary(pl.UTF-8):	Biblioteka ASDCP
Name:		asdcplib
Version:	2.7.19
Release:	2
License:	BSD
Group:		Libraries
# note: download URL shows more recent versions than document at download directory
#Source0Download: http://www.cinecert.com/asdcplib/download/
Source0:	http://download.cinecert.com/asdcplib/%{name}-%{version}.tar.gz
# Source0-md5:	f9290440d1645cc834cfb9fb5a337348
# from asdcplib 1.12.60 sources
Source1:	%{name}.pc.in
Patch0:		%{name}-link.patch
URL:		http://www.cinecert.com/asdcplib/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	expat-devel >= 1.95
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7
#BuildRequires:	python-devel >= 1:2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The asdcplib library is a set of objects that offer simplified access
to files conforming to the sound and picture track file formats
developed by the SMPTE Working Group DC28.20 (now TC 21DC).

%description -l pl.UTF-8
Biblioteka asdcplib to zbiór obiektów oferujących uproszczony dostęp
do plików zgodnych z formatami plików ścieżek dźwięku i obrazu
opracowanych przez grupę roboczą SMPTE DC28.20 (obecnie TC 21DC).

%package devel
Summary:	Header files for ASDCP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ASDCP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel >= 0.9.7

%description devel
Header files for ASDCP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ASDCP.

%package static
Summary:	Static ASDCP libraries
Summary(pl.UTF-8):	Statyczne biblioteki ASDCP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ASDCP libraries.

%description static -l pl.UTF-8
Statyczne biblioteki ASDCP.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--with-expat=/usr \
	--with-openssl=/usr \
	--enable-as-02 \
	--enable-phdr
#	--with-python is broken (required files missing in tarball)

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
sed -e 's,@prefix@,%{_prefix},;s,@exec_prefix@,%{_prefix},;s,@libdir@,%{_libdir},;s,@includedir@,%{_includedir},;s,@PACKAGE_VERSION@,%{version},' %{SOURCE1} >$RPM_BUILD_ROOT%{_pkgconfigdir}/asdcplib.pc

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/as-02-info
%attr(755,root,root) %{_bindir}/as-02-unwrap
%attr(755,root,root) %{_bindir}/as-02-wrap
%attr(755,root,root) %{_bindir}/asdcp-info
%attr(755,root,root) %{_bindir}/asdcp-test
%attr(755,root,root) %{_bindir}/asdcp-unwrap
%attr(755,root,root) %{_bindir}/asdcp-util
%attr(755,root,root) %{_bindir}/asdcp-wrap
%attr(755,root,root) %{_bindir}/blackwave
%attr(755,root,root) %{_bindir}/j2c-test
%attr(755,root,root) %{_bindir}/klvsplit
%attr(755,root,root) %{_bindir}/klvwalk
%attr(755,root,root) %{_bindir}/kmfilegen
%attr(755,root,root) %{_bindir}/kmrandgen
%attr(755,root,root) %{_bindir}/kmuuidgen
%attr(755,root,root) %{_bindir}/wavesplit
%attr(755,root,root) %{_bindir}/phdr-unwrap
%attr(755,root,root) %{_bindir}/phdr-wrap
%attr(755,root,root) %{_bindir}/pinkwave
%attr(755,root,root) %{_libdir}/libas02-%{version}.so
%attr(755,root,root) %{_libdir}/libasdcp-%{version}.so
%attr(755,root,root) %{_libdir}/libkumu-%{version}.so
%attr(755,root,root) %{_libdir}/libphdr-%{version}.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libas02.so
%attr(755,root,root) %{_libdir}/libasdcp.so
%attr(755,root,root) %{_libdir}/libkumu.so
%attr(755,root,root) %{_libdir}/libphdr.so
%{_includedir}/AS_02.h
%{_includedir}/AS_02_PHDR.h
%{_includedir}/AS_DCP.h
%{_includedir}/KM_*.h
%{_pkgconfigdir}/asdcplib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libas02.a
%{_libdir}/libasdcp.a
%{_libdir}/libkumu.a
%{_libdir}/libphdr.a
