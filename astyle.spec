Summary:	Automatic Indentation Filter
Summary(pl.UTF-8):	Automatyczny filtr wcięć
Name:		astyle
Version:	2.01
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/astyle/%{name}_%{version}_linux.tar.gz
# Source0-md5:	e85b31972c532373a4054842e2149b34
URL:		http://astyle.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artistic Style is a reindenter and reformatter of C++, C and Java
source code.

%description -l pl.UTF-8
Artistic Style to narzędzie do reformatowania kodu z poprawianiem
wcięć dla źródeł w C++, C i Javie.

%prep
%setup -q -n %{name}

%build
%{__make} -C build/gcc \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/gcc install \
	INSTALL=install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

# docdir fixed
mkdir  $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/
mv $RPM_BUILD_ROOT/%{_docdir}/%{name}/html/*.html $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html doc/*.css
%attr(755,root,root) %{_bindir}/*
