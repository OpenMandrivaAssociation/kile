%define	name	kile
%define	version	2.0.1
%define	release	%mkrel 2
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
%_bindir/*
%_datadir/applications/kde/kile.desktop
%_datadir/mimelnk/text/*
%_datadir/apps/kile
%_datadir/apps/kconf_update/*.upd
%_datadir/apps/kconf_update/*.pl
%_datadir/config.kcfg/kile.kcfg
%_iconsdir/hicolor/*/apps/*

#--------------------------------------------------------------------
%prep
%setup -q

%build
make -f admin/Makefile.common
%configure	--disable-rpath \
		--disable-debug \
		--enable-final
%make


%install
%{makeinstall_std}

# menu
desktop-file-install --vendor="" \
  --remove-key='Encoding' \
  --remove-category="Application" \
  --add-category="Publishing" \
  --dir %{buildroot}%{_datadir}/applications/kde %{buildroot}%{_datadir}/applications/kde/*

# fix conflicts with our kdelibs
rm -fr %{buildroot}%{_datadir}/apps/katepart/syntax

%find_lang %name --with-html
