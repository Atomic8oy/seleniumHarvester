from config import WEBSITE, EXCEL
from utilities import Logger

logging = Logger()

match WEBSITE:
    case  "history":
        import tsetmc
    case "live":
        import tsetmcLive
    case _:
        raise(f"{WEBSITE} is not supported.\nCheck for typos or new updates.")

if EXCEL:
    from config import OUT
    logging.log(f"Saving as excel in [out/{OUT}.json]")
    import pandas

    pandas.read_json(f"out/{OUT}.json").to_excel(f"out/{OUT}.xlsx")
    logging.done()