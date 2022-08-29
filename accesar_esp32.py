import shutil
from PIL import Image
import requests
#import os, sys
import datetime
import time


def tomar_foto_noche():
	datetime_object = datetime.datetime.now()
	#print(datetime_object)
	d1 = str(datetime_object)
	output = d1.replace(":", " ")
	output = output.replace(" ", "_")
	output = output[0:19]+".jpg"

	foto = 'http://192.168.2.35/boto'
	boto = 'http://192.168.2.35/foto'
	filename = str(output)

	response = requests.get(boto, stream=True)
	response = requests.get(foto, stream=True)

	if response.status_code == 200:
		try:
			response.raw.decode_content = True
			with open(filename,'wb') as f:
				shutil.copyfileobj(response.raw, f)
				print('Image sucessfully Downloaded: ',filename)

			imagen = Image.open(filename)
			imagen_2=imagen.rotate(-90)
			imagen_2.save(filename)
			#imagen_2.show()
				
		except exception as e:
			print('Algo ocurrio: ' + str(e))

	else:
		print(response.status_code)
		print('Image Couldn\'t be retreived')

	datetime_object = datetime.datetime.now()
	#print(datetime_object)


while True:
	tomar_foto_noche()
	time.sleep(60)