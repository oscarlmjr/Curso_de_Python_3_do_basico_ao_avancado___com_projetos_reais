# Selenium - Automatizando tarefas no navegador
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'
# print(ROOT_FOLDER)
# print(CHROME_DRIVER_EXEC)


chrome_options = webdriver.ChromeOptions()
chrome_service = Service(
	executable_path=str(CHROME_DRIVER_EXEC),
	)
chrome_browser = webdriver.Chrome(
		service=chrome_service,
		options=chrome_options,
	)

chrome_browser.get('https://www.google.com')
sleep(30)
