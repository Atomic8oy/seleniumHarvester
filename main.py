from config import WEBSITE, EXCEL
from utilities import log

if WEBSITE == "digikala":
    import digikala
elif WEBSITE == "divar":
    import divar
elif WEBSITE == "tsetmc":
    import tsetmc
else:
    log("Website variable in config file is not valid.\nPlease read the readme.md")

if EXCEL:
    from config import OUT
    log(f"Saving as excel in [out/{OUT}.json]")
    import pandas

    pandas.read_json(f"out/{OUT}.json").to_excel(f"out/{OUT}.xlsx")
    log("[DONE]")