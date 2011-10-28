Name:		getmail
Summary:	POP3 mail retriever with reliable Maildir delivery
Version:	4.22.1
Release:	%mkrel 1
License:	GPL
Group:		Networking/Mail
URL:		http://pyropus.ca/software/getmail/
Source:		http://pyropus.ca/software/getmail/old-versions/%{name}-%{version}.tar.gz
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
# workaround a bug in 4.7.8
perl -pi -e 's/^.*getmail\.spec.*$//' setup.py 

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=%{buildroot}
rm -Rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%{py_puresitedir}/getmailcore/
%{py_puresitedir}/*.egg-info
%{_bindir}/getmail*
%{_mandir}/man1/*


