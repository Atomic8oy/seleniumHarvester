from config import WEBSITE

if WEBSITE == "digikala":
    import digikala
elif WEBSITE == "divar":
    import divar
else:
    pass