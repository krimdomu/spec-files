%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Parser-XS

Summary: a fast, primitive HTTP request parser  
Name: perl-HTTP-Parser-XS
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Parser-XS/

Packager: Jan Gehring <repo@rexify.org>
Vendor: Rexify Repository, http://rex.linux-files.org/

Source:	http://search.cpan.org/CPAN/authors/id/K/KA/KAZUHO/HTTP-Parser-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: x86_64
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
perl-HTTP-Parser-XS is a Perl module that implements an extensible,
general Perl server engine.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
#%{perl_vendorlib}/
/usr/lib64/perl5/vendor_perl/

%changelog
* Sat Jun 11 2011 Jan Gehring <repo@rexify.org> - 0.14-1
- inital spec file

