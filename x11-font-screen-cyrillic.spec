Name: x11-font-screen-cyrillic
Version: 1.0.4
Release: 6
Summary: Xorg X11 font screen-cyrillic
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-screen-cyrillic-%{version}.tar.bz2
License: MIT-like
BuildArch: noarch
BuildRequires: fontconfig

BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.2

Conflicts: xorg-x11-cyrillic-fonts <= 6.9.0
Requires: mkfontdir
Requires: mkfontscale

%description
Xorg X11 font screen-cyrillic

%prep
%setup -q -n font-screen-cyrillic-%{version}

%build
./configure --prefix=/usr --x-includes=%{_includedir}\
	    --x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/cyrillic

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/cyrillic/fonts.dir
rm -f %{buildroot}%_datadir/fonts/cyrillic/fonts.scale

%post
mkfontscale %_datadir/fonts/cyrillic
mkfontdir %_datadir/fonts/cyrillic

%postun
mkfontscale %_datadir/fonts/cyrillic
mkfontdir %_datadir/fonts/cyrillic

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_datadir/fonts/cyrillic/screen8x16*.pcf.gz




%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.4-3mdv2011.0
+ Revision: 675493
- br fontconfig for fc-query used in new rpm-setup-build

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2
+ Revision: 671216
- mass rebuild

* Thu Dec 09 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 618746
- new release

* Wed Oct 06 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 583222
- new release

* Wed Oct 06 2010 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 583215
- new release

* Wed Jan 13 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 490691
- Fix license
- New version: 1.0.2

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-3mdv2009.1
+ Revision: 351272
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2009.0
+ Revision: 226001
- rebuild
- fix no-buildroot-tag

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 134667
- fix prereq
- kill re-definition of %%buildroot on Pixel's request


* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-1mdv2007.0
+ Revision: 86036
- new release

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com> 1.0.0-4mdv2007.0
+ Revision: 51494
- Fonts packages now are noarch. Moved for new place /usr/share/fonts. Approved by Boiko

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - increment release
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

