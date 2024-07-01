from config import WEBSITE
from utilities import log

if WEBSITE == "digikala":
    import digikala
elif WEBSITE == "divar":
    import divar
else:
    log("Website variable in config file is not valid.\nPlease read the readme.md")