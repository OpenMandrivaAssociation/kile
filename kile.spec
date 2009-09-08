# http://apps.sourceforge.net/mediawiki/kile/index.php?title=KileForKDE4

%define	name	kile
%define	version	2.1
%define	release	%mkrel 0.%svn.1
%define	Summary	Integrated LaTeX Environment for KDE4
%define svn     b2

Name:		%{name}
Summary:	%{Summary}
Version: 	%{version}
Release:	%{release}
Source0:	http://jaist.dl.sourceforge.net/sourceforge/kile/%{name}-%{version}%svn.tar.bz2
Epoch:		2
License:	GPLv2+
Group:		Publishing
Url:		http://kile.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tetex-latex
Requires:   kappfinder
BuildRequires:	kdelibs4-devel
BuildRequires:  desktop-file-utils
Obsoletes:      kile-i18n-de
Obsoletes:      kile-i18n-es 
Obsoletes:      kile-i18n-fr 
Obsoletes:      kile-i18n-it 
Obsoletes:      kile-i18n-nl 
Obsoletes:      kile-i18n-pt
Obsoletes:      kile-i18n-en_GB
Obsoletes:      kile-i18n-da
Obsoletes:      kile-i18n-pt_BR
Obsoletes:      kile-i18n-sv
Obsoletes:      kile-i18n-ta

%description
Kile is an integrated LaTeX Environment for KDE4.

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog README* TODO kile-remote-control.txt
%{_kde_bindir}/kile
%{_kde_datadir}/applications/kde4/kile.desktop
%{_kde_appsdir}/kconf_update/kile*
%{_kde_datadir}/config.kcfg/kile.kcfg
%{_kde_datadir}/dbus-1/interfaces/net.sourceforge.kile.main.xml
%{_kde_datadir}/mimelink/text/x-kilepr.desktop
%{_kde_appsdir}/kile
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}%svn

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%{makeinstall_std} -C build

# menu
desktop-file-install --vendor="" \
  --remove-key='Encoding' \
  --remove-category="Application" \
  --add-category="Publishing" \
  --dir %{buildroot}%{_kde_datadir}/applications/kde4 %{buildroot}%{_kde_datadir}/applications/kde4/*
