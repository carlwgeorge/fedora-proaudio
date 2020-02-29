Summary: Jack_delay can be used to measure the round-trip latency of a soundcard.
Name:    jack_delay
Version: 0.4.2
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel

%description
Jack_delay can be used to measure the round-trip latency of a soundcard.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile
sed -i 's|-lasound||' source/Makefile

pushd source
make PREFIX=%{_prefix}
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/

pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING
%{_bindir}/*

%changelog
* Tue Oct 15 2019 Drew DeVore <drew@devorcula.com> - 0.4.2-1
- forked

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- initial release

