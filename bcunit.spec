# NOTE:	Latest stable release (3.0) still uses CUnit
#	as name so it conflicts with 'cunit' package.
%define commit 29c556fa8ac1ab21fba1291231ffa8dea43cf32a
%define shortcommit %(c=%{commit}; echo ${c:0:7})

%define oname BCUnit
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define major	1
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}

Summary:	A fork of the defunct project CUnit (Unit Testing Framework for C)
Name:		%{lname}
Version:	3.0.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/BelledonneCommunications/%{name}
#Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{version}.tar.gz
Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{commit}/%{name}-%{commit}.zip
Patch0:		%{name}-3.0-pkgconfig.patch
Patch1:		%{name}-3.0-soversion.patch
Patch2:		%{name}-3.0-docdir.patch
Patch3:		%{name}-29c556fa-pkgconfig.patch
Patch4:		%{name}-29c556fa-soversion.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(ncurses)

%description
BCUnit is a lightweight system for writing, administering, and running unit
tests in C. It provides C programmers a basic testing functionality with a
flexible variety of user interfaces.

BCUnit is built as a static library which is linked with the user's testing
code. It uses a simple framework for building test structures, and provides
a rich set of assertions for testing common data types. In addition, several
different interfaces are provided for running tests and reporting results.
These interfaces currently include:

- Automated: Non-interactive output to xml file
- Basic: Non-interactive flexible programming interface
- Console: Interactive console interface (ansi C)
- Curses: Interactive graphical interface (Unix)

BCUnit is a fork of the defunct project CUnit, with several fixes and patches
applied.

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for accessing USB devices
Group:		System/Libraries

%description -n	%{libname}
BCUnit is a lightweight system for writing, administering, and running unit
tests in C. It provides C programmers a basic testing functionality with a
flexible variety of user interfaces.

BCUnit is built as a static library which is linked with the user's testing
code. It uses a simple framework for building test structures, and provides
a rich set of assertions for testing common data types. In addition, several
different interfaces are provided for running tests and reporting results.
These interfaces currently include:

- Automated: Non-interactive output to xml file
- Basic: Non-interactive flexible programming interface
- Console: Interactive console interface (ansi C)
- Curses: Interactive graphical interface (Unix)

BCUnit is a fork of the defunct project CUnit, with several fixes and patches
applied.

%files -n %{libname}
%{_libdir}/lib%{lname}.so.*
%doc COPYING

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%files -n %{devname}
%{_includedir}/%{oname}
%{_libdir}/lib%{lname}*.so
%{_libdir}/pkgconfig/%{lname}.pc
%{_datadir}/%{oname}
%{_docdir}/%{oname}
%{_mandir}/man3/%{oname}.3*
%doc README
%doc NEWS
%doc TODO
%doc AUTHORS
%doc COPYING


#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{commit}

# Apply all patches
#patch0 -p1 -b .orig
#patch1 -p1 -b .orig
#patch2 -p1 -b .orig
%patch3 -p1 -b .orig
%patch4 -p1 -b .orig

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Debug \
	-DUSE_SHARED_MBEDTLS_LIBRARY:BOOL=ON \
	-DUSE_STATIC_MBEDTLS_LIBRARY:BOOL=OFF \
	-DENABLE_AUTOMATED:BOOL=ON \
	-DENABLE_BASIC:BOOL=ON \
	-DENABLE_CONSOLE:BOOL=ON \
	-DENABLE_CURSES:BOOL=ON \
	-DENABLE_DOC:BOOL=ON \
	-DENABLE_EXAMPLES:BOOL=OFF \
	-DENABLE_MEMTRACE:BOOL=OFF \
	-DENABLE_DEPRECATED:BOOL=OFF
%make

%install
%makeinstall_std -C build

