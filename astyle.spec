Summary:	Automatic Indentation Filter
Summary(pl.UTF-8):   Automatyczny filtr wcięć
Name:		astyle
Version:	1.15.3
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/astyle/%{name}_%{version}.zip
# Source0-md5:	4d8adbcd8703aea00fcd2670be090ddd
URL:		http://astyle.sourceforge.net/
Patch0:		%{name}-Makefile.patch
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artistic Style is a reindenter and reformatter of C++, C and Java
source code.

%description -l pl.UTF-8
Artistic Style to narzędzie do reformatowania kodu z poprawianiem
wcięć dla źródeł w C++, C i Javie.

%prep
%setup -q -c
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install astyle $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc astyle.html astyle_release_notes.html
%attr(755,root,root) %{_bindir}/*
