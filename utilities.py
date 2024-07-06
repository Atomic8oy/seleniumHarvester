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
        if n in digits:
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
    
def exists(item: dict, items: dict):
    for data in items.values():
        if data == item:
            return True
    return False

def convertToTitle(columnNumber: int) -> str:
        out = ""
        while columnNumber > 0:
            print(columnNumber)
            columnNumber -= 1
            out += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[columnNumber%26] 
            columnNumber = int(columnNumber/26)
        return out[::-1]