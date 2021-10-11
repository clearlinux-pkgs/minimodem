#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : minimodem
Version  : 0.24.1
Release  : 10
URL      : https://github.com/kamalmostafa/minimodem/archive/minimodem-0.24-1.tar.gz
Source0  : https://github.com/kamalmostafa/minimodem/archive/minimodem-0.24-1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: minimodem-bin = %{version}-%{release}
Requires: minimodem-filemap = %{version}-%{release}
Requires: minimodem-license = %{version}-%{release}
Requires: minimodem-man = %{version}-%{release}
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(sndfile)

%description
minimodem - general-purpose software audio FSK modem
Minimodem is a command-line program which decodes (or generates) audio
modem tones at any specified baud rate, using various framing protocols.
It acts a general-purpose software FSK modem, and includes support for
various standard FSK protocols such as Bell103, Bell202, RTTY, TTY/TDD,
NOAA SAME, and Caller-ID.

%package bin
Summary: bin components for the minimodem package.
Group: Binaries
Requires: minimodem-license = %{version}-%{release}
Requires: minimodem-filemap = %{version}-%{release}

%description bin
bin components for the minimodem package.


%package filemap
Summary: filemap components for the minimodem package.
Group: Default

%description filemap
filemap components for the minimodem package.


%package license
Summary: license components for the minimodem package.
Group: Default

%description license
license components for the minimodem package.


%package man
Summary: man components for the minimodem package.
Group: Default

%description man
man components for the minimodem package.


%prep
%setup -q -n minimodem-minimodem-0.24-1
cd %{_builddir}/minimodem-minimodem-0.24-1
pushd ..
cp -a minimodem-minimodem-0.24-1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633823903
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1633823903
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/minimodem
cp %{_builddir}/minimodem-minimodem-0.24-1/COPYING %{buildroot}/usr/share/package-licenses/minimodem/245cd12d5d5b2b1afd89530068d8f330f0073ca2
cp %{_builddir}/minimodem-minimodem-0.24-1/debian/copyright %{buildroot}/usr/share/package-licenses/minimodem/d9774cd82a13c9ab3ebdef7250922a91bc10fc57
pushd ../buildavx2/
%make_install_v3
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/minimodem
/usr/share/clear/optimized-elf/bin*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-minimodem

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/minimodem/245cd12d5d5b2b1afd89530068d8f330f0073ca2
/usr/share/package-licenses/minimodem/d9774cd82a13c9ab3ebdef7250922a91bc10fc57

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/minimodem.1
