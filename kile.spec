Name: kile
Summary: Integrated LaTeX Environment for KF5
Version: 2.9.91
Release: 1
Epoch: 2
Url: http://kile.sourceforge.net/
Source0: http://jaist.dl.sourceforge.net/sourceforge/kile/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Publishing
Requires: texlive
Requires: texlive-scheme-full
Requires: konsole
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(Okular5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5)
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
Kile is an integrated LaTeX Environment for KF5.

%files -f %name.lang
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog README* kile-remote-control.txt
%{_kde5_bindir}/kile
%{_kde5_datadir}/applications/org.kde.kile.desktop
%{_kde5_datadir}/kconf_update/kile*
%{_kde5_datadir}/config.kcfg/kile.kcfg
%{_kde5_datadir}/dbus-1/interfaces/net.sourceforge.kile.main.xml
%{_kde5_datadir}/mime/packages/kile.xml
%{_kde5_datadir}/kile
%{_kde5_iconsdir}/*/*/*/*
%{_kde5_libdir}/*.so
%{_sysconfdir}/xdg/kile.categories
%{_datadir}/metainfo/org.kde.kile.appdata.xml

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%cmake_kde5
%build
%ninja_build -C build

%install
%{ninja_install} -C build

%find_lang %name --with-html
