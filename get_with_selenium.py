from selenium import webdriver

# ChromeDriver útvonalának beállítása
chrome_driver_path = "chromedriver"  # Cseréld le a valós útvonalra

# Selenium inicializálása
driver = webdriver.Chrome(chrome_driver_path)

# Oldal betöltése
driver.get("https://store.epicgames.com/en-US/")

# Elem lekérdezése XPath segítségével
element_xpath = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/span[4]/div/div/section/div/div[1]/div/div/div/a")
print("Elem (XPath):", element_xpath.text)

# Elem lekérdezése CSS PATH segítségével
element_css = driver.find_element_by_css_selector("html body div#dieselReactWrapper.en-US-locale div.isBrowser.css-14n04jc div.css-1vplx76 main.css-1pmr3eb div.css-1ktypff div.css-1dacand div.css-lai20k div.css-1knv3fd div div span div.css-1p2cbqg div.css-1vu10h2 section.css-2u323 div.css-1myhtyb div.css-1ukp34s div.css-aere9z div div.css-2mlzob a.css-g3jcms")
print("Elem (CSS PATH):", element_css.text)

# Böngésző bezárása
driver.quit()
