Name:    lxqt-session
Summary: Main session for LXQt desktop suite
Version: 0.9.0
Release: 1%{?dist}
License: LGPLv2+
URL:     http://lxqt.org/
Source0: http://downloads.lxqt.org/lxqt/0.9.0/lxqt-session-0.9.0.tar.xz

Requires: lxqt-common >= 0.8.0
# Temporary. OpenBox should come through groups
Requires: openbox

## omit for now, until a razorqt -> lxqt transition plan is in place -- Rex
# Obsoletes: razorqt-session <= 0.5.2

BuildRequires: cmake >= 2.8.9
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Xdg)
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(x11)
BuildRequires: kf5-kwindowsystem-devel >= 5.5
BuildRequires: desktop-file-utils

%description
%{summary}.

%prep
%setup

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
	%{cmake} -DBUNDLE_XDG_UTILS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
for name in config-session hibernate lockscreen logout reboot shutdown suspend; do 
	desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
		--remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-${name}.desktop
done

%files
%doc COPYING
%{_bindir}/lxqt-session
%{_bindir}/lxqt-config-session
%{_bindir}/lxqt-leave
%{_datadir}/lxqt/translations/lxqt-session
%{_datadir}/lxqt/translations/lxqt-config-session
%{_datadir}/applications/*.desktop

%changelog
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
