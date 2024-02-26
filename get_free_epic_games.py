import requests
from bs4 import BeautifulSoup

def get_element_text(url, xpath):
    # Weboldal letöltése
    response = requests.get(url)
    if response.status_code == 200:
        # BeautifulSoup objektum létrehozása a HTML tartalomból
        soup = BeautifulSoup(response.text, 'html.parser')
        # XPath alapján keresés
        element = soup.select_one(xpath)
        if element:
            return element.text.strip()
        else:
            return "Nem található az elem az adott XPath szerint."
    else:
        print(response.status_code)
        print(response.resp)
        return "Hiba történt a weboldal letöltése közben."

# Az URL és az XPath definiálása
url = "https://store.epicgames.com/en-US/"
xpath = "html > body > div:nth-of-type(1) > div > div:nth-of-type(4) > main > div:nth-of-type(2) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > span:nth-of-type(4) > div > div > section > div > div:nth-of-type(1) > div > div > div > a"

# Az elem szövegének lekérdezése és kiírása
print(get_element_text(url, xpath))

