Summary:	Simple calendar which helps you to remember about important days
Summary(pl):	Prosty kalendarz pomagaj±cy pamiêtaæ o wa¿nych datach
Name:		tskal
Version:	0.5
Release:	2
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

%description -l pl
Tskal jest prost± aplikacj± opart± o biblioteki Qt, która wy¶wietla
kartki kalendarza u³o¿one w pasek. Dziêki temu, podobnie jak to czyni±
poborowi u¿ywaj±c centymetra, ju¿ na wiele dni wcze¶niej ³atwo
zauwa¿yæ, ¿e co¶ siê zbli¿a (np. imieniny ¿ony) i mamy czas na
sensown± reakcjê (czyt. wybór i kupno prezentów i kwiatów). 
Aplikacja u¿ywa systemu skórek. 

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
%attr(755,root,root) %{_bindir}/*
%{_docdir}/tskal
%{_datadir}/tskal
