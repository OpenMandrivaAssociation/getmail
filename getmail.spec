Name:		getmail
Summary:	POP3 mail retriever with reliable Maildir delivery
Version:	4.27.0
Release:	1
License:	GPLv2
Group:		Networking/Mail
URL:		http://pyropus.ca/software/getmail/
Source0:	http://pyropus.ca/software/getmail/old-versions/%{name}-%{version}.tar.gz
Requires:	python
BuildRequires:	python-devel
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
python setup.py install --root=%{buildroot}
rm -Rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

%files
%doc docs/*
%{py_puresitedir}/getmailcore/
%{py_puresitedir}/*.egg-info
%{_bindir}/getmail*
%{_mandir}/man1/*


%changelog
* Mon May 21 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 4.27.0-1
+ Revision: 799748
- update to 4.27.0

* Tue Dec 06 2011 Andrey Bondrov <abondrov@mandriva.org> 4.23.0-1
+ Revision: 738378
- New version 4.23.0

* Fri Oct 28 2011 Andrey Bondrov <abondrov@mandriva.org> 4.22.1-1
+ Revision: 707710
- New version 4.22.1

* Wed Apr 20 2011 Michael Scherer <misc@mandriva.org> 4.20.2-1
+ Revision: 656140
- update to new version 4.20.2

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 4.20.0-2mdv2011.0
+ Revision: 592386
- rebuild for python 2.7

* Tue Aug 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.20.0-1mdv2011.0
+ Revision: 572615
- update to 4.20.0
- don't define name, version and release on top of spec. (cosmetic)

* Thu Jan 07 2010 Frederik Himpe <fhimpe@mandriva.org> 4.16.0-1mdv2010.1
+ Revision: 487286
- update to new version 4.16.0

* Thu Dec 24 2009 Frederik Himpe <fhimpe@mandriva.org> 4.14.0-1mdv2010.1
+ Revision: 481981
- update to new version 4.14.0

* Tue Nov 10 2009 Michael Scherer <misc@mandriva.org> 4.13.0-1mdv2010.1
+ Revision: 463856
- update to new version 4.13.0

* Sun Aug 23 2009 Frederik Himpe <fhimpe@mandriva.org> 4.11.0-1mdv2010.0
+ Revision: 420169
- update to new version 4.11.0

* Sat Aug 08 2009 Frederik Himpe <fhimpe@mandriva.org> 4.10.0-1mdv2010.0
+ Revision: 411745
- update to new version 4.10.0

* Wed Jun 03 2009 Michael Scherer <misc@mandriva.org> 4.9.0-1mdv2010.0
+ Revision: 382355
- update to new version 4.9.0

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 4.8.4-2mdv2009.1
+ Revision: 325244
- rebuild

* Wed Nov 05 2008 Michael Scherer <misc@mandriva.org> 4.8.4-1mdv2009.1
+ Revision: 300120
- update to new version 4.8.4

* Fri Aug 15 2008 Michael Scherer <misc@mandriva.org> 4.8.3-1mdv2009.0
+ Revision: 272296
- update to new version 4.8.3

* Mon Aug 04 2008 Frederik Himpe <fhimpe@mandriva.org> 4.8.2-1mdv2009.0
+ Revision: 263383
- update to new version 4.8.2

* Wed May 14 2008 Michael Scherer <misc@mandriva.org> 4.8.1-1mdv2009.0
+ Revision: 207255
- update to new version 4.8.1

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 4.8.0-1mdv2008.1
+ Revision: 177095
- new version

* Mon Feb 11 2008 Michael Scherer <misc@mandriva.org> 4.7.8-1mdv2008.1
+ Revision: 165072
- new version 4.7.8
- use gz instead of bz2

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Michael Scherer <misc@mandriva.org> 4.7.6-1mdv2008.0
+ Revision: 63635
- update to 4.7.6, fix #32557

* Sun Jul 01 2007 Michael Scherer <misc@mandriva.org> 4.7.5-1mdv2008.0
+ Revision: 46489
- 4.7.5
- remove old doc directory, new doc policy on cooker

* Wed Apr 25 2007 Lenny Cartier <lenny@mandriva.org> 4.7.4-1mdv2008.0
+ Revision: 18191
- Update to 4.7.4

* Sun Apr 22 2007 Michael Scherer <misc@mandriva.org> 4.7.3-1mdv2008.0
+ Revision: 16979
- update to 4.7.3


* Wed Feb 21 2007 Lenny Cartier <lenny@mandriva.com> 4.7.2-1mdv2007.0
+ Revision: 123707
- Update to 4.7.2

* Tue Feb 06 2007 Lenny Cartier <lenny@mandriva.com> 4.7.1-1mdv2007.1
+ Revision: 116587
- Update to 4.7.1

* Thu Jan 25 2007 Lenny Cartier <lenny@mandriva.com> 4.7.0-2mdv2007.1
+ Revision: 113277
- Fix filelist
- Update to 4.7.0
- Update to 4.6.7

* Tue Dec 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 4.6.6-2mdv2007.1
+ Revision: 99221
- Rebuild against new python

  + Lenny Cartier <lenny@mandriva.com>
    - Update to 4.6.6

* Wed Oct 04 2006 Michael Scherer <misc@mandriva.org> 4.6.4-1mdv2007.1
+ Revision: 62833
- clean specfiles from comment, and old part of the spec
- fix build on x86_64, with correct macros
- update to 4.6.4
- Import getmail

* Sun Jul 09 2006 Michael Scherer <misc@mandriva.org> 4.6.3-1
- New release 4.6.3

* Wed Jun 14 2006 Lenny Cartier <lenny@mandriva.com> 4.6.2-1mdv2007.0
- 4.6.2

* Fri Jun 02 2006 Lenny Cartier <lenny@mandriva.com> 4.6.1-1mdv2007.0
- 4.6.1

* Fri Apr 14 2006 Lenny Cartier <lenny@mandriva.com> 4.6.0-1mdk
- 4.6.0

* Thu Feb 09 2006 Lenny Cartier <lenny@mandriva.com> 4.5.3-1mdk
- 4.5.3

* Wed Feb 08 2006 Lenny Cartier <lenny@mandriva.com> 4.5.2-1mdk
- 4.5.2

* Mon Jan 02 2006 Lenny Cartier <lenny@mandriva.com> 4.5.0-1mdk
- 4.5.0

* Fri Dec 02 2005 Lenny Cartier <lenny@mandriva.com> 4.4.3-1mdk
- 4.4.3

* Mon Nov 14 2005 Michael Scherer <misc@mandriva.org> 4.4.2-1mdk
- New release 4.4.2

* Fri Nov 11 2005 Michael Scherer <misc@mandriva.org> 4.4.1-1mdk
- New release 4.4.1

* Wed Nov 09 2005 Michael Scherer <misc@mandriva.org> 4.4.0-1mdk
- New release 4.4.0

* Wed Oct 26 2005 Michael Scherer <misc@mandriva.org> 4.3.13-1mdk
- New release 4.3.13
- %%mkrel
- remove -q for %%prep
- fix BuildRequires

* Sat Jun 18 2005 Lenny Cartier <lenny@mandriva.com> 4.3.11-1mdk
- 4.3.11

* Sun May 22 2005 Lenny Cartier <lenny@mandriva.com> 4.3.10-1mdk
- 4.3.10

* Tue Apr 05 2005 Lenny Cartier <lenny@mandrakesoft.com> 4.3.5-1mdk
- 4.3.5

* Mon Feb 21 2005 Lenny Cartier <lenny@mandrakesoft.com> 4.3.3-1mdk
- 4.3.3

* Sun Feb 06 2005 Lenny Cartier <lenny@mandrakesoft.com> 4.3.2-1mdk
- 4.3.2

* Wed Jan 19 2005 Lenny Cartier <lenny@mandrakesoft.com> 4.3.1-1mdk
- 4.3.1

* Mon Jan 10 2005 Lenny Cartier <lenny@mandrakesoft.com> 4.3.0-1mdk
- 4.3.0

* Mon Jan 03 2005 Lenny Cartier <lenny@mandrakesoft.com> 4.2.6-1mdk
- 4.2.6

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 4.2.4-2mdk
- Rebuild for new python

* Mon Nov 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.2.4-1mdk
- 4.2.4

* Tue Oct 12 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.2.1-1mdk
- 4.2.1

* Wed Sep 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.2.0-1mdk
- 4.2.0

* Thu Sep 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.1.3-1mdk
- 4.1.3

* Thu Aug 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.1.0-1mdk
- 4.1.0

* Fri Aug 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.0.12-1mdk
- 4.0.12

* Sat Aug 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.0.10-1mdk
- 4.0.10

* Tue Aug 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.0.8-1mdk
- 4.0.8

* Fri Aug 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.0.6-1mdk
- 4.0.6

* Wed Aug 04 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.0.4-1mdk
- 4.0.4

* Tue Jul 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.0.1-1mdk
- 4.0.1

* Sun Jul 25 2004 Michael Scherer <misc@mandrake.org> 4.0.0-1mdk
- New release 4.0.0
- change url

* Sat May 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.2.4-1mdk
- 3.2.4

* Tue Mar 23 2004 Michael Scherer <misc@mandrake.org> 3.2.2-1mdk
- 3.2.2
- use /usr/share/getmail/

