#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Clutter
Summary:	Clutter - Simple GL-based canvas library
Name:		perl-Clutter
Version:	1.002
Release:	2
License:	perl, lgpl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/E/EB/EBASSI/Clutter-%{version}.tar.gz
# Source0-md5:	a11bbe7a45a4f66c4015fd8b88c432b4
URL:		http://search.cpan.org/dist/Clutter/
BuildRequires:	clutter-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(ExtUtils::Depends) >= 0.300
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Pango) >= 1.140
BuildRequires:	perl-Cairo >= 1.000
BuildRequires:	perl-Glib >= 1.220
%endif
Requires:	clutter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clutter is a GObject based library for creating fast, visually rich
graphical user interfaces. It is intended for creating single window
heavily stylised applications such as media box UI's, presentations or
kiosk style programs in preference to regular 'desktop' style
applications.

Clutter's underlying graphics rendering is OpenGL (version 1.2+)
based. The clutter API is intended to be easy to use, attempting to
hide many of the GL complexities. It targets mainly 2D based graphics
and is definetly not intended to be a general interface for all OpenGL
functionality.

As well as OpenGL Clutter depends on and uses Glib, Glib::Object,
Pango and Cairo.

For more informations about Clutter, visit:

http://www.clutter-project.org

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{perl_vendorarch}/%{pdir}/
%{perl_vendorarch}/%{pdir}.pm
%{perl_vendorarch}/%{pdir}/*.pm
%{perl_vendorarch}/%{pdir}/*.pod
%dir %{perl_vendorarch}/%{pdir}/Behaviour
%dir %{perl_vendorarch}/%{pdir}/Cogl
%dir %{perl_vendorarch}/%{pdir}/Container
%dir %{perl_vendorarch}/%{pdir}/Event
%dir %{perl_vendorarch}/%{pdir}/Model
%dir %{perl_vendorarch}/%{pdir}/Path
%{perl_vendorarch}/%{pdir}/*/*.pod
%{perl_vendorarch}/%{pdir}/Install
%dir %{perl_vendorarch}/auto/%{pdir}/
%{perl_vendorarch}/auto/%{pdir}/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
