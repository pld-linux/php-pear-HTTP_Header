%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Header
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - OO-Interface to modify HTTP-Headers easily
Summary(pl):	%{_pearname} - Obiektowy interfejs do modyfikowania nag��wk�w HTTP
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	9aa028af8e7017f9c4346da9b8847897
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://opensource.visionp.de/modules/project/HTTP_Header.php
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Requires:	php-pear-HTTP >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides methods to set/modify HTTP-Headers. To abstract
common things, like caching etc. some sub classes are provided that
handle special cases (i.e. HTTP_Header_Cache).

This class has in PEAR status: %{_status}.

%description -l pl
Ta klasa udost�pnia metody do ustawiania/modyfikowania nag��wk�w HTTP.
Aby wyabstrahowa� wsp�lne elementy, takie jak buforowanie itp.,
zosta�o udost�pnionych troch� podklas obs�uguj�cych specjalne
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
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
