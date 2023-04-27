Name:           epstool
Version:        3.09
Release:        2
Summary:        A utility to create or extract preview images in EPS files
License:        GPLv2+
URL:            http://pages.cs.wisc.edu/~ghost/gsview/epstool.htm
Source0:        http://www.ghostgum.com.au/download/%{name}-%{version}.tar.gz
Patch0:         fix-cc.patch

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
%autosetup -n %{name}-%{version} -p1

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
* Thu Apr 27 2023 yoo <sunyuechi@iscas.ac.cn> - 3.09-2
- Add support for specifying cc

* Wed Dec 15 2021 jiangxinyu <jiangxinyu@kylinos.cn> - 3.09-1
- upgrade to 3.09

* Tue May 05 2020 Hubble Zhu <zhuhengbo1@huawei.com> - 3.08-1
- First release.
