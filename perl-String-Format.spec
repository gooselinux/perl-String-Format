Name:           perl-String-Format
Version:        1.15
Release:        2.1%{?dist}
Summary:        Sprintf-like string formatting capabilities with arbitrary format definitions

Group:          Development/Libraries
License:        GPLv2
URL:            http://search.cpan.org/dist/String-Format/
Source0:        http://www.cpan.org/authors/id/D/DA/DARREN/String-Format-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
String::Format lets you define arbitrary printf-like format sequences
to be expanded. This module would be most useful in configuration
files and reporting tools, where the results of a query need to be
formatted in a particular way.


%prep
%setup -q -n String-Format-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/String/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 1.15-2.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 27 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.15-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14-3
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14-2
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14-1.2
- add BR: perl(Test::More)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14-1.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sat Sep 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- First build.
