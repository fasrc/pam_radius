Name: pam_radius
Summary: PAM Module for RADIUS Authentication
Version: 2.0.0
Release: 2fasrc01%{?dist}
License: GPLv2+
URL: http://www.freeradius.org/pam_radius_auth/

# In reality the releases are located in
# https://github.com/FreeRADIUS/pam_radius/archive/refs/tags/release_2_0_0.tar.gz
# but that causes an error when building the package because the web name
# and the local name do not match
Source: ftp://ftp.freeradius.org/pub/radius/pam_radius-%{version}.tar.gz
Requires: pam
BuildRequires: pam-devel
BuildRequires: gcc

# patches default location of configuration file in pam_radius_auth.h 
# Sent upstream via email 20100114
Patch1: pam_radius_auth-conffile-location.patch
# patches default location of configuration file in radius.h  
# Sent upstream via email 20100114
Patch2: radius-conffile-location.patch
# patches default location of configuration file in pam_radius.conf
# Sent upstream via email 20100221
Patch3: pam_radius_auth-conf-inlinedoc.patch
# patches default location of configuration file in INSTALL documentation file
# Sent upstream via email 20100221
Patch4: INSTALL-doc.patch
# https://github.com/FreeRADIUS/pam_radius/commit/d0eda229d93494202c407bdb176679425affad0b
Patch5: pam_radius_auth-stop-printing-password.patch
#FASRC pathc to use Auth Token From Radius
Patch6: pam_radius_auth.patch

%description
pam_radius is a PAM module which allows user authentication using 
a radius server.

%prep
%setup -q -n pam_radius-release_2_0_0
%patch1
%patch2
%patch3
%patch4
%patch5 -p1 -b .stop-printing-password

%build
%configure --enable-werror
make %{?_smp_mflags} CFLAGS="%{optflags} -Wall -fPIC -Wno-unused-but-set-variable -Wno-strict-aliasing"

%install
mkdir -p %{buildroot}/%{_lib}/security
install -p pam_radius_auth.so %{buildroot}/%{_lib}/security
mkdir -p %{buildroot}%{_sysconfdir}
install -p pam_radius_auth.conf %{buildroot}%{_sysconfdir}/pam_radius.conf


%files
%doc README.rst INSTALL USAGE LICENSE Changelog
%config(noreplace) %attr(0600, root, root) %{_sysconfdir}/pam_radius.conf
/%{_lib}/security/pam_radius_auth.so

%changelog
* Fri Sep 16 2022 Paul Edmon <pedmon@cfa.harvard.edu> - 2.0.0-2fasrc01
- Change Auth Token to Verification Code

* Mon Aug 22 2022 Iker Pedrosa <ipedrosa@redhat.com> - 2.0.0-2
- pam_radius_auth: stop printing password

* Tue Jul  5 2022 Iker Pedrosa <ipedrosa@redhat.com> - 2.0.0-1
- Rebase to version 2.0.0. Resolves: #2103904

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Alexander Scheel <ascheel@redhat.com> - 1.4.0-14
- Fix NULL-termination of password buffer, garbage contents prior to hashing

* Mon Apr 01 2019 Jason Taylor <jtfas90@gmail.com> - 1.4.0-13
- Fixed broken patch definition

* Mon Apr 01 2019 Jason Taylor <jtfas90@gmail.com> - 1.4.0-12
- Rebuild with gcc buildrequires

* Thu Mar 14 2019 Jason Taylor <jtfas90@gmail.com> - 1.4.0-11
- Rebuilt with patch for password length buffer overflow

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.0-2
- Update spec to guidelines and fix build on new arches

* Sun Dec 21 2014 Tim Lank <timlank@timlank.com> 1.4.0-1
- Many changes.  See USAGE for details.

* Sun Feb 21 2010 Tim Lank <timlank@timlank.com> 1.3.17-2
- everything it takes to get this accepted for Fedora 

* Mon Oct 26 2009 Richard Monk <rmonk@redhat.com> 1.3.17-0
- Bump for new version
- spec fixes for x86_64 builds

* Mon Jun 03 2002 Richie Laager <rlaager@wiktel.com> 1.3.15-0
- Inital RPM Version
