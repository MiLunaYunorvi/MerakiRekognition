# MerakiRekognition
Antes de implementar el código, es necesario crear la base de datos de rostros conocidos y para ellos usaremos el código del archivo collections.py, pero primero obtendremos 2 credenciales de AWS para usar el servicios de colecciones de AWS Rekognition.
1. Primero nos aseguraremos de instalar la librería boto3 en nuestro ambiente local, esto con el comando **pip install boto3**.
2. Ahora iremos a la consola de AWS, en la barra de navegación desplegamos el usuario y nos dirijimos a 'Credenciales de seguridad'.
   ![image](https://github.com/MiLunaYunorvi/MerakiRekognition/assets/89271104/36b44780-a02b-4709-89f7-5300fcd1142a)
3. Ya en la ventana nos dirijimos a Claves de acceso y generamos un juego de estas.
   ![image](https://github.com/MiLunaYunorvi/MerakiRekognition/assets/89271104/af904d26-5be1-42da-b74a-2b0e4f7f1e1d)
4. Una vez generadas las copiamos en algùn bloc de notas o directamente en el encabezado del código del archivo collections.py, como se muestra.
   ![image](https://github.com/MiLunaYunorvi/MerakiRekognition/assets/89271104/dd5278b0-5c25-4f00-8151-546af259061b)
   ```
      import boto3 
      ACCESS_KEY = 'AKIAX4D*****5T6XLT'
      SECRET_KEY = 'CKSLeY7v+xH***************Q4o'
   ```
5. A continuación un video que muestra como usar el código, creamos la colección y luego se muestra como agregar rostros.
   [![Alt text](https://img.youtube.com/vi/hYdUmoWpnfE/0.jpg)](https://www.youtube.com/watch?v=hYdUmoWpnfE)

Una vez creada la colecciónn pasamos a desplegar la aplicación en un lambda de AWS, para esto usaremos el layer.zip que contiene las librerias necesarias y será nuestro layer en AWS.
1. Crear Lambda en AWS: https://youtu.be/vMQ2YbHjNI0
2. Video para crear el layer en AWS: https://youtu.be/v-pyZzjcKGk
3. Creación de un disparador, AWS API Gateway que se usará con el boton MT30 o Motion Alert de Meraki: https://youtu.be/FgzcocOKlhA
4. En el archivo meraki.py que también subiremos a AWS Lambda, se deben colocar los parámetros de Meraki, el bot y sala de Webex justo después de importar las librerías.
   ```
      from time import sleep
      import requests
      import urllib.request
      from PIL import Image
      from io import BytesIO
      import json
      
      ############### PARAMETROS PARA LLENAR ##############################
      api_key = ''
      mv_serial = ''
      token_bot = ''
      room_id = ''
      collect_name = 'DemoCollecion'  #cambiar el nombre si se uso uno diferente al momento de crear la colección
      ######################################################################
   ```
