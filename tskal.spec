# TODO:
# - optflags
Summary:	Simple calendar which helps you to remember about important days
Summary(pl):	Prosty kalendarz pomagaj�cy pami�ta� o wa�nych datach
Name:		tskal
Version:	0.5
Release:	1
License:	GPL
Group:		X11/Applications
# Source0Download:	http://mike.oldfield.org.pl/tytus/index.html
Source0:	http://mike.oldfield.org.pl/tytus/prog/%{name}-%{version}.tgz
# Source0-md5:	6237687c0218091b88e84b09c32f34bf
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

%description -l pl
Tskal jest prost� aplikacj� opart� o biblioteki Qt, kt�ra wy�wietla
kartki kalendarza u�o�one w pasek. Dzi�ki temu, podobnie jak to czyni�
poborowi u�ywaj�c centymetra, ju� na wiele dni wcze�niej �atwo
zauwa�y�, �e co� si� zbli�a (np. imieniny �ony) i mamy czas na
sensown� reakcj� (czyt. wyb�r i kupno prezent�w i kwiat�w). 
Aplikacja u�ywa systemu sk�rek. 

%prep
%setup -q

%build
qmake
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
%attr(755,root,root) %{_bindir}/*
%{_docdir}/tskal
%{_datadir}/tskal
