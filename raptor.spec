%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:   	Raptor RDF Parser Toolkit for Redland
Name:      	raptor
Version:   	1.4.21
Release:   	6
License: 	GPL LGPL
Group:     	Development/Other
URL:       	http://librdf.org/raptor/
Source0:	http://librdf.org/dist/source/%{name}-%{version}.tar.gz
Patch0:		raptor-1.4.21-mdv_conf.diff
Patch1:		raptor-1.4.21-CVE-2012-0037.diff
BuildRequires: 	libxml2-devel
BuildRequires:  curl-devel
Requires:	%{libname} >= %{version}

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package -n	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary:	Header files and static libraries from %name
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes:	%{name}-devel < %{version}-%{release}
Obsoletes:	%{mklibname -d raptor 1}
Conflicts:	%{name} < 1.4.21-3

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep

%setup -q
%patch0 -p0
%patch1 -p1 -b .CVE-2012-0037

%build
%configure2_5x
%make

%install

install -d %{buildroot}%{_mandir}/man{1,3}
%makeinstall

rm -f %{buildroot}%{_libdir}/*.*a

%files
%doc AUTHORS COPYING COPYING.LIB ChangeLog LICENSE.txt NEWS README
%{_mandir}/man1/rapper.1*
%{_mandir}/man3/libraptor.3*
%{_bindir}/rapper

%files -n %libname
%{_libdir}/lib*.so.%{major}*

%files -n %develname
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*
%_datadir/gtk-doc/html/raptor/
%{_bindir}/raptor-config
%{_mandir}/man1/raptor-config.1*
