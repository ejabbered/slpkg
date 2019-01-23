Title: Repositories - slpkg
Date: 2019-1-18
Authors: dslackw
Slug: repositories


Default available Repositories:


| Repositories                               | Archs       | Versions                             |
| :------------------------------------------| :---------- | :------------------------------------|
| [SBo](http://slackbuilds.org/)             | x86, x86_64 | 13.1 to 14.2 | 
| [Slack](http://www.slackware.com/)         | x86, x86_64 | 3.3  to 14.2, current |
| [Alien's](http://bear.alienbase.nl/mirrors/people/alien/sbrepos/) | x86, x86_64 | 13.0 to 14.2, current |
| [Slacky](http://repository.slacky.eu/)     | x86, x86_64 | 11.0 to 14.2 |
| [Robby's](http://slackware.uk/people/rlworkman/) | x86, x86_64 | 11.0 to 14.2 |
| [Conraid's](http://slack.conraid.net/repository/slackware64-current) | x86_64 | current |
| [Slackonly](https://slackonly.com/) | x86, x86_64 | 14.1, 14.2 |
| [Alien's ktown](http://alien.slackbook.org/ktown/) | x86, x86_64 | 13.37 to 14.2, current |
| [Alien's multi](http://bear.alienbase.nl/mirrors/people/alien/multilib/) | x86, x86_64 | 13.0 to 14.2, current |
| [Slacke E17 and E18](http://ngc891.blogdns.net/pub/) | x86, x86_64, arm | 14.1 | 
| [SalixOS](http://download.salixos.org/) | x86, x86_64 | 13.0 to 14.2 |
| [Slackel](http://www.slackel.gr/repo/) | x86, x86_64 | current |
| [Restricted](http://bear.alienbase.nl/mirrors/people/alien/restricted_slackbuilds/) | x86, x86_64 | 11.0 to 14.2, current |
| [MATE Desktop Environment](http://slackware.org.uk/msb/) | x86, x86_64 | 14.0 to 14.2, current |
| [Cinnamon Desktop Environment](http://slackware.org.uk/csb/) | x86, x86_64 | 14.1, 14.2, current |
 
You can enable more default repositories just edit the file '`/etc/slpkg/repositories.conf`',
by default are 'slack' and 'sbo' repositories is enabled. Please read the [REPOSITORIES.md](https://gitlab.com/dslackw/slpkg/blob/master/REPOSITORIES.md)
file for each of the particularities. Alternative you can run the command '`slpkg repo-enable`' ('`python2-pythondialog`' required).
If a repository is not in the above list, manage the custom repositories with the commands '`repo-add`' and '`repo-remove`'.
