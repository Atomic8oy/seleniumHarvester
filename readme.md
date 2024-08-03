# How to use
* Go to `config.json` and change it based on what you want to do (There are instructions below)
* Run `main.py` and get your output in `out/` folder

# config.json instructions

### target:
The target website:
digikala, divar, tsetmc, tsetmcLive

### keyword: 
(digikala) a keyword to search in digikala<br>
(divar) city's name<br>
(tsetmc) `https://www.tsetmc.com/History/{KEYWORD}`<br>
(tsetmcLive) `https://tsetmc.com/instInfo/{KEYWORD}`<br>

### out:
output file to save the data in `out/{OUT}.json`<br>
if it was empty it uses the keyword

### excel:
excel output, `true/false`

### scroll:
How many times the app scrolls down

### scrollAmount:
How much should app scroll down by pixels