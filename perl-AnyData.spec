%define real_name AnyData

Summary:	Easy access to data in many formats
Name:		perl-%{real_name}
Version:	0.10
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JZ/JZUCKER/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/AnyData
%dir %{perl_vendorlib}/AnyData/Storage
%dir %{perl_vendorlib}/AnyData/Format
%{perl_vendorlib}/AnyData/Storage/*
%{perl_vendorlib}/AnyData/Format/*
%{perl_vendorlib}/*.pm
%{_mandir}/*/*
