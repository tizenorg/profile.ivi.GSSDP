# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       gssdp
Summary:    GSSDP implements resource discovery and announcement over SSDP
Version:    0.14.2
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.gupnp.org
Source0:    http://download.gnome.org/sources/%{name}/0.14/%{name}-%{version}.tar.bz2
Requires:   dbus
Requires:   libsoup2.4
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)


%description
GSSDP implements resource discovery and announcement over SSDP and is part
of gUPnP.  GUPnP is an object-oriented open source framework for creating
UPnP devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible. GSSDP
implements resource discovery and announcement over SSDP.



%package devel
Summary:    Development package for gssdp
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for gssdp.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING
%{_libdir}/*.so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc %{_datadir}/gtk-doc/html/gssdp
%{_libdir}/*.so
%{_libdir}/pkgconfig/gssdp-1.0.pc
%{_includedir}/gssdp-1.0
# << files devel


