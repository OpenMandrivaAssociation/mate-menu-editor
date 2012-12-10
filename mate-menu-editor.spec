Summary:	Simple menu editor for MATE
Name:		mate-menu-editor
Version:	1.4.0
Release:	1
Group:		System/Configuration/Other
License:	LGPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(libmate-menu)
BuildRequires:	pkgconfig(pygtk-2.0)

Requires:	pygtk2.0
Requires:	python-mateconf
Requires:	python-mate
Requires:	python-mate-menus

Provides:	mozo = %{EVRD}

%description
mozo is a menu editor for MATE that lets you get things done,
simply and quickly.

Just click and type to edit, add, and delete any menu entry.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x

%make

%install
%makeinstall_std

%find_lang mozo --with-gnome

%files -f mozo.lang
%doc README AUTHORS COPYING
%{py_puresitedir}/*
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/mozo
%{_iconsdir}/hicolor/*/*/*



%changelog
* Fri Jun 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 803385
- rebuild fixing python deps

* Wed Jun 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 802818
- imported package mate-menu-editor

