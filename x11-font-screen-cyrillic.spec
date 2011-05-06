Name: x11-font-screen-cyrillic
Version: 1.0.4
Release: %mkrel 2
Summary: Xorg X11 font screen-cyrillic
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-screen-cyrillic-%{version}.tar.bz2
License: MIT-like
BuildArch: noarch

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


