%global debug_package %{nil}

Name:           airwindows
Version:        20200223
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        A collection of open-source VST audio effects plugins.

Group:          Applications/Multimedia
License:        MIT
URL:            https://www.airwindows.com/
Source0:        https://www.airwindows.com/wp-content/uploads/NewUpdates.zip

%description
A collection of open-source audio effects plugins.

%prep
%autosetup -n NewUpdates

%install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_libdir}/vst/%{name}.vst
install -p -m 744 what.txt %{buildroot}%{_datadir}/doc/airwindows/
install -p -m 744 LinuxVST/*.so %{buildroot}%{_libdir}/vst/%{name}.vst

%clean

%files
%doc what.txt
%{_datadir}/doc/%{name}/
%{_libdir}/vst/

%changelog
* Fri Feb 28 2020 Drew DeVore <drew@devorcula.com> - 20200223
- update

* Tue Oct 15 2019 Drew DeVore <drew@devorcula.com> - 20191013
- Update

* Sun Sep 7 2019 Drew DeVore <drew@devorcula.com> - 20190907
- Initial build