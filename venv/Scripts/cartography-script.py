#!C:\Users\Renato\PycharmProjects\APS\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'cartography==0.10.0','console_scripts','cartography'
__requires__ = 'cartography==0.10.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('cartography==0.10.0', 'console_scripts', 'cartography')()
    )
