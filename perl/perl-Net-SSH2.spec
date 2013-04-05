%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SSH2

Summary: Perl module that implements support for the SSH 2 protocol via libSSH2
Name: perl-Net-SSH2
Version: 0.45
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SSH2/

Source: http://search.cpan.org/CPAN/authors/id/R/RK/RKITOVER/Net-SSH2-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/Net/Net-SSH2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libssh2-devel
BuildRequires: openssl-devel
BuildRequires: perl >= 5.6.0
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: zlib-devel
Requires: libssh2
Requires: openssl
Requires: perl >= 5.6.0
Requires: zlib

#filter_from_requires /^perl*/d
#filter_setup

%description
perl-Net-SSH2 is a Perl module that implements support for the SSH 2 protocol
via libSSH2.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' Makefile.PL

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README example/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/SSH2/
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/SSH2/
%{perl_vendorarch}/Net/SSH2.pm

%changelog
* Mon Jul 30 2012 Jan Gehring <jan.gehring at, gmail.com> - 0.45-2
- Updated to release 0.45.

* Mon Jun 06 2011 Jan Gehring <jan.gehring at, gmail.com> - 0.38-1
- Updated to release 0.38.

* Thu Mar 31 2011 Jan Gehring <jan.gehring at, gmail.com> - 0.33-1
- Updated to release 0.33.

* Tue Jun 22 2010 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.28-1
- Updated to version 0.28.

* Thu Sep 10 2009 Christoph Maser <cmr@financial.com> - 0.27-1
- Updated to version 0.27.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.25-1
- Updated to version 0.25.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Updated to version 0.21.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Fri Sep 07 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
