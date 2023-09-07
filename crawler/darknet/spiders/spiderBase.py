# encoding: utf-8
'''
EN: Module in charge of the generic and base implementation of any spider that we want to apply to a darkent.
SP: Módulo encargado de la implementación genérica y base de cualquier spider que queramos aplicar a una darkent.

For general information about scrapy.Spider, see: https://doc.scrapy.org/en/latest/topics/spiders.html
Para obtener información general sobre scrapy.Spider, consulte: https://doc.scrapy.org/en/latest/topics/spiders.html
'''

import random 		# https://docs.python.org/2/library/random.html
import re			# https://docs.python.org/2.7/library/re.html
import os			# https://docs.python.org/2/library/os.html
import sys
import logging
from logging.handlers import RotatingFileHandler
#import shutil		# https://docs.python.org/2/library/shutil.html
import urllib.parse		# https://docs.python.org/2/library/urlparse.html
import copy			# https://docs.python.org/2/library/copy.html
import time			# https://docs.python.org/2/library/time.html
#import operator		# https://docs.python.org/2/library/operator.html
import json			# https://docs.python.org/2/library/json.html
import nltk			# https://www.nltk.org
#from w3lib.html import remove_tags
#from py_translator import Translator
from googletrans import Translator
from bs4 import BeautifulSoup
import scrapy		# https://doc.scrapy.org/en/latest
from scrapy.linkextractors import LinkExtractor
from scrapy.spidermiddlewares.httperror import HttpError
from scrapy.exceptions import IgnoreRequest
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

import darknet.darknetsettings as darknetsettings
from darknet.items import Darknet_spider_state

nltk.download('punkt')
nltk.download('stopwords')

logger = logging.getLogger(__name__)
format = logging.Formatter('%(asctime)s %(levelname)s - %(threadName)s - mod: %(module)s, method: %(funcName)s, msg: %(message)s')

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(format)
ch.setLevel(logging.INFO)
logger.addHandler(ch)

fh = RotatingFileHandler(darknetsettings.PATH_LOG + "spiders.log", maxBytes=0, backupCount=0) # NO rotation, neither by size, nor by number of files
fh.setFormatter(format)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class spiderBase(scrapy.Spider):
	'''
	EN: Spider that is responsible for extracting the links contained in an darknet site.
	SP: Spider que se encarga de extraer los links contenidos en un darknet site.

	For general information about scrapy.Spider, see: https://doc.scrapy.org/en/latest/topics/spiders.html
	Para obtener información general sobre scrapy.Spider, consulte: https://doc.scrapy.org/en/latest/topics/spiders.html
	'''

	end_time = 0
	start_time = 0
	start_urls = []
	MAX_VISITED_LINKS = 1000
	overflow_visited_links = 0
	visited_links = {}
	non_visited_links_filename = "none"
	parse_darksite = None
	error = True
	state_item = Darknet_spider_state()
	state_item["darksite"] = "none"
	state_item["visited_links"] = {}
	state_item["language"] = {}
	state_item["extracted_darksites"] = []
	state_item["total_darksite_pages"] = 0
	state_item["title"] = "none"
	state_item["size_main_page"] = {}
	state_item["main_page_tokenized_words"] = []
	cond = False
	LANGUAGES_NLTK = [] # Lista de idiomas disponibles en la nltk

	LANGUAGES_GOOGLE = {} # Lista de idiomas disponibles en API Google
	main_page = True

	extractor_darknet = None

	def __init__(self, url=None, *args, **kwargs):
		'''
		EN: It initializes the seed URL list with the URL that has been passed as a parameter
		SP: Inicializa la lista de URLs semilla con la URL pasada como parámetro.

		:param url: url of the site to crawl / url del site a crawlear
		'''
		super(spiderBase, self).__init__(*args, **kwargs)

	def start_requests(self):
		'''
		EN: It returns an iterable of Requests which the Spider will begin to crawl.
		SP: Devuelve un iterable de Requests que el Spider comenzará a crawlear.
		'''
		#logger.debug("Dentro de start_requests()")
		for u in self.start_urls:
			yield scrapy.Request(u, callback=self.parse, errback=self.err, dont_filter=True)

	def detect_language_nltk(self, sample):
		'''
		EN: It uses NLTK platform to detect the language of a given sample.
		SP: Utiliza la plataforma NLTK para detectar el idioma de una muestra dada.

		:param sample: sample of text from which the language is detected / muestra de texto a partir de la cual detectar el idioma
		:return: the detected language / el idioma detectado
		'''
		#logger.debug("Dentro de detect_language_nltk()")

		# Dividimos el texto de entrada en tokens o palabras únicas
		tokens = nltk.tokenize.word_tokenize(sample)
		tokens = [t.strip().lower() for t in tokens] # Convierte todos los textos a minúsculas para su posterior comparación
		# Creamos un dict donde almacenaremos la cuenta de las stopwords para cada idioma
		lang_count = {}
		# Por cada idioma
		try:
			for lang in self.LANGUAGES_NLTK:
				# Obtenemos las stopwords del idioma del módulo nltk
				stop_words = str(nltk.corpus.stopwords.words(lang))
				lang_count[lang] = 0 # Inicializa a 0 el contador para cada idioma
				# Recorremos las palabras del texto a analizar
				for word in tokens:
					if word in stop_words: # Si la palabra se encuentra entre las stopwords, incrementa el contador
						lang_count[lang] += 1
			#print lang_count
			# Obtenemos el idioma con el número mayor de coincidencias
			language_nltk = max(lang_count, key=lang_count.get)
			if lang_count[language_nltk] == 0:
				language_nltk = 'undefined'
		except UnicodeDecodeError as e:
			logger.error('ERROR: %s', str(e))
			language_nltk = 'error'
		finally:
			return language_nltk

	def detect_language_google(self, sample):
		'''
		EN: It uses Google Translate to detect the language of a given sample.
		SP: Utiliza el Traductor de Google para detectar el idioma de una muestra dada.

		:param sample: sample of text from which the language is detected / muestra de texto a partir de la cual detectar el idioma
		:return: the detected language / el idioma detectado
		'''
		#logger.debug("Dentro de detect_language_google()")
		language_google = ""
		try:
			translator = Translator()
			det = translator.detect(sample)
			language_google = self.LANGUAGES_GOOGLE[det.lang]
		except ValueError as e:
			logger.error('ERROR: %s', str(e))
			language_google = "undefined--" + det.lang
		finally:
			return language_google

	def add_visited_links(self, link):
		'''
		EN: It controls the process of adding a new link to the visited_links dictionary.
		SP: Controla el proceso de adición de un nuevo link al diccionario visited_links.

		:param link: link to process / link a procesar
		'''
		logger.debug("Dentro de add_visited_links(): %s", str(link))
		if link in self.visited_links:
			count = self.visited_links.get(link) + 1
			self.visited_links.update({link:count})
		else:
			if len(self.visited_links) >= self.MAX_VISITED_LINKS:
				self.overflow_visited_links = self.overflow_visited_links + 1
				logger.info("Overflow_visited_links = %s", str(self.overflow_visited_links))
				min_val = min(self.visited_links.values())
				urls_min_value = []
				for url, value in self.visited_links.items():
					if value == min_val:
						urls_min_value.append(url)
				key = random.sample(urls_min_value, 1)[0]
				del self.visited_links[key]
			self.visited_links[link] = 1

	def split_words_in_groups(self, words):
		'''
		EN: It separates the words contained on the main page into an odd number of groups of maximum 200 words each.
		SP: Separa las palabras contenidas en la página principal en un número impar de grupos de máximo 200 palabras cada uno.

		:param words: full set of words / conjunto de palabras completo
		:return: list that contains the groups of words / lista que contiene los grupos de palabras
		'''
		#logger.debug("Dentro de split_words_in_groups()")
		words_delimiter = []
		if len(words) >= 200:
			self.cond = True
		while self.cond:
			words_delimiter.append(words[0:200])
			for _ in range(0, 200):
				words.pop(0)
			if len(words) < 200:
				self.cond = False
		if len(words_delimiter)%2 == 0:
			words_delimiter.append(words[0:len(words)])
		return words_delimiter


	def get_encoding(self, soup):
		'''
		EN: Get encoding of a page from BeautifulSoup
		SP: Obtiene la codificacion de una pagina de BeautifulSoup

		:param response: encoding returned by an darksite main page / codificacion devuelta por la página principal de un darksite
		'''
		if soup and soup.meta:
			encod = soup.meta.get('charset')
			if encod is None:
				encod = soup.meta.get('content-type')
				if encod is None:
					content = soup.meta.get('content')
					if content is None:
						return 'utf-8'

					match = re.search('charset=(.*)', content)
					if match:
						encod = match.group(1)
					else:
						return 'utf-8'
		else:
			return 'utf-8'
		return encod



	def main_page_analysis(self, response):
		'''
		EN: It analyzes and extracts information from the main page of an darksite.
		SP: Analiza y extrae información de la página principal de un darksite.

		:param response: response returned by an darksite main page / respuesta devuelta por la página principal de un darksite
		'''
		#logger.debug("Dentro de main_page_analysis()")
		main_page_code = response.body
		soup = BeautifulSoup(main_page_code, "html5lib")
		charset = self.get_encoding(soup)
		logger.debug("Dentro de main_page_analysis() - charset = %s", str(charset))
		soup = BeautifulSoup(main_page_code, "html5lib", from_encoding=charset)
		text = soup.get_text(strip=True)
		tokens = [t for t in text.split()]
		#main_page_without_tags = remove_tags(main_page_code, encoding=charset)
		main_page_without_tags = BeautifulSoup(main_page_code, "lxml", from_encoding=charset).text
		#logger.debug("Dentro de main_page_analysis() - pasa el remove_tags")
		title = response.xpath('normalize-space(//title/text())').extract()
		sample = re.sub('[^?!A-Za-z0-9]+', ' ', main_page_without_tags)
		words = sample.replace("\n", "")
		words = words.split(" ")
		num_words = len(words)
		logger.info("Total words in main page: %s", str(num_words))
		num_letters = 0
		for word in words:
			num_letters = num_letters + len(word)
		logger.info("Total letters in main page: %s", str(num_letters))

		sample = self.split_words_in_groups(words)
		language_google = []
		language_nltk = []
		for i in range(0, len(sample)):
			# Lenguaje con API de GOOGLE:
			try:
				language_google.append(self.detect_language_google(" ".join(sample[i])))
			except ValueError as e:
				logger.error('ERROR: %s', str(e))
				lang_google_error = "undefined--"
				#print "\nLanguage error: " + str(lang_google_error)
				language_google.append(lang_google_error)
			#print str(language_google)
			# Lenguaje con nltk:
			language_nltk.append(self.detect_language_nltk(" ".join(sample[i])))
			#print str(language_nltk)
		freq_lang_google = []
		for w in language_google:
			freq_lang_google.append(language_google.count(w))
		language_google_decision = language_google[freq_lang_google.index(max(freq_lang_google))]
		freq_lang_nltk = []
		for w in language_nltk:
			freq_lang_nltk.append(language_nltk.count(w))
		language_nltk_decision = language_nltk[freq_lang_nltk.index(max(freq_lang_nltk))]
		logger.debug("Language_google: %s", str(language_google))
		logger.debug("Language_nltk: %s", str(language_nltk))
		#logger.debug(("Pairs (Google):\n" + str(zip(language_google, freq_lang_google)))
		#logger.debug(("Pairs (NLTK):\n" + str(zip(language_nltk, freq_lang_nltk)))

		images = response.xpath('//img').extract()
		scripts = response.xpath('//script').extract()
		num_images = len(images)
		num_scripts = len(scripts)
		#logger.debug("Images (content): " + str(images))
		#logger.debug("Scripts (content): " + str(scripts))
		logger.debug("Images: %s", str(num_images))
		logger.debug("Scripts: %s", str(num_scripts))

		# Añadiendo al item:
		self.state_item["title"] = title
		self.state_item["main_page_tokenized_words"] = tokens
		self.state_item["size_main_page"]['WORDS'] = num_words
		self.state_item["size_main_page"]['LETTERS'] = num_letters
		self.state_item["size_main_page"]['IMAGES'] = num_images
		self.state_item["size_main_page"]['SCRIPTS'] = num_scripts
		self.state_item["language"]['GOOGLE'] = language_google_decision
		self.state_item["language"]['NLTK'] = language_nltk_decision

	def delete_link_from_non_visited(self, link):
		'''
		EN: It deletes the link passed as parameter from the file that contains the non visited links.
		SP: Elimina el link pasado como parámetro del fichero que contiene los links no visitados.

		:param link: link to delete / link a eliminar
		'''
		#logger.debug("Dentro de delete_link_from_non_visited()")
		link_parse = urllib.parse.urlparse(link)
		link_path = link_parse.path
		f = open(self.non_visited_links_filename, "r")
		lines = f.readlines()
		f.close()
		f = open(self.non_visited_links_filename, "w")
		for line in lines:
			if ((link_path not in line) and (not line.isspace())):
				#if (link_path not in line) and (line.isalnum()) and (not line.isspace()):
				line = line.replace("\n", "")
				line = line.replace(" ", "")
				f.write("\n")
				f.write(line)
		f.close()

	def check_link_in_non_visited(self, link):
		'''
		EN: It checks if the link passed as parameter is inside the file that contains the non visited links.
		SP: Comprueba si el link pasado como parámetro se encuentra dentro del archivo que contiene los links no visitados.

		:param link: link to check / link a comprobar
		:return: boolean that is True if the link is in the file; False otherwise /
			booleano que está a True si el link se encuentra en el fichero; a False en caso contrario
		'''
		#logger.debug("Dentro de check_link_in_non_visited()")
		link_parse = urllib.parse.urlparse(link)
		link_path = link_parse.path
		belongs = False
		with open(self.non_visited_links_filename) as f:
			line = f.readline()
			while line != "" and not belongs:
				if link_path in line:
					belongs = True
				else:
					line = f.readline()
		return belongs

	def add_link_to_non_visited(self, link):
		'''
		EN: It adds the link passed as parameter to the file that contains the non visited links.
		SP: Añade el link pasado como parámetro al fichero que contiene los links no visitados.

		:param link: link to add / link a añadir
		'''
		#logger.debug("Dentro de add_link_to_non_visited()")
		link_parse = urllib.parse.urlparse(link)
		link_path = link_parse.path
		f = open(self.non_visited_links_filename, "a+")
		f.write("\n")
		f.write(link_path)
		f.close()

	def parse(self, response):
		'''
		EN: It handles the downloaded response for each of the made requests.
		SP: Maneja la respuesta descargada para cada una de las solicitudes realizadas.

		It stores the extracted darksites from each response in the corresponding Item.
		In addition, it makes a yield to itself with a Request for each of the internal links of the site (with what the whole site is crawled).
		Almacena en el Item correspondiente los darksites extraídos de cada response.
		Además, hace un yield a sí mismo con una Request para cada uno de los enlaces internos del site (con lo que se crawlea el site entero).

		:param response: response returned by an darksite / respuesta devuelta por un darksite.
		'''

		try:
			self.error = False
			logger.debug("Received response from %s", str(response.url))
			if self.main_page:
				self.main_page_analysis(response)
				self.main_page = False
			self.add_visited_links(response.url)
			self.state_item["total_darksite_pages"] = len(self.visited_links)+self.overflow_visited_links
			if self.check_link_in_non_visited(response.url):
				self.delete_link_from_non_visited(response.url)
			self.state_item["visited_links"] = self.visited_links.copy()
			links = self.get_links(response)
			for link in links:
				parse_link = urllib.parse.urlparse(link.url)
				if ((parse_link.netloc not in self.state_item["extracted_darksites"]) and (parse_link.netloc != self.parse_darksite.netloc)):
					self.state_item["extracted_darksites"].append(parse_link.netloc)
				if ((not self.check_link_in_non_visited(link.url)) and (link.url not in self.visited_links) and (self.parse_darksite.netloc == parse_link.netloc)):
					self.add_link_to_non_visited(link.url)
					yield scrapy.Request(link.url, callback=self.parse, errback=self.err, dont_filter=True)
					if self.check_link_in_non_visited(response.url):
						self.delete_link_from_non_visited(response.url)
				yield self.state_item
			yield self.state_item
		except Exception as e:
			logger.error("ERROR scraping site %s: %s", response.url, e)
			raise


	def get_links(self, response):
		'''
		EN: It extracts the links from a certain darksite.
		SP: Extrae los links de un determinado darksite.

		:param response: response returned by an darksite / respuesta devuelta por un darksite
		:return: list that contains the extracted links / lista que contiene los links extraídos
		'''
		logger.info("Extracting links from %s...", str(response))
		links = self.extractor_darknet.extract_links(response)
		#logger.info("Links extracted: %s", links)
		return links

	def closed(self, reason):
		'''
		EN: It is called when the spider has ended the crawling process.
		SP: Se llama cuando el spider ha terminado todo el proceso de crawling.

		It generates an empty file with ".fail" extension in case there has been any error and the site
		hasn't been crawled correctly; otherwise, it generates an empty file with ".ok" extension.
		Genera un archivo vacío con extensión ".fail" en caso de que haya habido algún error y el site no
		se haya podido crawlear correctamente; en caso contrario, genera un archivo vacío con extensión ".ok".

		:param reason: a string which describes the reason why the spider was closed / string que describre por qué ha finalizado el spider
		'''
		logger.debug("Dentro de closed()")
		logger.info("SPIDER FINALIZADO")
		logger.info("ERROR = %s", str(self.error))
		site = self.parse_darksite.netloc

		logger.debug("SPIDER SITE = %s", site)
		ok = darknetsettings.PATH_FINISHED_SPIDERS + site + ".ok"
		fail = darknetsettings.PATH_FINISHED_SPIDERS + site + ".fail"
		target = darknetsettings.PATH_ONGOING_SPIDERS + site + ".json"
		self.end_time = time.time()
		if self.error:
			f = open(fail, "w")
			f.close()
			logger.debug(".fail has been created at %s", fail)
		else:
			f = open(ok, "w")
			f.close()
			logger.debug(".ok has been created at %s", ok)
			logger.debug("Total time taken in crawling %s: %s seconds.", self.parse_darksite.netloc, str(self.end_time - self.start_time))
			if os.path.exists(self.non_visited_links_filename):
				os.remove(self.non_visited_links_filename)
			with open(target, 'r+') as f:
				data = json.load(f)
				del data["visited_links"]
				f.seek(0)
				json.dump(data, f)
				f.truncate()

	def err(self, failure):
		'''
		EN: It reports about possible errors that may occur when a request fails.
		SP: Reporta los posibles errores que pueden producirse cuando una petición falla.

		This function is called when an error occurs (if any exception was raised while processing
		the request). The showed errors are: HttpError, DNSLookupError y TimeoutError.
		Esta función es llamada cuando ocurre un error (si se lanza cualquier extensión mientras se	procesa
		una respuesta). Son mostrados los errores: HttpError, DNSLookupError y TimeoutError.

		:param failure: type of error which has ocurred /
			tipo de error que ha ocurrido
			(https://twistedmatrix.com/documents/current/api/twisted.python.failure.Failure.html)
		'''
		logger.debug("Dentro de err()")
		logger.error("Detailed traceback %s ", failure.printDetailedTraceback())
		logger.error("Error message %s ", failure.getErrorMessage())


		if failure.check(HttpError):
			response = failure.value.response
			logger.error("HttpError occurred on %s", response.url)
		elif failure.check(DNSLookupError):
			request = failure.request
			logger.error("DNSLookupError occurred on %s", request.url)
		elif failure.check(TimeoutError, TCPTimedOutError):
			request = failure.request
			logger.error("TimeoutError occurred on %s", request.url)
		else:
			logger.error("Error failure %s ", failure)
			request = failure.request
			if failure.check(IgnoreRequest):
				logger.info("Request %s ignored by extension. This is how it is defined in middlewares", request.url)
			if self.check_link_in_non_visited(request.url):
				self.delete_link_from_non_visited(request.url)
			if request.url not in self.visited_links:
				self.add_visited_links(request.url)
			self.state_item["visited_links"] = copy.deepcopy(self.visited_links)
			yield self.state_item
