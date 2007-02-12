Summary:	Flux is a survival-through-structure library
Summary(pl.UTF-8):   Flux - biblioteka struktur danych i operacji na nich
Name:		flux
Version:	0.4.1
Release:	6
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.copyleft.no/projects/fluxlib/%{name}-%{version}.tar.gz
# Source0-md5:	959cf209acfed3af40baf6a3bcd9c26b
Patch0:		%{name}-gethostbyname_is_in_libc_aka_no_libnsl.patch
Patch1:		%{name}-acinclude_fix.patch
Patch2:		%{name}-am15.patch
Patch3:		%{name}-AC_C_BIGENDIAN.patch
Patch4:		%{name}-gcc33.patch
Patch5:		%{name}-ltfix.patch
Patch6:		%{name}-errno.patch
URL:		http://www.fluxlib.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flux is a survival-through-structure library, whose goal is to reduce
the complexity of C programming. To this end, it supplies high-level
functions for manipulating data and communication with specialized
handles, masking typically tedious programming tasks. Common
instruction blocks are wrapped in higher-level calls with intuitive
names. In short: Do it once, do it right, then forget about it.

Abstracting things this way involves speed compromises. In Flux, these
should be minimal, and sometimes, when superiour algorithms are easily
accessible, efficiency is actually gained.

Another important goal is bridging gaps between typical tasks - like
parsing, storage, retrieval, buffering and transfer, data structures -
like generic tree structures, generic network structures, XML and
presentation formats, and protocols - like FluxComm, Unix protocols
and IRC. (Note: IRC protocols are hairy and ill-defined. Unification
and masking is particularly useful here).

%description -l pl.UTF-8
Flux jest biblioteką typu "survival-through-structure", której celem
jest redukcja złożoności programowania w C. W tym celu zaprojektowano
funkcje wysokiego poziomu służące manipulacji danymi i komunikacji z
wyspecjalizowanymi uchwytami, ukrywając nużące zazwyczaj zadania
programistyczne. Popularne bloki instrukcji są zawinięte w wywołaniach
wyższego poziomu o intuicyjnych nazwach. Mówiąc krótko: Zrób to raz,
zrób to dobrze i zapomnij o tym. Takie wyabstrahowywanie wymaga wielu
kompromisów. We Fluksie powinny być one ograniczone do minimum, czasem
zaś, kiedy łatwo jest użyć lepszych algorytmów, zyskuje się na
wydajności. Inną ważną rzeczą jest stworzenie pomostu między typowymi
zadaniami (parsowanie, przechowywanie, wydobywanie, buforowanie i
transfer), strukturami danych (generyczne struktury drzew, generyczne
struktury sieci XML i formaty prezentacyjne) a protokołami (FluxComm,
protokoły uniksowe i IRC. Uwaga: protokoły ircowe są niezgrabne i źle
zdefiniowane. Szczególnie w tym wypadku unifikacja i maskowanie
ukazują swoja wartość).

%package devel
Summary:	Header files and development documentation for flux
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do flux
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for flux.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do biblioteki flux.

%package static
Summary:	Static flux libraries
Summary(pl.UTF-8):   Biblioteki statyczne flux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static flux libraries.

%description static -l pl.UTF-8
Biblioteki statyczne flux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
echo n | %{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS README NEWS TODO doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
