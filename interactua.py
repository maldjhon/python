from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoAlertPresentException
import time

# Configura el servicio del navegador (asegúrate de tener el driver adecuado instalado)
options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
service = Service(r'D:\Documentos\Proyectos\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

# Abre la página web
driver.get('https://maldjhon.github.io/userinterface/')

# Espera hasta que los elementos de la página estén cargados
time.sleep(2)

# Encuentra los campos de usuario y contraseña
campo_usuario = driver.find_element(By.ID, 'usuario')
campo_contrasena = driver.find_element(By.ID, 'contrasena')

# Ingresa el usuario y la contraseña
campo_usuario.send_keys('jhon')
campo_contrasena.send_keys('jhon1')

# Encuentra el botón de ingresar y haz clic en él
boton_ingresar = driver.find_element(By.ID, 'btnIngresar')
boton_ingresar.click()

# Espera unos segundos para observar el resultado
time.sleep(120)

# Captura el mensaje de alerta si aparece
try:
    alerta = driver.switch_to.alert
    mensaje_alerta = alerta.text
    print(f"Mensaje de alerta: {mensaje_alerta}")
    alerta.accept()  # Acepta la alerta para cerrarla
except NoAlertPresentException:
    print("No hay alerta presente.")

# Espera unos segundos para observar el resultado
time.sleep(60)

# Cierra el navegador
driver.quit()
