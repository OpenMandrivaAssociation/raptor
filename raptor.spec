%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	RDF Parser Toolkit for Redland
Name:		raptor
Version:	1.4.21
Release:	23
License:	GPLv2
Group:		Development/Other
Url:		https://librdf.org/raptor/
Source0:	http://librdf.org/dist/source/%{name}-%{version}.tar.gz
Patch0:		raptor-1.4.21-mdv_conf.diff
Patch1:		raptor-1.4.21-CVE-2012-0037.diff
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package -n	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
License:	LGPLv2

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{devname}
Summary:	Header files and static libraries from %name
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Conflicts:	%{name} < 1.4.21-3

%description -n	%{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x --disable-static
%make

%install
install -d %{buildroot}%{_mandir}/man{1,3}
%makeinstall

%files
%doc AUTHORS COPYING COPYING.LIB ChangeLog LICENSE.txt NEWS README
%{_mandir}/man1/rapper.1*
%{_mandir}/man3/libraptor.3*
%{_bindir}/rapper

%files -n %{libname}
%{_libdir}/libraptor.so.%{major}*

%files -n %{devname}
%{_bindir}/raptor-config
%{_libdir}/libraptor.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*
%{_datadir}/gtk-doc/html/raptor/
%{_mandir}/man1/raptor-config.1*

