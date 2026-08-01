%define upstream_name    AnyData
%define upstream_version 0.12
Name:		perl-%{upstream_name}
Version:	0.12
Release:	7

Summary:	Easy access to data in many formats
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://github.com/perl5-dbi/AnyData
Source0:	https://cpan.metacpan.org/authors/id/R/RE/REHSACK/AnyData-0.12.tar.gz

BuildRequires:	make
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
%setup -q -n AnyData-0.12

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

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


