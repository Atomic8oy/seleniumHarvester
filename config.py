from json import loads

with open("config.json", 'r') as configFile:
    data = loads(configFile.read())

WEBSITE = data["website"]
KEYWORD = data["keyword"]
if data["out"] == "":
    OUT = KEYWORD
else:
    OUT = data["out"]

EXCEL = data['excel']

SCROLL = data['scroll']
SCROLL_AMOUNT = data['scrollAmount']