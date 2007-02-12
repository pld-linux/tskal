Summary:	Simple calendar which helps you to remember about important days
Summary(pl.UTF-8):	Prosty kalendarz pomagający pamiętać o ważnych datach
Name:		tskal
Version:	0.5
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://mike.oldfield.org.pl/tytus/prog/%{name}-%{version}.tgz
# Source0-md5:	a931673e9bcf3a467494903f282a4e57
URL:		http://mike.oldfield.org.pl/tytus/tskal.html
BuildRequires:	qmake
BuildRequires:	qt-devel > 3.3
Obsoletes:	calendar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tskal is simple and easy application which helps you to remember about
important days. Application displays calendar cards in horizontal line
so it is easy to notice few days before that an event (ie. partner's
birthday) is coming. This gives us some time for action (ie. to buy
flowers). Application uses skin system.

%description -l pl.UTF-8
Tskal jest prostą aplikacją opartą o biblioteki Qt, która wyświetla
kartki kalendarza ułożone w pasek. Dzięki temu, podobnie jak to czynią
poborowi używając centymetra, już na wiele dni wcześniej łatwo
zauważyć, że coś się zbliża (np. imieniny żony) i mamy czas na
sensowną reakcję (czyt. wybór i kupno prezentów i kwiatów). Aplikacja
używa systemu skórek.

%package themes
Summary:	Additional skins for tskal application (recommended)
Summary(pl.UTF-8):	Dodatkowe skórki dla programu tskal (zalecane)
Group:		X11/Applications
Requires:	%{epoch}:%{name}-%{version}-%{release}

%description themes
Additional skins for tskal application, which allows customise user
interface. It is recommended by author to install this package because
there is only one built-in skin in main package.

%description themes -l pl.UTF-8
W tym pakiecie znajdują się dodatkowe skórki do programu tskal. Dzięki
nim można lepiej dostosować wygląd aplikacji. Autor poleca instalację
tego pakietu, ponieważ w głównym pakiecie zawiera się tylko jedna,
domyślna skórka.

%prep
%setup -q

%build
qmake \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS="%{rpmldflags}" \
	QMAKE_RPATH=

%{__make} \
	QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	QTDIR=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/docb/* doc/um/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/tskal
%{_datadir}/tskal/*.qm
%dir %{_datadir}/tskal/themes

%files themes
%defattr(644,root,root,755)
%{_datadir}/tskal/themes/*
