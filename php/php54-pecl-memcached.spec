%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PECL package to use the memcached distributed caching system
Name: php54-pecl-memcached
Version: 2.1.0
Release: 1%{?dist}
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/memcached
Source: http://pecl.php.net/get/memcached-2.1.0.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php54, libmemcached
BuildRequires: php54, php54-devel, zlib-devel, openssl-devel, libmemcached-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool

Provides: php54-pecl(memcached) = %{version}-%{release}

%description
Memcached is a caching daemon designed especially for dynamic web applications
to decrease database load by storing objects in memory.  This extension allows
you to work with memcached through handy OO and procedural interfaces.


%prep
%setup -q -n memcached-%{version}


%build
# Workaround for broken old phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/memcached.ini << 'EOF'
; Enable memcache extension module
extension=memcached.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CREDITS README
%config(noreplace) %{_sysconfdir}/php.d/memcached.ini
%{php_extdir}/memcached.so


%changelog
* Wed Apr 10 2013 Jan Gehring <jan.gehring@inovex.de> - 2.1.0-1
- added package
