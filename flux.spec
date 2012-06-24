Summary:	Flux is a survival-through-structure library
Name:		flux
Version:	0.3.0
Release:	1
Group:		Libraries
Group(pl):	Biblioteki
Copyright:	GPL
Source:		ftp://ftp.styx.net/projects/flux/%{name}-%{version}.tar.gz
URL:		http://projects.simplemente.net/flux/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Flux is a survival-through-structure library, whose goal is to reduce the
complexity of C programming. To this end, it supplies high-level functions
for manipulating data and communication with specialized handles, masking
typically tedious programming tasks. Common instruction blocks are wrapped
in higher-level calls with intuitive names. In short: Do it once, do it
right, then forget about it.

Abstracting things this way involves speed compromises. In Flux, these
should be minimal, and sometimes, when superiour algorithms are easily
accessible, efficiency is actually gained.

Another important goal is bridging gaps between typical tasks - like
parsing, storage, retrieval, buffering and transfer, data structures - like
generic tree structures, generic network structures, XML and presentation
formats, and protocols - like FluxComm, Unix protocols and IRC. (Note: IRC
protocols are hairy and ill-defined. Unification and masking is particularly
useful here).

%package devel
Summary:	Header files and development documentation for flux
Summary(pl):	Pliki nag��wkowe i dokumentacja do flux
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for flux.

%description -l pl devel
Pliki nag��wkowe i dokumentacja do biblioteki flux.

%package static
Summary:	Static flux libraries
Summary(pl):	Biblioteki statyczne flux
Group:		Development/Libraries
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

make install DESTDIR=$RPM_BUILD_ROOT

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
%attr(644,root,root) %{_libdir}/lib*.a

%changelog
