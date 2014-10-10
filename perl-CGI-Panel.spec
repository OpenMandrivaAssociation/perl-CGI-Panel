%define upstream_name    CGI-Panel
%define upstream_version 0.97

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	CGI-Panel module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Apache::Session)
BuildRequires:	perl(CGI)
BuildArch:	noarch

%description
CGI::Panel allows applications to be built out of simple object-based
components. It'll handle the state of your data and objects so you can
write a web application just like a desktop app. You can forget about
the http requests and responses, whether we're getting or posting, and
all that stuff because that is all handled for you leaving to you
interact with a simple API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find . -type d -name CVS -exec rm -rf {} \; || :

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes demo LICENSE README TODO
%{perl_vendorlib}/CGI/Panel
%{perl_vendorlib}/CGI/Panel.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.970.0-2mdv2011.0
+ Revision: 680692
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.970.0-1mdv2011.0
+ Revision: 403000
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.97-5mdv2009.0
+ Revision: 255778
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.97-3mdv2008.1
+ Revision: 136906
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.97-2mdv2007.0
+ Revision: 73389
- import perl-CGI-Panel-0.97-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.97-2mdk
- Fix SPEC Using perl Policies
	- BuildRequires
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.97-1mdk
- initial Mandriva package

