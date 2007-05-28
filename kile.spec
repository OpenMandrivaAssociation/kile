%define	name	kile
%define	version	1.9.3
%define	release	%mkrel 2
%define	Summary	Integrated LaTeX Environment for KDE3
%define qtdir	%{_prefix}/lib/qt3/%{_lib}

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

%dir %_datadir/apps/kile/
%_datadir/apps/kile/*.rc

%dir %_datadir/apps/kile/mathsymbols/
%_datadir/apps/kile/mathsymbols/*.png

%dir %_datadir/apps/kile/pics/
%_datadir/apps/kile/pics/*.png

%dir %_datadir/apps/kile/templates/
%_datadir/apps/kile/templates/*.tex


%dir %_datadir/apps/kconf_update/
%_datadir/apps/kconf_update/*.upd
%_datadir/apps/kconf_update/*.pl

%dir %_datadir/apps/kile/complete/abbreviation/
%_datadir/apps/kile/complete/abbreviation/*.cwl

%dir %_datadir/apps/kile/complete/dictionary/
%_datadir/apps/kile/complete/dictionary/*.cwl

%dir %_datadir/apps/kile/complete/tex/
%_datadir/apps/kile/complete/tex/*.cwl

%dir %_datadir/apps/kile/encodings/
%_datadir/apps/kile/encodings/*.enc

%dir %_datadir/apps/kile/help/
%_datadir/apps/kile/help/*.lst

%dir %_datadir/apps/kile/icons/hicolor/16x16/actions/
%_datadir/apps/kile/icons/hicolor/16x16/actions/*.png

%dir %_datadir/apps/kile/icons/hicolor/22x22/actions/
%_datadir/apps/kile/icons/hicolor/22x22/actions/*.png

%dir %_datadir/apps/kile/icons/hicolor/32x32/actions/
%_datadir/apps/kile/icons/hicolor/32x32/actions/*.png

%dir %_datadir/apps/kile/icons/hicolor/64x64/actions/
%_datadir/apps/kile/icons/hicolor/64x64/actions/*.png

%dir %_datadir/apps/kile/test/
%_datadir/apps/kile/test/*.sh
%_datadir/apps/kile/test/*.bib
%_datadir/apps/kile/test/*.tex

%_datadir/apps/kile/tips

%_datadir/config.kcfg/kile.kcfg
%doc %_docdir/HTML/en/kile/TODO
%doc %_docdir/HTML/en/kile/common
%doc %_docdir/HTML/en/kile/*.bz2
%doc %_docdir/HTML/en/kile/*.docbook
%doc %_docdir/HTML/en/kile/*.html
%doc %_docdir/HTML/en/kile/*.png

%doc %_docdir/HTML/es/kile/common
%doc %_docdir/HTML/es/kile/*.png
%doc %_docdir/HTML/es/kile/*.docbook
%doc %_docdir/HTML/es/kile/*.bz2

%dir %_docdir/HTML/da/kile/
%doc %_docdir/HTML/da/kile/common
%doc %_docdir/HTML/da/kile/*.bz2
%doc %_docdir/HTML/da/kile/*.docbook

%dir %_docdir/HTML/et/kile/
%doc %_docdir/HTML/et/kile/common
%doc %_docdir/HTML/et/kile/*.bz2
%doc %_docdir/HTML/et/kile/*.docbook


%dir %_docdir/HTML/it/kile/
%doc %_docdir/HTML/it/kile/common
%doc %_docdir/HTML/it/kile/*.bz2
%doc %_docdir/HTML/it/kile/*.docbook
%doc %_docdir/HTML/it/kile/*.png

%dir %_docdir/HTML/nl/kile/
%doc %_docdir/HTML/nl/kile/common
%doc %_docdir/HTML/nl/kile/*.bz2
%doc %_docdir/HTML/nl/kile/*.docbook

%dir %_docdir/HTML/pt/kile/
%doc %_docdir/HTML/pt/kile/common
%doc %_docdir/HTML/pt/kile/*.bz2
%doc %_docdir/HTML/pt/kile/*.docbook

%dir %_docdir/HTML/sv/kile/
%doc %_docdir/HTML/sv/kile/common
%doc %_docdir/HTML/sv/kile/*.bz2
%doc %_docdir/HTML/sv/kile/*.docbook
%doc %_docdir/HTML/sv/kile/*.png



%_iconsdir/hicolor/128x128/apps/kile.png
%_iconsdir/hicolor/16x16/apps/kile.png
%_iconsdir/hicolor/22x22/apps/kile.png
%_iconsdir/hicolor/32x32/apps/kile.png
%_iconsdir/hicolor/48x48/apps/kile.png
%_iconsdir/hicolor/64x64/apps/kile.png
%_iconsdir/hicolor/scalable/apps/kile.svgz



#--------------------------------------------------------------------
%prep
%setup -q
%patch1 -p1 -b .fix_unblacklist_gcc

%build
make -f admin/Makefile.common
QTDIR=%{qtdir}
export QTDIR
%configure2_5x	--disable-rpath \
		--disable-debug \
		--enable-final
%make


%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

# menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Graphics" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

rm -rf $RPM_BUILD_ROOT/%_datadir/apps/katepart/syntax/latex.xml
rm -rf $RPM_BUILD_ROOT/%_datadir/apps/katepart/syntax/bibtex.xml

rm -rf $RPM_BUILD_ROOT/%_datadir/INSTALL
rm -rf $RPM_BUILD_ROOT/%_datadir/README
rm -rf $RPM_BUILD_ROOT/%_datadir/AUTHORS
rm -rf $RPM_BUILD_ROOT/%_datadir/NEWS
rm -rf $RPM_BUILD_ROOT/%_datadir/TODO
rm -rf $RPM_BUILD_ROOT/%_datadir/COPYING

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
