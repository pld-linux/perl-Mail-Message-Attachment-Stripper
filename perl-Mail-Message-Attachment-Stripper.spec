#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Message-Attachment-Stripper
Summary:	Mail::Message::Attachment::Stripper - strip the attachments from a mail
Summary(pl.UTF-8):   Mail::Message::Attachment::Stripper - wycinanie załączników z poczty
Name:		perl-Mail-Message-Attachment-Stripper
Version:	1.0
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b61fe2db5261dbd6757899bc5deb849c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Mail-Box >= 2.050
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Given a Mail::Message object, detach all attachments from the message.
These are then available separately.

%description -l pl.UTF-8
Po przekazaniu obiektu Mail::Message, klasa odłącza z listu wszystkie
załączniki. Są one później dostępne osobno.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Mail/Message/Attachment/*.pm
%{_mandir}/man3/*
