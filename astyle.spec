#
# Conditional build:
%bcond_without	java		# Java library
%bcond_without	static_libs	# static library

Summary:	Automatic Indentation Filter
Summary(pl.UTF-8):	Automatyczny filtr wcięć
Name:		astyle
Version:	3.1
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/astyle/%{name}_%{version}_linux.tar.gz
# Source0-md5:	7712622f62661b1d8cb1062d7fedc390
URL:		http://astyle.sourceforge.net/
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artistic Style is a reindenter and reformatter of C++, C and Java
source code.

%description -l pl.UTF-8
Artistic Style to narzędzie do reformatowania kodu z poprawianiem
wcięć dla źródeł w C++, C i Javie.

%package java
Summary:	AStyle library for Java
Summary(pl.UTF-8):	Biblioteka AStyle dla Javy
Group:		Libraries

%description java
AStyle library for Java.

%description java -l pl.UTF-8
Biblioteka AStyle dla Javy.

%package devel
Summary:	Header file for AStyle library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki AStyle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header file for AStyle library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki AStyle.

%package static
Summary:	Static AStyle library
Summary(pl.UTF-8):	Statyczna biblioteka AStyle
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AStyle library.

%description static -l pl.UTF-8
Statyczna biblioteka AStyle.

%prep
%setup -q -n %{name}

%build
%{__make} -C build/gcc astyle shared %{?with_static_libs:static} %{?with_java:java} \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/gcc install \
	INSTALL=install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}
install build/gcc/bin/libastyle.so.*.*.* $RPM_BUILD_ROOT%{_libdir}
ln -sf $(basename build/gcc/bin/libastyle.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libastyle.so
%if %{with java}
install build/gcc/bin/libastylej.so.*.*.* $RPM_BUILD_ROOT%{_libdir}
ln -sf $(basename build/gcc/bin/libastylej.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libastylej.so
%endif
%if %{with static_libs}
cp -p build/gcc/bin/libastyle.a $RPM_BUILD_ROOT%{_libdir}
%endif
cp -p src/astyle.h $RPM_BUILD_ROOT%{_includedir}

/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md doc/{*.html,*.css}
%attr(755,root,root) %{_bindir}/astyle
%attr(755,root,root) %{_libdir}/libastyle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libastyle.so.3

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libastylej.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libastylej.so.3
%attr(755,root,root) %{_libdir}/libastylej.so
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libastyle.so
%{_includedir}/astyle.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libastyle.a
%endif
