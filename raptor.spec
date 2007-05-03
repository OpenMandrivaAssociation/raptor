%define name    raptor
%define version 1.4.15
%define release %mkrel 1

%define major	1
%define libname %mklibname %{name} %{major}

Summary:   	Raptor RDF Parser Toolkit for Redland
Name:      	%{name}
Version:   	%{version}
Release:   	%{release}
License: 	GPL LGPL
Group:     	Development/Other
Source:    	http://librdf.org/dist/source/%{name}-%{version}.tar.bz2
URL:       	http://www.redland.opensource.ac.uk/raptor/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	libxml2-devel
BuildRequires:  curl-devel

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package -n	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{libname}-devel
Summary:	Header files and static libraries from %name
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	lib%{name}-devel = %{version}-%{release} %{name}-devel = %{version}-%{release} 
Obsoletes:	%{name}-devel

%description -n	%{libname}-devel
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_mandir}/man{1,3}
%makeinstall

#multiarch
%multiarch_binaries %{buildroot}%{_bindir}/raptor-config

%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING.LIB ChangeLog LICENSE.txt NEWS README
%{_mandir}/man1/rap*
%{_mandir}/man3/libraptor.3*
%{_bindir}/rapper

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files -n %libname-devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*
%_datadir/gtk-doc/html/raptor/
%multiarch %{multiarch_bindir}/raptor-config
%{_bindir}/raptor-config


