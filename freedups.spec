%define name	freedups
%define	version	0.6.14
%define release	%mkrel 6

Summary:	Hardlinks identical files to save space
Name:		%{name}	
Version:	%{version}
Release:	%{release}	
License:	GPL
Group:		File tools
URL:		http://www.stearns.org/freedups/
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


