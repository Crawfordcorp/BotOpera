from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Configurações do navegador Google Chrome
chrome_options = ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Abre o navegador maximizado

# Configuração do service do ChromeDriver
chrome_driver_path = "C:\\Users\\David\\Downloads\\chromedriver.exe"  # Caminho para o chromedriver

# URLs que serão abertas
urls = [
    "https://www.twitch.tv/alanzoka",
    "https://www.twitch.tv/naashshadow"
]

try:
    # Inicializa o service do ChromeDriver
    chrome_service = ChromeService(executable_path=chrome_driver_path)

    # Inicializa o driver do Chrome com as opções do Google Chrome
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Abre as URLs
    for url in urls:
        driver.get(url)

    # Mantém o navegador aberto por um tempo (opcional)
    input("Pressione Enter para fechar o navegador...")

except Exception as e:
    print(f"Ocorreu um erro ao iniciar o WebDriver: {str(e)}")

finally:
    # Fecha o navegador
    if 'driver' in locals():
        driver.quit()
