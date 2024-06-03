import requests
import sys
from bs4 import BeautifulSoup

def main():
	url = input("Ingrese el sitio web\n=> ")
	agent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	peticion = requests.get(url=url,headers=agent)
	soup = BeautifulSoup(peticion.text,'html.parser')

	lista_plugin = []
	lista_final = []

	for enlace in soup.find_all('link'):
		if 'wp-content/plugins' in enlace.get('href'):
			href = enlace.get('href')
			href = href.split('/')
			posicion = href.index('plugins')
			plugin = href[posicion+1]
			lista_plugin.append(plugin)

	for i in lista_plugin:
		if i in lista_final:
			pass
		else:
			lista_final.append(i)

	for i in lista_final:
		print("(+) Se encontro el plugin {}".format(i))



if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()