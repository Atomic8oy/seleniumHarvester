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
    
class Logger():
    def __init__(self):
        self.onLine = False
    
    def log(self, string:str, newLine:bool = False)-> None:
        if self.onLine and newLine:
            print(string)
            self.onLine = False
        elif self.onLine and (newLine == False):
            print(string, end=" ")
            self.onLine = True
        elif (self.onLine == False) and newLine:
            print(f"[{datetime.now().strftime('%Y/%m/%d %I:%M:%S%p')}] {string}")
            self.onLine = False
        elif (self.onLine == False) and (newLine == False):
            print(f"[{datetime.now().strftime('%Y/%m/%d %I:%M:%S%p')}] {string}", end=" ")
            self.onLine = True
        else:
            raise("an unexpected error happened while logging.")

    
def exists(item: dict, items: dict)-> bool:
    for data in items:
        if data == item:
            return True
    return False
