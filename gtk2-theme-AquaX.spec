Summary:	AquaX theme
Summary(pl):	Motyw AquaX
Name:		gtk2-theme-AquaX
Version:	1.0
Release:	2
License:	GPL
Group:		Themes/GTK+
Source0:	http://ep09.pld-linux.org/~havner/AquaX.tar.bz2
# Source0-md5:	3398c6476700f3656174a9a867382839
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AquaX theme based on MacOSX.

%description -l pl
Temat AquaX oparty na MacOSX.

%prep
%setup -q -n AquaX

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/AquaX
cp -R gtk* $RPM_BUILD_ROOT%{_datadir}/themes/AquaX/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README READMETOO Changelog
%{_datadir}/themes/AquaX
