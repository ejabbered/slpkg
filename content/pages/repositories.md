Title: Repositories - slpkg
Date: 2019-1-18
Authors: dslackw
Slug: repositories


Default available Repositories:


- [SBo](http://slackbuilds.org/)
Arch: {x86, x86_64}
Versions: {13.1, 13.37, 14.0, 14.1, 14.2}
- [Slack](http://www.slackware.com/)
Arch: {x86, x86_64}
Versions: {3.3, 8.1, 9.0, 9.1, 10.0, 10.1, 10.2, 11.0, 12.0, 12.2, 13.0, 13.37, 14.0, 14.1, 14.2, current}
- [Alien's](http://bear.alienbase.nl/mirrors/people/alien/sbrepos/)
Arch: {x86, x86_64}
Versions: {13.0, 13.1, 13.37, 14.0, 14.1, 14.2, current}
- [Slacky](http://repository.slacky.eu/)
Arch: {x86, x86_64}
Versions: {11.0, 12.0, 12.1, 12.2, 13.0, 13.1, 13.37, 14.0, 14.1, 14.2}
- [Robby's](http://slackware.uk/people/rlworkman/)
Arch: {x86, x86_64}
Versions: {11.0, 12.0, 12.1, 12.2, 13.0, 13.1, 13.37, 14.0, 14.1, 14,2}
- [Conraid's](http://slack.conraid.net/repository/slackware64-current)
Arch: {x86_64}
Versions: {current}
- [Slackonly](https://slackonly.com/)
Arch: {x86, x86_64}
Versions: {14.1, 14.2}
- [Alien's ktown](http://alien.slackbook.org/ktown/)
Arch: {x86, x86_64}
Versions: {13.37, 14.0, 14.1, 14.2, current}
- [Alien's multi](http://bear.alienbase.nl/mirrors/people/alien/multilib/)
Arch: {x86_64}
Versions: {13.0, 13.1, 13.37, 14.0, 14.1, 14.2, current}
- [Slacke E17 and E18](http://ngc891.blogdns.net/pub/)
Arch: {x86, x86_64, arm}
Versions: {14.1}
- [SalixOS](http://download.salixos.org/)
Arch: {x86, x86_64}
Versions: {13.0, 13.1, 13.37, 14.0, 14.1, 14.2}
- [Slackel](http://www.slackel.gr/repo/)
Arch: {x86, x86_64}
Versions: {current}
- [Restricted](http://bear.alienbase.nl/mirrors/people/alien/restricted_slackbuilds/)
Arch: {x86, x86_64}
Versions: {11.0, 12.0, 12.1, 12.2, 13.0, 13.1, 13.37, 14.0, 14,1, 14.2, current}
- [MATE Desktop Environment](http://slackware.org.uk/msb/)
Arch: {x86, x86_64}
Versions: {14.0, 14,1, 14.2, current}
- [Cinnamon Desktop Environment](http://slackware.org.uk/csb/)
Arch: {x86, x86_64}
Versions: {14,1, 14.2, current}

You can enable more default repositories just edit the file '`/etc/slpkg/repositories.conf`',
by default are 'slack' and 'sbo' repositories is enabled. Please read the [REPOSITORIES](https://gitlab.com/dslackw/slpkg/blob/master/REPOSITORIES.md) file for each of the particularities.
Alternative you can run the command '`slpkg repo-enable`' ('`python2-pythondialog`' required).
If a repository is not in the above list, manage the custom repositories with the commands
'`repo-add`' and '`repo-remove`'.
