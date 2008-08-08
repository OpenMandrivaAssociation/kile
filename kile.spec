%define	name	kile
%define	version	2.0.1
%define	release	%mkrel 3
%define	Summary	Integrated LaTeX Environment for KDE3

Name:		%{name}
Summary:	%{Summary}
Version: 	%{version}
Release:	%{release}
Source0:	http://jaist.dl.sourceforge.net/sourceforge/kile/%{name}-%{version}.tar.bz2
Epoch:		1
License:	GPLv2+
Group:		Publishing
Url:		http://kile.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tetex-latex
BuildRequires:	kdelibs-devel
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
Kile is an integrated LaTeX Environment for KDE3.

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%{update_desktop_database}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%{clean_desktop_database}
%endif

%files -f %name.lang
%defattr(-,root,root,0755)
%doc README ChangeLog TODO AUTHORS
%_kde3_bindir/*
%_kde3_datadir/applications/kde/kile.desktop
%_kde3_datadir/mimelnk/text/*
%_kde3_datadir/apps/kile
%_kde3_datadir/apps/kconf_update/*.upd
%_kde3_datadir/apps/kconf_update/*.pl
%_kde3_datadir/config.kcfg/kile.kcfg
%_kde3_iconsdir/hicolor/*/apps/*

#--------------------------------------------------------------------
%prep
%setup -q

%build
make -f admin/Makefile.common
%configure_kde3
%make


%install
rm -fr %buildroot
%{makeinstall_std}

# menu
desktop-file-install --vendor="" \
  --remove-key='Encoding' \
  --remove-category="Application" \
  --add-category="Publishing" \
  --dir %{buildroot}%{_kde3_datadir}/applications/kde %{buildroot}%{_kde3_datadir}/applications/kde/*

# fix conflicts with our kdelibs
rm -fr %{buildroot}%{_kde3_datadir}/apps/katepart/syntax

%find_lang %name --with-html
