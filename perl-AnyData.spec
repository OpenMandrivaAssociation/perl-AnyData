%define upstream_name    AnyData
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Easy access to data in many formats
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JZ/JZUCKER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The rather wacky idea behind this module and its sister module DBD::AnyData is
that any data, regardless of source or format should be accessible and
modifiable with the same simple set of methods. This module provides a
multi-dimensional tied hash interface to data in a dozen different formats. The
DBD::AnyData module adds a DBI/SQL interface for those same formats.

Both modules provide built-in protections including appropriate flocking() for
all I/O and (in most cases) record-at-a-time access to files rather than
slurping of entire files.

Currently supported formats include general format flatfiles (CSV, Fixed
Length, etc.), specific formats (passwd files, httpd logs, etc.), and a variety
of other kinds of formats (XML, Mp3, HTML tables). The number of supported
formats will continue to grow rapidly since there is an open API making it easy
for any author to create additional format parsers which can be plugged in to
AnyData itself and thereby be accessible by either the tiedhash or DBI/SQL
interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/AnyData
%dir %{perl_vendorlib}/AnyData/Storage
%dir %{perl_vendorlib}/AnyData/Format
%{perl_vendorlib}/AnyData/Storage/*
%{perl_vendorlib}/AnyData/Format/*
%{perl_vendorlib}/*.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 680450
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 402961
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 241144
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 14 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10-1mdv2008.0
+ Revision: 26654
- Import perl-AnyData



* Mon May 14 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10-1
- initial Mandriva package 
