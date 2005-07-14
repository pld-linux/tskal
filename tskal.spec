#
Summary:	Simple calendar which helps you to remember about important days
Summary(pl):	Prosty kalendarz pomagaj±cy pamiêtaæ o wa¿nych dniach
Name:		tskal
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications
# Source0Download:	http://mike.oldfield.org.pl/tytus/index.html
Source0:	http://mike.oldfield.org.pl/tytus/prog/%{name}-%{version}.tgz
# Source0-md5:	5ed8ee5ab0dc2914638e136530ad6b2b
URL:		http://mike.oldfield.org.pl/tytus/tskal.html
BuildRequires:	glibc-devel
BuildRequires:	qt-devel > 3.3
BuildRequires:	qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

Obsoletes:	calendar

%description
Tskal is simple and easy application which helps you to remember about 
important days. Application displays calendar cards in horizontal line 
so it is easy to notice few days before that an event (ie. partner's 
birthday) is comming. This gives us some time for action (ie. to buy 
flowers). Application uses skin system.
%description -l pl
Tskal jest prost± aplikacj± opart± o biblioteki Qt, która wy¶wietla
kartki kalendarza u³o¿one w pasek. Dziêki temu, podobnie jak to czyni±
poborowi u¿ywaj±c centymetra, ju¿ na wiele dni wcze¶niej ³atwo
zauwa¿yæ, ¿e co¶ siê zbli¿a (np. imieniny ¿ony) i mamy czas na
sensown± reakcjê (czyt. wybór i kupno prezentów i kwiatów). 
Aplikacja u¿ywa systemu skórek. 

%prep
%setup -q -n %{name}-%{version}

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
%dir %{_docdir}/tskal
%{_docdir}/tskal/*
%dir %{_datadir}/tskal
%{_datadir}/tskal/*
