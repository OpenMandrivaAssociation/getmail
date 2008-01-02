%define name getmail
%define version 4.7.6
%define release %mkrel 1

Name:		%{name}
Summary:	POP3 mail retriever with reliable Maildir delivery
Version:	%{version}
Release:	%{release}

License:	GPL
Group:		Networking/Mail
URL:		http://pyropus.ca/software/getmail/
Source:		http://pyropus.ca/software/getmail/old-versions/%{name}-%{version}.tar.bz2
Requires:	python
BuildRequires:  python-devel 
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot


%description
getmail is intended as a simple replacement for fetchmail for those people
who do not need its various and sundry configuration options, complexities,
and bugs.  It retrieves mail from one or more POP3 servers for one or more
email accounts, and reliably delivers into a Maildir specified on a
per-account basis.  It can also deliver into mbox files, although this
should not be attempted over NFS.  getmail is written entirely in python.


%prep

%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT 
rm -Rf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%{py_puresitedir}/getmailcore/
%{py_puresitedir}/*.egg-info
%_bindir/getmail*
%_mandir/man1/*


