%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Header
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - OO-Interface to modify HTTP-Headers easily
Summary(pl):	%{_pearname} - Obiektowy interfejs do modyfikowania nag³ówków HTTP
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5aba41157f1c63d2c84c3660c9221d17
URL:		http://pear.php.net/package/HTTP_Header/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Requires:	php-pear-HTTP >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides methods to set/modify HTTP-Headers. To abstract
common things, like caching etc. some sub classes are provided that
handle special cases (i.e. HTTP_Header_Cache).

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa udostêpnia metody do ustawiania/modyfikowania nag³ówków HTTP.
Aby wyabstrahowaæ wspólne elementy, takie jak buforowanie itp.,
zosta³o udostêpnionych trochê podklas obs³uguj±cych specjalne
przypadki (np. HTTP_Header_Cache).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
