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
driver.get('http://localhost:3001/')

# Espera hasta que los elementos de la página estén cargados
time.sleep(2)

# Encuentra los campos de usuario y contraseña
campo_usuario = driver.find_element(By.ID, 'usuario')
campo_contrasena = driver.find_element(By.ID, 'contrasena')

# Ingresa el usuario y la contraseña
campo_usuario.send_keys('jmaldonado')
campo_contrasena.send_keys('jhon123')

# Encuentra el botón de ingresar y haz clic en él
boton_ingresar = driver.find_element(By.ID, 'btnIngresar')
boton_ingresar.click()

# Espera unos segundos para observar el resultado
time.sleep(20)

# Capturar la URL actual
current_url = driver.current_url
driver.get(current_url)

# Captura el campo nombre en la nueva pantalla
campo_nombre = driver.find_element(By.ID,'nombre')
campo_nombre.send_keys('PRUEBA')

# Encuenta el botón field y haz clic en él
boton_selec_archivo = driver.find_element(By.ID, 'archivo')
# Sube un archivo
boton_selec_archivo.send_keys(r'C:\Users\jhonf\Downloads\evidencia_humedad.jpg')
time.sleep(10)

# Cierra el navegador
driver.quit()
