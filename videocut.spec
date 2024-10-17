%define name videocut
%define version 0.2.0
%define release 2

Name:		%{name}
Version:		%{version}
Release:		%{release}
License:		GPLv2
Group:		Video
Url:		https://code.google.com/p/videocut/
Source:		%{name}-%{version}.tar.gz
Patch1:		videocut-strcmp-0.2.0.patch
Patch2:		videocut-0.2.0-ftbfs.patch
BuildRequires:	qt4-devel 
BuildRequires:	pkgconfig(libxine)

Summary:	Application for creating compositions of screenshots from video files

%description
VideoCut is an open source desktop application specialized 
for creating compositions of screenshots from video files.

%prep
%setup -qn %{name}-%{version}.orig
%patch1 -p1
%patch2 -p0

%build
qmake
%make

%install
test "%{buildroot}" != "/" && %{__rm} -rf %{buildroot}
%__install -Dm 0755 build/result/videocut %{buildroot}%{_bindir}/videocut
%__install -Dm 0644 videocut.desktop %{buildroot}%{_datadir}/applications/videocut.desktop
%__install -Dm 0644 videocut.svg %{buildroot}%{_datadir}/pixmaps/videocut.svg


%files

%doc ABOUT AUTHORS THANKSTO
%{_bindir}/videocut
%{_datadir}/applications/videocut.desktop
%{_datadir}/pixmaps/videocut.svg



%changelog
* Thu Oct 01 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 452145
- import videocut


* Thu Oct 1 2009 <steletch@mandriva.org> 0.2.0-2mdv2010.0
- Updated spec file
- Permission fixes

* Mon May 11 2009 Donald Stewart <watersnowrock@gmail.com> 0.2.0-1mdv2010.0
- initial RPM
- import SUSE
- clean SUSE specific stuff
- fix buildrequires
