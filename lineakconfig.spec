Summary:	GUI for lineakd daemon configuration
Summary(pl):	Graficzny interfejs do konfiguracji demona lineakd
Name:		lineakconfig
Version:	0.3.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lineak/%{name}-%{version}.tar.gz
Patch0:		%{name}-pl.po.patch
URL:		http://lineak.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
Requires:	lineakd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI to put actions on the multimedia keys on modern keyboards.

%description -l pl
GUI do przypisywania akcji klawiszom multimedialnym wystêpuj±cym na
nowych klawiaturach.

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/lineakconfig
%{_datadir}/lineakconfig
