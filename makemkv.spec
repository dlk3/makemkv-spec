%define  debug_package %{nil}


Name:           makemkv
Version:        1.14.7
Release:        3%{?dist}
Summary:        Software to convert blu-ray and dvd to mkv

License:        Proprietary & GPLv2
URL:            https://www.makemkv.com/forum/viewtopic.php?f=3&t=224
Source0:        https://www.makemkv.com/download/%{name}-bin-%{version}.tar.gz
Source1:        https://www.makemkv.com/download/%{name}-oss-%{version}.tar.gz
BuildArch:		x86_64

Obsoletes:		libaacs

BuildRequires:	qt5-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	openssl-devel
BuildRequires:	gcc-c++

Provides:		libdriveio.so.0()(64bit)
Provides:		libmakemkv.so.1()(64bit)
Provides:		libmmbd.so.0()(64bit)
Provides:		libaacs.so.0()(64bit)
Provides:		libbdplus.so.0()(64bit)


%description
MakeMKV is your one-click solution to convert video that you own into 
free and patents-unencumbered format that can be played everywhere. 
MakeMKV is a format converter, otherwise called "transcoder". It 
converts the video clips from proprietary (and usually encrypted) disc 
into a set of MKV files, preserving most information but not changing 
it in any way.


%prep
%setup -n %{name}-bin-%{version}
%setup -n %{name}-oss-%{version} -T -b 1 -D


%build
cd ../%{name}-oss-%{version}
%configure --enable-allcodecs
make %{?_smp_mflags}


%install
cd ../%{name}-oss-%{version}
make install DESTDIR=%{buildroot}
cd ../%{name}-bin-%{version}
mkdir tmp
echo "accepted" >tmp/eula_accepted
make install DESTDIR=%{buildroot}
%{__ln_s} libmmbd.so.0 %{buildroot}%{_libdir}/libaacs.so.0
%{__ln_s} libmmbd.so.0 %{buildroot}%{_libdir}/libbdplus.so.0


%files
%license License.txt
%{_bindir}/makemkv
%{_bindir}/makemkvcon
%{_libdir}/libdriveio.so.0
%{_libdir}/libmakemkv.so.1
%{_libdir}/libmmbd.so.0
%{_libdir}/libaacs.so.0
%{_libdir}/libbdplus.so.0
%{_datadir}/MakeMKV/appdata.tar
%{_datadir}/MakeMKV/blues.jar
%{_datadir}/MakeMKV/blues.policy
%{_datadir}/applications/makemkv.desktop
%{_datadir}/icons/hicolor/16x16/apps/makemkv.png
%{_datadir}/icons/hicolor/22x22/apps/makemkv.png
%{_datadir}/icons/hicolor/32x32/apps/makemkv.png
%{_datadir}/icons/hicolor/64x64/apps/makemkv.png
%{_datadir}/icons/hicolor/128x128/apps/makemkv.png


%post
echo -e "\n  **********************************************************************"
echo "  *  Before running a new release of makemkv for the first time be     *"
echo -e "  *  sure to delete your \$HOME/.MakeMKV directory, if one exists.      *"
echo "  **********************************************************************"


%changelog
* Mon Dec 9 2019 David King <dave@daveking.com> - 1.14.7-3
	Add libmmbd->libaacs support for VLC and others
* Sun Dec 8 2019 David King <dave@daveking.com> - 1.14.7-2
	Add --enable-allcodecs to configure
* Sat Dec 7 2019 David King <dave@daveking.com> - 1.14.7-1
	Initial Version
- 
