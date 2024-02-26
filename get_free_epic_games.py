import requests
from bs4 import BeautifulSoup

def get_element_text(url, xpath):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.select_one(xpath)
        if element:
            return element.text.strip()
        else:
            return "Nem található az elem az adott XPath szerint."
    else:
        print(response.status_code)
        return "Hiba történt a weboldal letöltése közben."

# Az URL és az XPath definiálása
url = "https://store.epicgames.com/en-US/"
xpath = "html > body > div:nth-of-type(1) > div > div:nth-of-type(4) > main > div:nth-of-type(2) > div > div > div > div:nth-of-type(2) > div:nth-of-type(2) > span:nth-of-type(4) > div > div > section > div > div:nth-of-type(1) > div > div > div > a"

# Az elem szövegének lekérdezése és kiírása
print(get_element_text(url, xpath))