%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-XS

Summary: JSON Module for Perl
Name: perl-JSON-XS
Version: 2.32
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/~mlehmann/JSON-XS-2.32/XS.pm

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/JSON-XS-2.32.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: x86_64
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Provides: perl(JSON::XS)

%description
JSON serialising/deserialising, done correctly and fast

%prep
%setup -n %{real_name}-%{version}

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
%doc %{_mandir}/*
#%{perl_vendorlib}/*
%{perl_vendorarch}/*
/usr/bin/json_xs
#/usr/lib64/perl5/vendor_perl/5.8.8/x86_64-linux-thread-multi/JSON/XS.pm
#/usr/lib64/perl5/vendor_perl/5.8.8/x86_64-linux-thread-multi/JSON/XS/Boolean.pm
#/usr/lib64/perl5/vendor_perl/5.8.8/x86_64-linux-thread-multi/auto/JSON/XS/XS.bs
#/usr/lib64/perl5/vendor_perl/5.8.8/x86_64-linux-thread-multi/auto/JSON/XS/XS.so

%changelog
* Thu Aug 18 2011  Jan Gehring <jan.gehring, gmail.com> - 2.32-1
- inital package

