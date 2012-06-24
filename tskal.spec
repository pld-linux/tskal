#
#TODO: sync pl and en description
#
Summary:	Simple calendar which helps you to remember about important days
Summary(pl):	Prosty kalendarz pomagaj�cy pami�ta� o wa�nych dniach
Name:		calendar
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
# Source0Download:	http://mike.oldfield.org.pl/tytus/index.html
Source0:	http://mike.oldfield.org.pl/tytus/prog/%{name}-%{version}.tgz
# Source0-md5:	614e6c5bd343cdf731ece14e19494274
URL:		http://mike.oldfield.org.pl/tytus/index.html
BuildRequires:	glibc-devel
BuildRequires:	automake
BuildRequires:	qt-devel >= 3.3}
BuildRequires:	kdelibs-devel
BuildRequires:	autoconf
BuildRequires:	libart_lgpl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calendar is simple and easy application which helps you to remember about
important days.

%description -l pl
Kalendarz jest prost� aplikacj� opart� o biblioteki Qt, kt�ra
wy�wietla kartki kalendarza u�o�one w pasek. Dzi�ki temu, podobnie jak
to czyni� poborowi u�ywaj�c centymetra, ju� na wiele dni wcze�niej
�atwo zauwa�y�, �e co� si� zbli�a (np. imieniny �ony) i mamy czas na
sensown� reakcj� (czyt. wyb�r i kupno prezent�w i kwiat�w).
Kalendarz obs�uguje sk�rki. Przyk�adowe mo�esz pobra� z:
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
%dir %{_datadir}/doc/HTML/en/kalendarz
%{_datadir}/doc/HTML/en/kalendarz/*
%dir %{_datadir}/apps/kalendarz
%{_datadir}/apps/kalendarz/*
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/applnk/Utilities/*
