Summary:	Flux is a survival-through-structure library
Summary(pl):	Flux - biblioteka struktur danych i operacji na nich
Name:		flux
Version:	0.4.1
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.styx.net/projects/flux/%{name}-%{version}.tar.gz
Patch0:		%{name}-gethostbyname_is_in_libc_aka_no_libnsl.patch
URL:		http://projects.simplemente.net/flux/
BuildRequires:	autoconf
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

%description -l pl
Flux jest bibliotek± typu "survival-through-structure", ktÛrej celem
jest redukcja z≥oøono∂ci programowania w C. W tym celu zaprojektowano
funkcje wysokiego poziomu s≥uø±ce manipulacji danymi i komunikacji z
wyspecjalizowanymi uchwytami, ukrywaj±c nuø±ce zazwyczaj zadania
programistyczne. Popularne bloki instrukcji s± zawiniÍte w wywo≥aniach
wyøszego poziomu o intuicyjnych nazwach. MÛwi±c krÛtko: ZrÛb to raz,
zrÛb to dobrze i zapomnij o tym. Takie wyabstrahowywanie wymaga wielu
kompromisÛw. We Fluksie powinny byÊ one ograniczone do minimum, czasem
za∂, kiedy ≥atwo jest uøyÊ lepszych algorytmÛw, zyskuje siÍ na
wydajno∂ci. Inn± waøn± rzecz± jest stworzenie pomostu miÍdzy typowymi
zadaniami (parsowanie, przechowywanie, wydobywanie, buforowanie i
transfer), strukturami danych (generyczne struktury drzew, generyczne
struktury sieci XML i formaty prezentacyjne) a protoko≥ami (FluxComm,
protoko≥y uniksowe i IRC. Uwaga: protoko≥y ircowe s± niezgrabne i ºle
zdefiniowane. SzczegÛlnie w tym wypadku unifikacja i maskowanie
ukazuj± swoja warto∂Ê).

%package devel
Summary:	Header files and development documentation for flux
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja do flux
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for flux.

%description -l pl devel
Pliki nag≥Ûwkowe i dokumentacja do biblioteki flux.

%package static
Summary:	Static flux libraries
Summary(pl):	Biblioteki statyczne flux
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static flux libraries.

%description -l pl static
Biblioteki statyczne flux.

%prep
%setup -q

%build
#autoconf
%configure2_13
echo n | make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS README NEWS TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
