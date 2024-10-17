%define name	freedups
%define	version	0.6.14
%define release	7

Summary:	Hardlinks identical files to save space
Name:		%{name}	
Version:	%{version}
Release:	%{release}	
License:	GPL
Group:		File tools
URL:		https://www.stearns.org/freedups/
Source:		http://www.stearns.org/freedups/%{name}-%{version}.tar.bz2
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}--buildroot

%description
Freedups hardlinks identical files to save space.  For files that are
generally read from and not written to, this can provide a 
significant space savings with no performance degredation.  In fact,
in a small number of cases, this can speed up the system.


%prep
%setup

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -m755 %{name}.pl $RPM_BUILD_ROOT%{_bindir}/%{name}

						
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/%{name}




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.14-6mdv2011.0
+ Revision: 618340
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.6.14-5mdv2010.0
+ Revision: 428885
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6.14-4mdv2009.0
+ Revision: 245363
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.14-2mdv2008.1
+ Revision: 136419
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Emmanuel Andry <eandry@mandriva.org> 0.6.14-2mdv2007.0
+ Revision: 108754
- add source URL
- Import freedups

* Fri Apr 07 2006 Lenny Cartier <lenny@mandriva.com> 0.6.14-1mdk
- 0.6.14

