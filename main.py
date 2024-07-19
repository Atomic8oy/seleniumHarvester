from config import WEBSITE, EXCEL
from utilities import Logger

logging = Logger()

if WEBSITE == "digikala":
    import digikala
elif WEBSITE == "divar":
    import divar
elif WEBSITE == "tsetmc":
    import tsetmc
else:
    raise(f"This app doesn't support {WEBSITE}.\nCheck for typos or new updates.")

if EXCEL:
    from config import OUT
    logging.log(f"Saving as excel in [out/{OUT}.json]")
    import pandas

    pandas.read_json(f"out/{OUT}.json").to_excel(f"out/{OUT}.xlsx")
    logging.log("[DONE]", True)