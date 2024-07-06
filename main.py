from config import WEBSITE, EXCEL
from utilities import log

if WEBSITE == "digikala":
    import digikala
elif WEBSITE == "divar":
    import divar
else:
    log("Website variable in config file is not valid.\nPlease read the readme.md")

if EXCEL:
    from config import OUT
    import pandas

    pandas.read_json(f"out/{OUT}.json").to_excel(f"out/{OUT}.xlsx")
