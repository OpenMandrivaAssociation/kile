Name: kile
Summary: Integrated LaTeX Environment for KF5
Version: 2.9.94
Release: 1
Epoch: 2
Url: https://kile.sourceforge.net/
Source0: http://jaist.dl.sourceforge.net/sourceforge/kile/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Publishing
Requires: texlive
Requires: texlive-scheme-full
Requires: (konsole or plasma6-konsole)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6QmlTools)
BuildRequires:	cmake(Poppler)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6)
BuildRequires:	cmake(Okular6)
BuildSystem:	cmake
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
%{_bindir}/kile
%{_datadir}/applications/org.kde.kile.desktop
%{_datadir}/kconf_update/kile*
%{_datadir}/config.kcfg/kile.kcfg
%{_datadir}/mime/packages/kile.xml
%{_datadir}/kile
%{_datadir}/icons/*/*/*/*
%{_datadir}/metainfo/org.kde.kile.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.kile.main.xml
%{_datadir}/qlogging-categories6/kile.categories
