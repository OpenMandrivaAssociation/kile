Name: kile
Summary: Integrated LaTeX Environment for KDE4
Version: 2.1.3
Release: 3
Epoch: 2
Url: http://kile.sourceforge.net/
Source0: http://jaist.dl.sourceforge.net/sourceforge/kile/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Publishing
Requires: texlive
Requires: texlive-scheme-full
Requires: konsole
Requires: katepart
BuildRequires: kdelibs4-devel
Obsoletes: kile-i18n-de
Obsoletes: kile-i18n-es 
Obsoletes: kile-i18n-fr 
Obsoletes: kile-i18n-it 
Obsoletes: kile-i18n-nl 
Obsoletes: kile-i18n-pt
Obsoletes: kile-i18n-en_GB
Obsoletes: kile-i18n-da
Obsoletes: kile-i18n-pt_BR
Obsoletes: kile-i18n-sv
Obsoletes: kile-i18n-ta

%description
Kile is an integrated LaTeX Environment for KDE4.

%files -f %name.lang
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog README* kile-remote-control.txt
%{_kde_bindir}/kile
%{_kde_datadir}/applications/kde4/kile.desktop
%{_kde_appsdir}/kconf_update/kile*
%{_kde_datadir}/config.kcfg/kile.kcfg
%{_kde_datadir}/dbus-1/interfaces/net.sourceforge.kile.main.xml
%{_kde_datadir}/mime/packages/kile.xml
%{_kde_appsdir}/kile
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_kde4
%make

%install
%{makeinstall_std} -C build
chmod 0755 %{buildroot}%{_kde_appsdir}/kconf_update/kile*.pl %{buildroot}%{_kde_appsdir}/kile/test/runTests.sh
chmod 0644 %{buildroot}%{_kde_datadir}/applications/kde4/kile.desktop

%find_lang %name --with-html
