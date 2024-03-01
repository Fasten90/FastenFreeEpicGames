from selenium import webdriver

# ChromeDriver útvonalának beállítása
chrome_driver_path = "/usr/bin/chromedriver"  # Cseréld le a valós útvonalra

# Selenium inicializálása
options = webdriver.ChromeOptions()
options.binary_location = chrome_driver_path  # Ha külön Chrome telepítést használsz, cseréld le a valós útvonalra
#driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver = webdriver.Chrome(options=options)

