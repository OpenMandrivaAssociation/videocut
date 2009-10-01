%define name videocut
%define version 0.2.0
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Video
Url:		http://code.google.com/p/videocut/
Source:		%{name}-%{version}.tar.gz
Patch1:		videocut-strcmp-0.2.0.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	qt4-devel 
BuildRequires:	%mklibname xine-devel

Summary:	Application for creating compositions of screenshots from video files

%description
VideoCut is an open source desktop application specialized 
for creating compositions of screenshots from video files.

%prep
%setup -qn %{name}-%{version}.orig
%patch1 -p1

%build
qmake
%make

%install
test "%{buildroot}" != "/" && %{__rm} -rf %{buildroot}
%__install -Dm 0755 build/result/videocut %{buildroot}%{_bindir}/videocut
%__install -Dm 0644 videocut.desktop %{buildroot}%{_datadir}/applications/videocut.desktop
%__install -Dm 0644 videocut.svg %{buildroot}%{_datadir}/pixmaps/videocut.svg


%clean
test "%{buildroot}" != "/" && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ABOUT AUTHORS THANKSTO
%{_bindir}/videocut
%{_datadir}/applications/videocut.desktop
%{_datadir}/pixmaps/videocut.svg

