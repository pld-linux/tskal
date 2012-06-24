#
Summary:	Simply calendar which helps you to remember about birthdays of your family
Summary(pl):	Prosty kalendarz, kt�ry pomo�e Ci pami�ta� o urodzinach Twoich bliskich
Name:		calendar
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
#Source0Download:	http://mike.oldfield.org.pl/tytus/index.html
Source0:	http://mike.oldfield.org.pl/tytus/prog/%{name}-%{version}.tgz
# Source0-md5:	614e6c5bd343cdf731ece14e19494274
URL:		http://mike.oldfield.org.pl/tytus/index.html
BuildRequires:  glibc-devel
BuildRequires:	automake
BuildRequires:	qt-devel >= 3.3}
BuildRequires:	kdelibs-devel
BuildRequires:	autoconf
BuildRequires:	libart_lgpl-devel
BuildRequires:	libtool

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%description -l pl
Kalendarz jest prost� aplikacj� opart� o biblioteki Qt, kt�ra wy�wietla kartki kalendarza u�o�one w pasek. Dzi�ki temu, podobnie jak to czyni� poborowi u�ywaj�c centymetra, ju� na wiele dni wcze�niej �atwo zauwa�y�, �e co� si� zbli�a (np. imieniny �ony) i mamy czas na sensown� reakcj� (czyt. wyb�r i kupno prezent�w i kwiat�w).



%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0744,root,root) %{_bindir}/kalendarz
%attr(0644,root,root) /usr/share/doc/HTML/en/kalendarz/um.docb
