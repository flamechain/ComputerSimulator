import sys, os, shutil
from colorama import Fore, Back, Style

RELEASE = 'null'
DEBUG = 'null'
DEFAULT_DIR = None
INSTALLED = None
INSTALL_DIR = None
TYPE = None
FORCE = False
CONFIG_FILE = './../setup_settings.txt'
SETTINGS = sys.argv[1:]
DIR_LINE = None

with open(CONFIG_FILE, 'r') as f:
    lines = f.readlines()

for i in lines:
    if i.startswith(':DEFAULT_PATH:'):
        DEFAULT_DIR = i.replace(':DEFAULT_PATH:', '').strip('\n').replace(' ', '').replace('*', ' ')

        if DEFAULT_DIR.startswith('='):
            DEFAULT_DIR = DEFAULT_DIR.strip('=')

        else:
            DEFAULT_DIR = None

    elif i.startswith(':INSTALLED:'):
        if i.replace(':INSTALLED:', '').replace(' ', '') == '=false':
            INSTALLED = False

        else:
            INSTALLED = True

    elif i.startswith(':INSTALL_DIR:'):
        DIR_LINE = i
        if i.replace(':INSTALL_DIR:', '').replace(' ', '').replace('*', ' ').strip('\n') == '=null':
            INSTALL_DIR = None
        else:
            INSTALL_DIR = i.replace(':INSTALL_DIR:', '').replace(' ', '').replace('*', ' ').strip('=').strip('\n')
            proceed = input(Fore.YELLOW + 'WARNING: Files already copied into ' + Style.RESET_ALL + INSTALL_DIR + Fore.YELLOW + '. Proceed? (Y/N) ' + Style.RESET_ALL).upper()
            if proceed == 'N':
                sys.exit()
            elif proceed == 'Y':
                with open(CONFIG_FILE, 'w') as f:
                    lines.pop(lines.index(i))
                    lines.append(':INSTALL_DIR: = null')
                    f.write(''.join(lines))
            else:
                print('Unknown Option.')
                sys.exit()

USAGE = 'Usage: setup.py [options]\n\nOptions:\n  -r, --release    Install type release\n' \
            '  -d, --debug      Install type debug (may be unstable)\n' \
            '  -p, --path       Custom path for the install directory\n' \
            '  -f, --force      Bypasses permissions and can wipe folders (would not advise)\n\n' \
            '  Default Path: %s' % DEFAULT_DIR

directory = DEFAULT_DIR

if '-r' in SETTINGS or '--release' in SETTINGS:
    if TYPE is not None:
        print(Fore.RED + '\nERROR: You must only chose 1 install type' + Style.RESET_ALL)
        sys.exit()

    TYPE = RELEASE

if '-d' in SETTINGS or '--debug' in SETTINGS:
    if TYPE is not None:
        print(Fore.RED + '\nERROR: You must only chose 1 install type' + Style.RESET_ALL)
        sys.exit()

    TYPE = DEBUG

if '-f' in SETTINGS or '--force' in SETTINGS:
    FORCE = True

if TYPE is None:
    print(USAGE + Fore.YELLOW + '\n\nWARNING: You must select an install type for confirmation' + Style.RESET_ALL)
    if len(SETTINGS) == 0:
        sys.exit()

if SETTINGS:
    unknown = []
    path = False
    unvar = ''

    for i in SETTINGS:
        if path:
            directory = i
            path = False
            continue

        if i in ['-r', '--release', '-d', '--debug', '-p', '--path', '-f', '--force']:
            if i in ['-p', '--path']:
                path = True

            continue

        unknown.append(i)

    for i in range(len(unknown)-2):
        unvar += unknown[i] + ', '

    if len(unknown) > 0:
        unvar += unknown[-1]
        if TYPE != None:
            print(USAGE + Fore.RED + f'\n\nERROR: Unknown settings: {unvar}')
            sys.exit()
        print(Fore.RED + f'ERROR: Unknown settings: {unvar}')
        sys.exit()

if FORCE:
    if os.path.isdir(directory):
        print('Wiping install directory . . .')

        try:
            os.rmdir(directory)

        except:
            print(Fore.RED + 'ERROR: Failed wipe directory. Directory status: Not Removed' + Style.RESET_ALL)
            sys.exit()

        try:
            os.mkdir(directory)

        except:
            print(Fore.RED + 'ERROR: Failed wipe directory. Directory status: Removed' + Style.RESET_ALL)
            sys.exit()

        print('Directory Wiped')

    else:
        print('Making Directory . . .')

        try:
            os.mkdir(directory)
    
        except:
            print(Fore.RED + f'ERROR: Failed to create directory ({directory}).' + Style.RESET_ALL)
            sys.exit()

        print('Directory Created')
        print('Copying Files . . .')

        try:
            shutil.copytree('./../../../MNLv2', directory + '\\MNL')

        except:
            print(Fore.RED + 'ERROR: Failed to copy files.' + Style.RESET_ALL)
            sys.exit()

        print('Files Copied into ' + directory)
        sys.exit()

    print('Copying Files . . .')

    try:
        shutil.copytree('./../../../MNLv2', directory + '\\MNL')

    except:
        print(Fore.RED + 'ERROR: Failed to copy files.' + Style.RESET_ALL)
        sys.exit()

    print('Files Copied into ' + directory)
    with open(CONFIG_FILE, 'w') as f:
        lines.pop(lines.index(DIR_LINE))
        lines.append(':INSTALL_DIR: = ' + directory)
        f.write(''.join(lines))
    sys.exit()

else:
    if os.path.isdir(directory):
        proceed = input(Fore.YELLOW + 'WARNING: Directory ' + directory + ' exists. Wipe folder, or continue copying files? (W/C) ' + Style.RESET_ALL).upper()

        if proceed == 'C':
            print('Copying Files . . .')

            try:
                shutil.copytree('./../../../MNLv2', directory + '\\MNL')

            except:
                print(Fore.RED + 'ERROR: Failed to copy files.' + Style.RESET_ALL)
                sys.exit()

            print(Fore.LIGHTGREEN_EX + 'Files Copied into ' + Style.RESET_ALL + directory)
            with open(CONFIG_FILE, 'w') as f:
                lines.pop(lines.index(DIR_LINE))
                lines.append(':INSTALL_DIR: = ' + directory)
                f.write(''.join(lines))
            sys.exit()

        elif proceed == 'W':
            print('Wiping Directory . . .')

            try:
                os.rmdir(directory)

            except:
                print(Fore.RED + 'ERROR: Failed wipe directory. Directory status: Not Removed' + Style.RESET_ALL)
                sys.exit()
            try:
                os.mkdir(directory)

            except:
                print(Fore.RED + 'ERROR: Failed wipe directory. Directory status: Removed' + Style.RESET_ALL)
                sys.exit()

            print(Fore.LIGHTGREEN_EX + 'Directory Wiped.' + Style.RESET_ALL)
            print('Copying Files . . .')

            try:
                shutil.copytree('./../../../MNLv2', directory + '\\MNL')

            except:
                print(Fore.RED + 'ERROR: Failed to copy files.' + Style.RESET_ALL)
                sys.exit()

            print(Fore.LIGHTGREEN_EX + 'Files Copied into ' + Style.RESET_ALL + directory)
            with open(CONFIG_FILE, 'w') as f:
                lines.pop(lines.index(DIR_LINE))
                lines.append(':INSTALL_DIR: = ' + directory)
                f.write(''.join(lines))
            sys.exit()

        else:
            print('Unknown Option.')
            sys.exit()
    
    else:
        proceed = input('Directory ' + directory + ' does not exists. Create folder and continue? (Y/N) ').upper()

        if proceed == 'N':
            sys.exit()

        elif proceed == 'Y':
            print('Creating Directory . . .')

            try:
                os.mkdir(directory)

            except:
                print(Fore.RED + 'ERROR: Failed to create directory.' + Style.RESET_ALL)
                sys.exit()

            print(Fore.LIGHTGREEN_EX + 'Directory Created.' + Style.RESET_ALL)
            print('Copying Files . . .')

            try:
                shutil.copytree('./../../../MNLv2', directory + '\\MNL')

            except:    
                print(Fore.RED + 'ERROR: Failed to copy files.' + Style.RESET_ALL)
                sys.exit()

            print(Fore.LIGHTGREEN_EX + 'Files Copied into ' + Style.RESET_ALL + directory)
            with open(CONFIG_FILE, 'w') as f:
                lines.pop(lines.index(DIR_LINE))
                lines.append(':INSTALL_DIR: = ' + directory)
                f.write(''.join(lines))
            sys.exit()

        else:
            print('Unknown Option.')    
            sys.exit()

# python setup.py -r -f -p C:\\Users\\rwc\\OneDrive\\Programming\\MNL\\COPY\\
# python setup.py --release --path C:\\Users\\rwc\\OneDrive\\Programming\\MNL\\COPY\\
