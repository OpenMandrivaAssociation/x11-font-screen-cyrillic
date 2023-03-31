Name: x11-font-screen-cyrillic
Version: 1.0.5
Release: 2
Summary: Xorg X11 font screen-cyrillic
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-screen-cyrillic-%{version}.tar.xz
License: MIT-like
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font screen-cyrillic.

%prep
%autosetup -p1 -n font-screen-cyrillic-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/cyrillic
%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/cyrillic/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/cyrillic/fonts.scale

%post
mkfontscale %{_datadir}/fonts/cyrillic
mkfontdir %{_datadir}/fonts/cyrillic

%postun
mkfontscale %{_datadir}/fonts/cyrillic
mkfontdir %{_datadir}/fonts/cyrillic

%files
%{_datadir}/fonts/cyrillic/screen8x16*.pcf.gz
