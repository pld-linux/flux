Summary:	Flux is a survival-through-structure library
Name:		flux
Version:	0.4.1
Release:	1
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
License:	GPL
Source0:	ftp://ftp.styx.net/projects/flux/%{name}-%{version}.tar.gz
URL:		http://projects.simplemente.net/flux/
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
Flux jest bibliotek± typu "", której celem jest redukcja z³o¿ono¶ci
programowania w C. W tym celu zaprojektowano funkcje wysokiego poziomu
s³u¿±ce manipulacji danymi i komunikacji z wyspecjalizowanymi
uchwytami, ukrywaj±c nu¿±ce zazwyczaj zadania programistyczne.
Popularne bloki instrukcji s± zawiniête w wywo³aniach wy¿szego poziomu
o intuicyjnych nazwach. Mówi±c krótko: Zrób to raz, zrób to dobrze i
zapomnij o tym. Takie wyabstrahowywanie wymaga wielu kompromisów. We
Fluksie powinny byæ one ograniczone do minimum, czasem za¶, kiedy
³atwo jest u¿yæ lepszych algorytmów, zyskuje siê na wydajno¶ci. Inn±
wa¿n± rzecz± jest stworzenie pomostu miêdzy typowymi zadaniami
(parsowanie, przechowywanie, wydobywanie, buforowanie i transfer),
strukturami danych (generyczne struktury drzew, generyczne struktury
sieci XML i formaty prezentacyjne) a protoko³ami (FluxComm, protoko³y
uniksowe i IRC. Uwaga: protoko³y ircowe s± niezgrabne i ¼le
zdefiniowane. Szczególnie w tym wypadku unifikacja i maskowanie
ukazuj± swoja warto¶æ).

%package devel
Summary:	Header files and development documentation for flux
Summary(pl):	Pliki nag³ówkowe i dokumentacja do flux
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for flux.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do biblioteki flux.

%package static
Summary:	Static flux libraries
Summary(pl):	Biblioteki statyczne flux
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static flux libraries.

%description -l pl static
Biblioteki statyczne flux.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
echo n | make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS README NEWS TODO 

%find_lang %{name}

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
