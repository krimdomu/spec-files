%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name common-sense

Summary: Perl Common Sense Module
Name: perl-common-sense
Version: 3.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/~mlehmann/common-sense-3.4/sense.pm.PL

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/common-sense-3.4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: x86_64
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
common::sense - save a tree AND a kitten, use common::sense!

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
%doc Changes MANIFEST README 
%doc %{_mandir}/*
%{perl_vendorlib}/*
%{perl_vendorarch}/*

%changelog
* Thu Aug 18 2011  Jan Gehring <jan.gehring, gmail.com> - 2.32-1
- inital package

