%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:   	RDF Parser Toolkit for Redland
Name:      	raptor
Version:   	1.4.21
Release:   	16
License: 	GPL LGPL
Group:     	Development/Other
URL:       	http://librdf.org/raptor/
Source0:	http://librdf.org/dist/source/%{name}-%{version}.tar.gz
Patch0:		raptor-1.4.21-mdv_conf.diff
Patch1:		raptor-1.4.21-CVE-2012-0037.diff
BuildRequires: 	pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libcurl)
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


%changelog
* Mon Apr 23 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4.21-6
+ Revision: 792770
- sync with MDVSA-2012:061
- cleanup the raptor-config file
- various fixes

* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.21-5
+ Revision: 686322
- avoid pulling 32 bit libraries on 64 bit arch

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.21-4
+ Revision: 661744
- multiarch fixes

* Wed Apr 20 2011 Funda Wang <fwang@mandriva.org> 1.4.21-3
+ Revision: 656103
- move raptor-config manpage into devel package

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.21-2mdv2011.0
+ Revision: 607310
- rebuild

* Mon Feb 22 2010 Emmanuel Andry <eandry@mandriva.org> 1.4.21-1mdv2010.1
+ Revision: 509783
- New version 1.4.21

* Fri Jan 01 2010 Emmanuel Andry <eandry@mandriva.org> 1.4.20-1mdv2010.1
+ Revision: 484722
- New version 1.4.20

* Wed Jul 29 2009 Emmanuel Andry <eandry@mandriva.org> 1.4.19-1mdv2010.0
+ Revision: 404066
- New version 1.4.19
- check major

* Wed Sep 03 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.4.18-3mdv2009.0
+ Revision: 279865
- add Requires (Bug #43472)

* Fri Jun 27 2008 Funda Wang <fwang@mandriva.org> 1.4.18-2mdv2009.0
+ Revision: 229465
- New devel package policy

* Fri Jun 27 2008 Funda Wang <fwang@mandriva.org> 1.4.18-1mdv2009.0
+ Revision: 229457
- update to new version 1.4.18

* Fri Jun 20 2008 Austin Acton <austin@mandriva.org> 1.4.17-1mdv2009.0
+ Revision: 227340
- new version
- fix URL

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4.16-2mdv2009.0
+ Revision: 225310
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 16 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.4.16-1mdv2008.1
+ Revision: 98763
- New version 1.4.16

* Thu May 03 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.4.15-1mdv2008.0
+ Revision: 21359
- New version 1.4.15


* Sat Jan 06 2007 Crispin Boylan <crisb@mandriva.org> 1.4.13-1mdv2007.0
+ Revision: 104783
- New version
- Import raptor

* Wed Apr 26 2006 Austin Acton <austin@mandriva.org> 1.4.9-1mdk
- New release 1.4.9

* Wed Jan 04 2006 Austin Acton <austin@mandriva.org> 1.4.8-1mdk
- New release 1.4.8

* Fri Nov 18 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.7-2mdk
- rebuilt against openssl-0.9.8a

* Fri Jun 10 2005 Austin Acton <austin@mandriva.org> 1.4.7-1mdk
- New release 1.4.7

* Wed Mar 23 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4.5-2mdk
- multiarch
- update license, only libraries are LGPL, while the rest is GPL

* Sun Feb 06 2005 Austin Acton <austin@mandrake.org> 1.4.5-1mdk
- 1.4.5

* Tue Jan 04 2005 Austin Acton <austin@mandrake.org> 1.4.3-1mdk
- 1.4.3

* Wed Dec 29 2004 Austin Acton <austin@mandrake.org> 1.4.2-2mdk
- rebuild

* Mon Nov 29 2004 Austin Acton <austin@mandrake.org> 1.4.2-1mdk
- 1.4.2
- source URL

* Sat Oct 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.4.1-1mdk
- 1.4.1

* Wed Oct 27 2004 Austin Acton <austin@mandrake.org> 1.4.0-1mdk
- 1.4.0
- configure 2.5

* Sat Jul 03 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.3.1-2mdk
- Rebuild for new curl

* Wed Jun 30 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.3.1-1mdk
- 1.3.1
- do parallel build
- reenable libtoolize

* Thu May 20 2004 Austin Acton <austin@mandrake.org> 1.3.0-1mdk
- 1.3.0

* Mon Feb 02 2004 Austin Acton <austin@mandrake.org> 1.2.0-1mdk
- 1.2.0

