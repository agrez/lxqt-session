Name:    lxqt-session
Summary: Main session for LXQt desktop suite
Version: 0.13.0
Release: 6%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:  0001-fedberry-config-defaults.patch
BuildRequires: %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires: pkgconfig(lxqt) >= 0.13.0
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11)
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: desktop-file-utils

Requires:      lxqt-themes-fedberry
Recommends:    pcmanfm-qt


%description
%{summary}.


%prep
%autosetup -p1


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
	%{cmake_lxqt} -DBUNDLE_XDG_UTILS=NO -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
for name in hibernate suspend leave; do
    desktop-file-edit --set-key=NoDisplay --set-value=true %{buildroot}%{_datadir}/applications/lxqt-${name}.desktop
done


%files
%{_bindir}/lxqt-session
%{_bindir}/lxqt-config-session
%{_bindir}/lxqt-leave
%{_bindir}/startlxqt
%{_datadir}/applications/*.desktop
%{_datadir}/kdm/sessions/lxqt.desktop
%{_datadir}/lxqt/lxqt.conf
%{_datadir}/lxqt/session.conf
%{_datadir}/lxqt/windowmanagers.conf
%{_datadir}/xsessions/lxqt.desktop
%{_mandir}/man1/lxqt-config-session*
%{_mandir}/man1/lxqt-leave*
%{_mandir}/man1/lxqt-session*
%{_mandir}/man1/startlxqt.1.gz
%{_sysconfdir}/xdg/autostart/lxqt-xscreensaver-autostart.desktop
%{_sysconfdir}/xdg/openbox/lxqt-rc.xml


%changelog
* Fri Nov 30 2018 Vaughan <devel at agrez dot net> - 0.13.0-6
- Update fedberry default (Patch1)
- Update desktop entry modifications

* Thu Nov 15 2018 Vaughan <devel at agrez dot net> - 0.13.0-5
- New Release
- Import config changes from depreciated lxqt-common pkg (patch1)

* Sat Sep 10 2016 Vaughan <devel at agrez dot net> - 0.10.0-5
- Fix incorrect menu entries in lxqt

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Helio Chissini de Castro <helio@kde.org> - 0.10.0-3
- Another razorqt obsoletes

* Sat Dec 12 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-2
- Prepare to epel7 with new cmake3

* Mon Nov 02 2015 Helio Chissini de Castro <helio@kde.org> - 0.10.0-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-4
- Rebuild (gcc5)

* Tue Feb 10 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-3
- Obsoletes razorqt-session and razorqt-desktop as migrated to lxqt

* Mon Feb 09 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-2
- Proper add locale for Qt tm files

* Sun Feb 08 2015 Helio Chissini de Castro <helio@kde.org> - 0.9.0-1
- New upstream release 0.9.0

* Tue Feb 03 2015 Helio Chissini de Castro <hcastro@redhat.com> - 0.9.0-0.1
- Prepare 0.9.0 release

* Mon Dec 29 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-6
- Rebuild against new Qt 5.4.0

* Sat Dec 20 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-5
- Unify naming as discussed on Fedora IRC

* Thu Nov 20 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-4
- omit Obsoletes: razorqt-session (for now)

* Mon Nov 10 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-3
- Update for review issues on https://bugzilla.redhat.com/show_bug.cgi?id=1158999

* Thu Oct 30 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-2
- Obsoletes razorqt session. Disable internal XDG_UTILS

* Mon Oct 27 2014 Helio Chissini de Castro <hcastro@redhat.com> - 0.8.0-1
- First release to LxQt new base
