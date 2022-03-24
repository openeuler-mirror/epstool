Name:           epstool
Version:        3.08
Release:        2
Summary:        A utility to create or extract preview images in EPS files
License:        GPLv2+
URL:            http://pages.cs.wisc.edu/~ghost/gsview/epstool.htm
Source0:        http://mirror.cs.wisc.edu/pub/mirrors/ghost/ghostgum/%{name}-%{version}.tar.gz
# Patch to compile with gcc 4.3 and newer (taken from Gentoo)
Patch0:         epstool-3.08-gcc43.patch

BuildRequires:  gcc

%description
Epstool is a utility to create or extract preview images in EPS files,
fix bounding boxes and convert to bitmaps.

Features:
* Add EPSI, DOS EPS or Mac PICT previews.
* Extract PostScript from DOS EPS files.
* Uses Ghostscript to create preview bitmaps.
* Create a TIFF, WMF, PICT or Interchange preview from part of a
  bitmap created by Ghostscript.
* works under Win32, Win64, OS/2 and Unix.
* works on little-endian machines (Intel) or big endian (Sun Sparc,
  Motorola) machines.

%prep
%setup -q
%patch0 -p1

%build
# SMP build doesn't work.
make

%install
rm -rf %{buildroot}
install -D -p -m 755 bin/epstool %{buildroot}%{_bindir}/epstool
install -D -p -m 644 doc/epstool.1 %{buildroot}%{_mandir}/man1/epstool.1

%files
%doc LICENCE doc/epstool.htm doc/gsview.css
%{_bindir}/epstool
%{_mandir}/man1/epstool.1.*

%changelog
* Thu Mar 24 2022 caodongxia <caodongxia@huawei.com> - 3.08-2
- Delete %{?dist}

* Tue May 05 2020 Hubble Zhu <zhuhengbo1@huawei.com> - 3.08-1
- First release.
