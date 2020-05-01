# Global variables for github repository
%global commit0 69e616772ab45a77baf58ae1202e16c19649826c
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    patchmatrix
Version: 0.18.0
Release: 1%{?dist}
Summary: A JACK patchbay in flow matrix style
URL:     https://github.com/OpenMusicKontrollers/patchmatrix
Source0: https://github.com/OpenMusicKontrollers/patchmatrix/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:   Applications/Multimedia
License: GPLv2+

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: meson

%description
A JACK patchbay in flow matrix style

%prep
%setup -qn %{name}-%{commit0}

%build
VERBOSE=1 meson --prefix=/usr build
cd build
VERBOSE=1 ninja 

%install

cd build
DESTDIR=%{buildroot} ninja install

%files
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri May 1 2019 Drew DeVore <drew@devorcula.com> - 0.18.0
- update to 0.18.0

* Tue Oct 15 2019 Drew DeVore <drew@devorcula.com> - 0.16.0
- update to 0.16.0

* Fri Jul 5 2019 Drew DeVore <drew@devorcula.com> - 0.14.0

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-2
- update for Fedora 29

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.12.0-2
- update to latest master
- switch to meson build

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.20.0-1
- inital release
