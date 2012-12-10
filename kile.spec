Name: kile
Summary: Integrated LaTeX Environment for KDE4
Version: 2.1.2
Release: 2
Epoch: 2
Url: http://kile.sourceforge.net/
Source0: http://jaist.dl.sourceforge.net/sourceforge/kile/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Publishing
Requires: texlive-latex.bin
Requires: konsole
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


%changelog
* Sat Jun 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2:2.1.2-2
+ Revision: 803917
- Adjust dependencies

* Thu May 03 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2:2.1.2-1
+ Revision: 795255
- update to 2.1.2

* Sat Jun 18 2011 Funda Wang <fwang@mandriva.org> 2:2.1-1
+ Revision: 685897
- new version 2.1 final

* Thu Apr 28 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2:2.1-0.b5.1
+ Revision: 659806
- beta5

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2:2.1-0.b4.2mdv2011.0
+ Revision: 612606
- the mass rebuild of 2010.1 packages

* Fri Apr 09 2010 Funda Wang <fwang@mandriva.org> 2:2.1-0.b4.1mdv2010.1
+ Revision: 533525
- 2.1b4

* Thu Mar 18 2010 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2:2.1-0.b3.2mdv2010.1
+ Revision: 525123
- Add konsole as Requires, thanks to Francois Boulogne

* Thu Dec 03 2009 Funda Wang <fwang@mandriva.org> 2:2.1-0.b3.1mdv2010.1
+ Revision: 472762
- new version 2.1 beta 3

* Thu Sep 17 2009 Helio Chissini de Castro <helio@mandriva.com> 2:2.1-0.b2.2mdv2010.0
+ Revision: 443974
- Proper packaging kile. It requires kappfinder which is obsolete

* Wed Sep 09 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2:2.1-0.b2.1mdv2010.0
+ Revision: 434566
- Fix file list
- Update to beta2

* Sat Feb 21 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:2.1-0.924057.3mdv2009.1
+ Revision: 343531
- Fix file list
- Fix file list

* Wed Feb 18 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:2.1-0.924057.2mdv2009.1
+ Revision: 342518
- Fix file list

* Tue Feb 10 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:2.1-0.924057.1mdv2009.1
+ Revision: 339043
- Snapshot of the KDE4 version

* Tue Dec 09 2008 Funda Wang <fwang@mandriva.org> 1:2.0.3-1mdv2009.1
+ Revision: 312239
- New version 2.0.3

* Wed Sep 03 2008 Funda Wang <fwang@mandriva.org> 1:2.0.2-1mdv2009.0
+ Revision: 279422
- New version 2.0.2

* Fri Aug 08 2008 Funda Wang <fwang@mandriva.org> 1:2.0.1-3mdv2009.0
+ Revision: 267854
- switch to /opt

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1:2.0.1-2mdv2009.0
+ Revision: 267786
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon May 19 2008 Lev Givon <lev@mandriva.org> 1:2.0.1-1mdv2009.0
+ Revision: 208989
- Update to 2.0.1.

* Sun Feb 10 2008 Frederik Himpe <fhimpe@mandriva.org> 1:2.0-3mdv2008.1
+ Revision: 164730
- Rebuild against openldap 2.4 libraries

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - better description

* Fri Nov 23 2007 Funda Wang <fwang@mandriva.org> 1:2.0-2mdv2008.1
+ Revision: 111377
- fix conflicts with kdelibs

* Thu Nov 22 2007 Funda Wang <fwang@mandriva.org> 1:2.0-1mdv2008.1
+ Revision: 111124
- add kate syntax
- fix filelist
- New version 2.0

* Sun Sep 02 2007 Funda Wang <fwang@mandriva.org> 1:1.9.3-3mdv2008.0
+ Revision: 77752
- fix desktop file category

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - Add menu entry


* Tue Nov 21 2006 Laurent Montel <lmontel@mandriva.com> 1.9.3-1mdv2007.0
+ Revision: 85839
- 1.9.3
- Import kile

* Tue Aug 29 2006 Laurent MONTEL <lmontel@mandriva.com> 1.9.2-1
- 1.9.2

* Fri Jul 14 2006 Laurent MONTEL <lmontel@mandriva.com> 1.9.1-1
- 1.9.1

* Fri Jul 14 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.9-3mdv2007.0
- Rebuild for new menu and extension
- Use macro for icons and macro

* Thu May 11 2006 Laurent MONTEL <lmontel@mandriva.com> 1.9-2
- Rebuild to generate category

* Wed Mar 22 2006 Laurent MONTEL <lmontel@mandriva.com> 1.9-1
- 1.9

* Mon Dec 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.8.1-4mdk
- Remove redundant Buildrequires

* Fri Dec 09 2005 Laurent MONTEL <lmontel@mandriva.com> 1.8.1-3
- Obsolete kile-i18n

* Thu Sep 01 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.8.1-2mdk
- use %%mkrel
- from Dominik Grafenhofer <dominik@grafenhofer.at>
  - added german GUI translation

* Fri Jun 03 2005 Laurent MONTEL <lmontel@mandriva.com> 1.8.1-1mdk
- 1.8.1

* Tue May 24 2005 Laurent MONTEL <lmontel@mandriva.com> 1.8-1mdk
- 1.8
- Necessary to add epoch because previous package was not named correctly :(

* Wed May 04 2005 Laurent MONTEL <lmontel@mandriva.com> 1.8b2-2mdk
- i18n is not in separate package

* Tue Apr 26 2005 Giuseppe Ghibò <ghibo@mandriva.com> 1.8b2-1mdk
- Release: 1.8b2.

* Sun Apr 17 2005 Giuseppe Ghibò <ghibo@mandriva.com> 1.8b1-1mdk
- Release: 1.8b1.
- Specify QTDIR (needed for building under X86-64).

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.7.1-5mdk
- Fix menu

* Tue Dec 07 2004 Dominik Grafenhofer <dominik@grafenhofer.at> 1.7.1-4mdk
- fixed dependencies of some i18n packages

* Mon Nov 08 2004 Dominik Grafenhofer <dominik@grafenhofer.at> 1.7.1-3mdk
- Added i18n packages
- fix source (the first 1.7.1 tarball was not working)

* Thu Oct 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.7.1-2mdk
- Fix conflict

* Tue Oct 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.7.1-1mdk
- 1.7.1

* Sat Jun 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.6.3-2mdk
- Rebuild

* Sat Jun 05 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.6.3-1mdk
- 1.6.3
- cleanups

* Thu Apr 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.6.2-1mdk
- 1.6.2

* Sun Feb 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.6.1-1mdk
- 1.6.1
- fix menu

