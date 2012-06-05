#
# Conditional build:
%bcond_with	tests		# perform "make test" (requires DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Clutter
Summary:	Clutter - Perl bindings for the Clutter 1.x API
Summary(pl.UTF-8):	Clutter - wiązania Perla do API biblioteki Clutter 1.x
Name:		perl-Clutter
Version:	1.110
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/E/EB/EBASSI/Clutter-%{version}.tar.gz
# Source0-md5:	0bfc0a9463daf8ce25a84b54d01781c0
URL:		http://search.cpan.org/dist/Clutter/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Cairo-GObject >= 1.000
BuildRequires:	perl-Glib >= 1.253
BuildRequires:	perl-Glib-Object-Introspection >= 0.002
BuildRequires:	perl-Pango >= 1.220
%endif
Requires:	perl-Cairo-GObject >= 1.000
Requires:	perl-Glib >= 1.253
Requires:	perl-Glib-Object-Introspection >= 0.002
Requires:	perl-Pango >= 1.220
# clutter with gobject binding
Requires:	clutter >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to use the Clutter library from Perl to create
dynamic, compelling, and portable graphical user interfaces, using a
Perlish and object oriented API.

%description -l pl.UTF-8
Ten moduł pozwala na wykorzystywanie biblioteki Clutter z poziomu
Perla w celu tworzenia dynamicznych, przenośnych graficznych
interfejsów użytkownika przy użyciu perlowego, zorientowanego
obiektowo API.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Clutter.pm
%{_mandir}/man3/Clutter.3pm*
%{_examplesdir}/%{name}-%{version}
