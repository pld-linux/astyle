Summary:	Automatic Indentation Filter
Summary(pl.UTF-8):	Automatyczny filtr wcięć
Name:		astyle
Version:	1.22
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/astyle/%{name}_%{version}_linux.tar.gz
# Source0-md5:	f319ee4e2538f5e6255211975b4e36cc
URL:		http://astyle.sourceforge.net/
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
%{__make} -C buildgcc \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C buildgcc install \
	INSTALL=install \
	prefix=$RPM_BUILD_ROOT%{_prefix}
        
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_bindir}/*
