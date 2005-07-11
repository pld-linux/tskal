#
#TODO: sync pl and en description
# files needs fix
#
Summary:	Simple calendar which helps you to remember about important days
Summary(pl):	Prosty kalendarz pomagaj±cy pamiêtaæ o wa¿nych dniach
Name:		calendar
Version:	0.2
Release:	0.1
License:	GPL
Group:		X11/Applications
# Source0Download:	http://mike.oldfield.org.pl/tytus/index.html
Source0:	http://mike.oldfield.org.pl/tytus/prog/%{name}-%{version}.tgz
# Source0-md5:	614e6c5bd343cdf731ece14e19494274
URL:		http://mike.oldfield.org.pl/tytus/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calendar is simple and easy application which helps you to remember about
important days.

%description -l pl
Kalendarz jest prost±, opart± o biblioteki Qt aplikacj±, która
wy¶wietla kartki kalendarza u³o¿one w pasek. Dziêki temu, podobnie jak
to czyni± poborowi u¿ywaj±c centymetra, ju¿ na wiele dni wcze¶niej
³atwo zauwa¿yæ, ¿e co¶ siê zbli¿a (np. imieniny ¿ony) i mamy czas na
sensown± reakcjê (czyt. wybór i kupno prezentów i kwiatów).
Kalendarz obs³uguje skórki. Przyk³adowe mo¿na pobraæ z:
http://mike.oldfield.org.pl/tytus/prog/calendar_addons.tgz

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
# XXX: use _kdedocdir
%dir %{_datadir}/doc/HTML/en/kalendarz
%{_datadir}/doc/HTML/en/kalendarz/*
%{_datadir}/apps/kalendarz
%{_iconsdir}/hicolor/16x16/apps/*
%{_iconsdir}/hicolor/32x32/apps/*
# XXX: use _desktopdir
%{_datadir}/applnk/Utilities/*
