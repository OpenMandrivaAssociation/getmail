%if %mdvver < 201500
%define __python2 %__python
%define py2_puresitedir %py_puresitedir
%endif

Name:		getmail
Summary:	POP3 mail retriever with reliable Maildir delivery
Version:	4.54.0
Release:	1
License:	GPLv2
Group:		Networking/Mail
URL:		http://pyropus.ca/software/getmail/
Source0:	http://pyropus.ca/software/getmail/old-versions/%{name}-%{version}.tar.gz
%if %mdvver >= 201500
Requires:	python2
%else
Requires:	python
%endif
BuildRequires:	pkgconfig(python2)
BuildArch:	noarch

%description
getmail is intended as a simple replacement for fetchmail for those people
who do not need its various and sundry configuration options, complexities,
and bugs. It retrieves mail from one or more POP3 servers for one or more
email accounts, and reliably delivers into a Maildir specified on a
per-account basis. It can also deliver into mbox files, although this
should not be attempted over NFS. getmail is written entirely in python.

%prep
%setup -q
# workaround a bug in 4.7.8
perl -pi -e 's/^.*getmail\.spec.*$//' setup.py

%build

%install
rm -rf %{buildroot}
%__python2 setup.py install --root=%{buildroot}
rm -Rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

%files
%doc docs/*
%{py2_puresitedir}/getmailcore/
%{py2_puresitedir}/*.egg-info
%{_bindir}/getmail*
%{_mandir}/man1/*

