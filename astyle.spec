Summary:	Automatic Indentation Filter
Summary(pl):	Automatyczny filtr wciêæ
Name:		astyle
Version:	1.15.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}_%{version}.zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artistic Style is a reindenter and reformatter of C++, C and Java
source code.

%prep
%setup -q -c

%build
%{__make} \
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
