Name:		getmail
Summary:	POP3 mail retriever with reliable Maildir delivery
Version:	6.8
Release:	1
License:	GPLv2
Group:		Networking/Mail
URL:		http://getmail6.org
Source0:	https://github.com/getmail6/getmail6/archive/v6.8.tar.gz
Requires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
BuildArch:	noarch

%description
getmail is intended as a simple replacement for fetchmail for those people
who do not need its various and sundry configuration options, complexities,
and bugs. It retrieves mail from one or more POP3 servers for one or more
email accounts, and reliably delivers into a Maildir specified on a
per-account basis. It can also deliver into mbox files, although this
should not be attempted over NFS. getmail is written entirely in python.

%prep
%setup -qn getmail6-%{version}

%build

%install
rm -rf %{buildroot}
%__python3 setup.py install --root=%{buildroot}
rm -Rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

%files
%doc docs/*
%{py3_puresitedir}/getmailcore/
%{py3_puresitedir}/*.egg-info
%{_bindir}/getmail*
%{_mandir}/man1/*

