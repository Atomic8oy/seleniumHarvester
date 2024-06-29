from datetime import datetime

digits = {
    "۰": "0",
    "۱": "1",
    "۲": "2",
    "۳": "3",
    "۴": "4",
    "۵": "5",
    "۶": "6",
    "۷": "7",
    "۸": "8",
    "۹": "9"
}
def convertDigits(inp:str)->str:
    out = ""
    for n in inp:
        out += digits[n]
    return out

onLine = False

def log(string: str, newLine: bool = False)-> None:
    global onLine

    if newLine and onLine:
        print(string)
        onLine = False
    elif not (newLine and onLine):
        print(f"[{datetime.now().strftime('%Y/%m/%d %I:%M:%S%p')}] {string}", end=" ")
        onLine = True
    elif newLine and not onLine:
        print(f"[{datetime.now().strftime('%Y/%m/%d %I:%M:%S%p')}] {string}")
        onLine = False
    elif not newLine and onLine:
        print(string, end=" ")
        onLine = True
    else:
        raise("An unexpected error happened in logging.")
    