%define real_name CGI-Panel

Summary:	CGI-Panel module for perl 
Name:		perl-%{real_name}
Version:	0.97
Release: %mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl(Apache::Session)
BuildRequires:  perl(CGI)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CGI::Panel allows applications to be built out of simple object-based
components. It'll handle the state of your data and objects so you can
write a web application just like a desktop app. You can forget about
the http requests and responses, whether we're getting or posting, and
all that stuff because that is all handled for you leaving to you
interact with a simple API.

%prep
%setup -q -n %{real_name}-%{version} 
find . -type d -name CVS -exec rm -rf {} \; || :

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes demo LICENSE README TODO
%{perl_vendorlib}/CGI/Panel
%{perl_vendorlib}/CGI/Panel.pm
%{_mandir}/*/*




