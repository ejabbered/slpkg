Title: Manpage
Date: 2019-1-18
Authors: dslackw
Slug: manpage


##### slpkg manpage (8)


```
Slpkg(14)                                          slpkg                                          Slpkg(14)

NAME
       Slpkg is a user-friendly package manager for Slackware installations

SYNOPSIS
       Usage: slpkg [COMMANDS|OPTIONS] {repository|package...}

                    Commands:
                    [update, --only=[...]]
                    [upgrade, --only=[...]]
                    [repo-add [repository name] [URL]]
                    [repo-remove [repository]]
                    [repo-enable]
                    [repo-list]
                    [repo-info [repository]]
                    [update [slpkg]]
                    [health, --silent]
                    [deps-status, --tree, --graph=[type]]
                    [new-config]

                    Optional arguments:
                    [-h] [-v]
                    [-a [script] [sources...]]
                    [-b [package...] --add, --remove,
                        [list]]
                    [-q [package...] --add, --remove,
                        [list, build, install, build-install]]
                    [-g [print, edit, reset]]
                    [-l [repository], --index, --installed, --name]
                    [-c [repository], --upgrade, --rebuild, --skip=[...],
                                      --resolve-off, --checklist]
                    [-s [repository] [package...], --rebuild, --reinstall,
                                                   --resolve-off, --download-only,
                                                   --directory-prefix=[dir],
                                                   --case-ins, --patches]
                    [-t [repository] [package], --check-deps, --graph=[type],
                                                --case-ins]
                    [-p [repository] [package], --color=[]]
                    [-n [SBo package], --checklist, --case-ins]
                    [-F [package...], --case-ins]
                    [-f [package...], --case-ins, --third-party]
                    [-i [options] [package...]]
                    [-u [options] [package...]]
                    [-r [options] [package...], --deps, --check-deps, --tag,
                                                --checklist]
                    [-d [package...]]

DESCRIPTION
       Slpkg  is a powerful software package manager that installs, updates, and removes packages on Slack‐
       ware based systems. It automatically computes dependencies and figures out what things should  occur
       to  install  packages.  Slpkg makes it easier to maintain groups of machines without having to manu‐
       ally update.

GLOBAL OPTIONS
       -v, --version

       Print the version of program and exit.

COMMANDS
       The following commands are available.

   update, create and update packages list
       slpkg update, --only=[repositories...]

       Used to re-synchronize the package lists and create some important files.   This  command  must  run
       every new repository is added or new updates is available.

       Additional options:

       --only=[repositories...] : Update at specifically repositories separate by comma.

   upgrade, recreate packages list
       slpkg upgrade, --only=[repositories...]

       It  is sometimes useful to create all of the base file from the beginning so this command delete all
       the package lists and recreated.

       Additional options:

       --only=[repositories...] : Update at specifically repositories separate by comma.

   repo-add, add custom repository
       slpkg repo-add <repository name> <URL>

       Add custom binary repository. The repositories will be added to this command should contain at least
       the  files  "PACKAGES.TXT"  and  "CHECKSUMS.md5"  and  optional file "ChangeLog.txt" used to control
       changes.

   repo-remove, remove custom repository
       slpkg repo-remove <repository>

       Remove custom repository by name.

   repo-enable, enable or disable repositories
       slpkg repo-enable

       Enable or disable repositories via dialog utility (require python2-pythondialog)

   repo-list, repositories list
       slpkg repo-list

       Lists all enabled or disabled repositories.

   repo-info, repository information
       slpkg repo-info <repository>

       View repository information.

   update slpkg, update slpkg itself
       slpkg update slpkg

       You can check for new versions and update slpkg itself.

   health, health check installed packages
       slpkg health, --silent

       Check file list from packages of files installed.

       Additional options:

       --silent : Print only errors.

   deps-status, print dependencies status
       slpkg deps-status --graph=[type]

       Print dependencies status used by packages. Prerequisite  packages  have  been  installed  with  the
       option "# slpkg -s <repository> <packages>".

       Additional options:

       --graph=[type]  :  Drawing dependencies diagram. (example for type: ascii, image.x11, image.png etc.
       Require pygraphviz)

       --tree : Switch to tree view.

   new-config, manage .new configuration files
       slpkg new-config

       This command searches for .new configuration files in /etc/ path and ask the  user  what  todo  with
       those files.

OPTIONS
       The following arguments are available.

   -a, --autobuild, auto build packages
       slpkg -a <script.tar.gz> <sources>

       If  you already have download the script and source with this argument you can build Slackware pack‐
       age from source quickly and easy. Slpkg will grab checksum from the .info file to make control if he
       does  not  agree  with  the versions you will get the wrong message. If you want switch off checksum
       from the configuration file.

   -b, --blacklist, add, remove, view packages in blacklist
       slpkg -b <name of packages> --add, --remove, list

       Add, remove or listed packages from blacklist file.  The  settings  here  affect  all  repositories.
       Remove  all  packages  from  blacklist  use argument like "# slpkg -b --remove". Use asterisk "*" to
       match pagkages like "# slpkg -b py* --add", this add all installed packages with starts string  "py"
       or "# slpkg -b multi:*multilib* --add", this add all multilib packages from repository "multi".

   -q, --queue, add, remove, view packages in queue
       slpkg -q <names of packages> --add, --remove

       slpkg -q list, build, install, build-install

       Add,  remove  and  listed sbo packages from queue. This argument is very useful if you want to build
       and install multiple packages together. Note the correct order if there  are  dependencies.  If  you
       want  to  remove  all  the  packages from the list run "# slpkg -q --remove".  (these arguments only
       working for the sbo repository) Build or install or build and install packages are queued.

   -g, --config, configuration file management
       slpkg -g print, edit, reset

       Print, reset or edit configuration file.

   -l, --list, list of installed packages
       slpkg -l <repository>, --index, --installed, --name

       Print a list of all available packages from repository, index or print only  packages  installed  on
       the system. Support command "grep" like "# slpkg -l sbo | grep python".

       Additional options:

       --index : Count packages per page.

       --installed : Highlight installed packages.

       --name : Print package name only.

   -c, --check, check if your packages is up to date
       slpkg -c <repository> --upgrade --rebuild --skip=[packages...], --resolve-off, --checklist

       Check  your  packages  if up to date. Slackware patches repository works independently of the others
       i.e not need before updating the list of packages by choosing "# slpkg update", works directly  with
       the official repository and so always you can have updated your system.

       Additional options:

       -c  : Check ChangeLog.txt files for changes.

       --upgrade : Check and install packages for upgrade.

       --rebuild : Rebuild packages from sbo repository.

       --resolve-off : Switch off automatic resolve dependencies.

       --skip=[packages...]  :  Skip  packages  from  upgrade  separate  by  comma  like  "#  slpkg  -c sbo
       --skip=jdk,pep8,pip" (See REGEX).

       --checklist : Enable dialog utility and checklist option. (Require python2-pythondialog)

   -s, --sync, synchronize packages, download, build and install package with all dependencies
       slpkg -s <repository> <names of packages>, --resolve-off, --case-ins, --patches

       Installs or upgrade packages from the repositories with automatically resolving all dependencies  of
       the package.

       Additional options:

       --rebuild : Rebuild packages from sbo repository.

       --reinstall : Reinstall binary packages from repositories.

       --resolve-off : Switch off automatic resolve dependencies.

       --download-only : Download packages without install.

       --directory-prefix=[path/to/dir/] : Download packages in specific directory.

       --case-ins : Search package name in repository with case insensitive.

       --patches : Switch to patches directory, only for slack repository.

   -t, --tracking, tracking dependencies
       slpkg -t <repository> <name of package>, --check-deps, --graph=[type] --case-ins

       Tracking  all dependencies of that package.  The sequence shown is that you must follow to correctly
       install package.  Also you can check if the installed package has all the required dependencies.

       Additional options:

       --check-deps : Check if installed packages used by other packages.

       --graph=[type] : Drawing dependencies graph. (example for type:  ascii,  image.x11,  image.png  etc.
       Require pygraphviz)

       --case-ins : Search package name in repository with case insensitive.

   -p, --desc, print packages description
       slpkg -p <repository> <name of package>, --color=[]

       Print  package  description from remote repository with color. Available colors: red, green, yellow,
       cyan, grey

       Additional options:

       --color=[] : Change color print.

   -F, --FIND, find packages from repositories
       slpkg -F <names of packages>, --case-ins

       Find packages from all repositories are enabled. Useful command to find all available  packages  per
       repository.

       Additional options:

       --case-ins : Search package name in repository with case insensitive.

   -f, --find, find installed packages
       slpkg -f <names of packages>, --case-ins, --third-party

       Find  installed packages with view total file size.  Example you can view all installed sbo packages
       like "# slpkg -f _SBo".

       Additional options:

       --case-ins : Search package name with case insensitive.

       --third-party : View all the third-party packages.

   -n, --network, view SBo packages
       slpkg -n <name of package>, <[pattern], --checklist>, --case-ins

       View complete slackbuilds.org site in your terminal. Read file, download, build or install etc.  Use
       "--checklist" additional option to load all repository, example: "# slpkg -n --checklist".

       Additional options:

       --checklist : Enable dialog utility and checklist option. (Require python2-pythondialog)

       --case-ins : Search package name in repository with case insensitive.

   -i, --installpkg, install Slackware binary packages
       slpkg  -i  [--warn,  --md5sum,  --root  /otherroot,  --infobox,  --menu,  --terse, --ask, --priority
       ADD|REC|OPT|SKP, --tagfile /somedir/tagfile] <packages.t?z>

       Installs single binary packages designed for use with the Slackware  Linux  distribution  into  your
       system. More information please read "man installpkg".

   -u, --upgradepkg, install-upgrade Slackware binary packages with new
       slpkg -u [--dry-run, --install-new, --reinstall, --verbose] <packages.t?z>

       Normally  upgrade only upgrades packages that are already installed on the system, and will skip any
       packages that do  not  already  have  a  version  installed.   More  information  please  read  "man
       upgradepkg".

   -r, --removepkg, remove previously installed Slackware binary packages
       slpkg -r [-copy, -keep, -preserve, -warn] <names of packages>, --deps, --check-deps, --tag, --check‐
       list, --third-party

       Removes a previously installed Slackware package, while writing a progress report  to  the  standard
       output.  A  package  may  be  specified  either  by  the  full  package name (as you'd see listed in
       /var/log/packages/), or by the base package name. If installed packages with  command  "#  slpkg  -s
       <repo>  <packages>" then write a file in /var/log/slpkg/dep/ with all dependencies and it allows you
       can remove them all together.  More information please read "man removepkg".

       Additional options:

       --deps : Remove packages with dependencies.

       --check-deps : Check if installed packages used by other packages.

       --tag : Remove packages with by TAG.

       --checklist : Enable dialog utility and checklist option. (Require python2-pythondialog)

       --third-party : Remove all the third-party packages. (Be sure update the package lists before)

   -d, --display, display the installed packages contents and file list
       slpkg -d <names of packages>

       Display the installed Slackware packages contents and file list with all descriptions.

HELP OPTION
       Specifying the help option displays help for slpkg itself, or a command.
       For example:
         slpkg --help - display help for slpkg

DEFAULT REPOSITORIES
        slackware.com = "slack"
        SlackBuilds.org = "sbo"
        Alien's = "alien"
        slacky.eu = "slacky"
        rworkman's = "rlw"
        Conraid's = "conrad"
        slackonly.com = "slonly"
        Alien's ktown = "ktown{latest}"
        Alien's multilib = "multi"
        Slacke E17 and E18 = "slacke{18}"
        SalixOS = "salix"
        Slackel.gr = "slackel"
        Alien's restricted = "rested"
        MATE Desktop Environment = "msb{1.18}"
        Cinnamon Desktop Environment = "csb"
        Connochaetos slack-n-free = "connos"
        Microlinux mles = "mles"

        Default enable repository is "slack" and "sbo".
        Add or remove default repository in configuration file "/etc/slpkg/repositories.conf".
        Read REPOSITORIES file for particularities.

COLORS
        red, green, yellow, cyan, grey

REGEX
        For options "--skip=" and blacklist file.

        All packages starts with: "string*"
        All packages ends with: "*string"
        All packages include: "*string*"

PASS VARIABLES TO SCRIPT
        If you want to pass variables to the script exported as:
        Usage: <NAME_VARIABLE=value>

        Example:
        "# export FFMPEG_X264=yes FFMPEG_LAME=yes"

FILES
       /etc/slpkg/slpkg.conf
            General configuration of slpkg

       /etc/slpkg/repositories.conf
            Configuration file for repositories

       /etc/slpkg/blacklist
            List of packages to skip

       /etc/slpkg/slackware-mirrors
            List of Slackware Mirrors

       /etc/slpkg/default-repositories
            List of default repositories

       /etc/slpkg/custom-repositories
            List of custom repositories

       /etc/slpkg/rlworkman.deps
            Rworkman's repository dependencies

       /etc/slpkg/pkg_security
            List of packages for security reasons

       /var/log/slpkg
            ChangeLog.txt repositories files
            SlackBuilds logs and dependencies files

       /var/lib/slpkg
            PACKAGES.TXT files
            SLACKBUILDS.TXT files
            CHECKSUMS.md5 files
            FILELIST.TXT files

       /tmp/slpkg
            Slpkg temporary downloaded files and build packages

AUTHOR
       Dimitris Zlatanidis <d.zlatanidis@gmail.com>

HOMEPAGE
       https://gitlab.com/dslackw/slpkg

COPYRIGHT
       Copyright © 2014-2019 Dimitris Zlatanidis

SEE ALSO
       installpkg(8), upgradepkg(8), removepkg(8), pkgtool(8), slackpkg(8), explodepkg(8), makepkg(8).

2019"                                                01                                           Slpkg(14)
```
