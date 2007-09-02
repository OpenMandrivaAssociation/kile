%define	name	kile
%define	version	1.9.3
%define	release	%mkrel 3
%define	Summary	Integrated LaTeX Environment for KDE3

Name:		%{name}
Summary:	%{Summary}
Version: 	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Epoch:		1
License:	GPL
Group:		Publishing
Url:		http://kile.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tetex-latex
BuildRequires:	kdelibs-devel
BuildRequires:  desktop-file-utils
Patch1:			kile-1.8-fix-blacklisted-gcc.patch
Patch2:		kile-1.8.1-i18n-de.patch
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
Provides:	kile-i18n-de >= 1.8.0
Provides:	kile-i18n-es >= 1.8.0
Provides:	kile-i18n-fr >= 1.8.0
Provides:	kile-i18n-it >= 1.8.0
Provides:	kile-i18n-nl >= 1.8.0
Provides:	kile-i18n-pt >= 1.8.0
Provides:	kile-i18n-en_GB >= 1.8.0
Provides:	kile-i18n-da >= 1.8.0
Provides:	kile-i18n-pt_BR	>= 1.8.0
Provides:	kile-i18n-sv >= 1.8.0
Provides:	kile-i18n-ta >= 1.8.0


%description
Integrated LaTeX Environment for KDE3


%post
%{update_menus}
%update_icon_cache hicolor
%{update_desktop_database}

%postun
%{clean_menus}
%clean_icon_cache hicolor
%{clean_desktop_database}

%files -f %name.lang
%defattr(-,root,root,0755)
%doc INSTALL README
%_bindir/*
%_datadir/applications/kde/kile.desktop
%_datadir/mimelnk/text/*
%_datadir/apps/kile/

%_datadir/apps/kconf_update/*.upd
%_datadir/apps/kconf_update/*.pl

%_datadir/config.kcfg/kile.kcfg

%_iconsdir/hicolor/*/apps/*



#--------------------------------------------------------------------
%prep
%setup -q
%patch1 -p1 -b .fix_unblacklist_gcc

%build
make -f admin/Makefile.common
%configure2_5x	--disable-rpath \
		--disable-debug \
		--enable-final
%make


%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

# menu
desktop-file-install --vendor="" \
  --remove-key='Encoding' \
  --remove-category="Application" \
  --add-category="Publishing" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde $RPM_BUILD_ROOT%{_datadir}/applications/kde/*

rm -rf $RPM_BUILD_ROOT/%_datadir/apps/katepart/syntax/latex.xml
rm -rf $RPM_BUILD_ROOT/%_datadir/apps/katepart/syntax/bibtex.xml

rm -rf $RPM_BUILD_ROOT/%_datadir/INSTALL
rm -rf $RPM_BUILD_ROOT/%_datadir/README
rm -rf $RPM_BUILD_ROOT/%_datadir/AUTHORS
rm -rf $RPM_BUILD_ROOT/%_datadir/NEWS
rm -rf $RPM_BUILD_ROOT/%_datadir/TODO
rm -rf $RPM_BUILD_ROOT/%_datadir/COPYING

%find_lang %name --with-html

%clean
rm -rf $RPM_BUILD_ROOT
