%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Header
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - OO-Interface to modify HTTP-Headers easily
Summary(pl.UTF-8):	%{_pearname} - Obiektowy interfejs do modyfikowania nagłówków HTTP
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	68e0a84fb3aca46e6e0a6ccfe25c2d6b
URL:		http://pear.php.net/package/HTTP_Header/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-HTTP >= 1.3.1
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides methods to set/modify HTTP-Headers. To abstract
common things, like caching etc. some sub classes are provided that
handle special cases (i.e. HTTP_Header_Cache).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa udostępnia metody do ustawiania/modyfikowania nagłówków HTTP.
Aby wyabstrahować wspólne elementy, takie jak buforowanie itp.,
zostało udostępnionych trochę podklas obsługujących specjalne
przypadki (np. HTTP_Header_Cache).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
