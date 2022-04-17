import pymysql
from pymysql.cursors import DictCursor

class DBmanager:

	def __init__(self):
		with open('password.txt') as f:
			passw = f.read()
		self.con = pymysql.connect(host='localhost',
									user='root',
									password=passw,
									db='encoding',
									charset='utf8mb4',
									cursorclass=DictCursor)
		self.curs = self.con.cursor()

	def encoding_query(self, symbol: str) -> str:
		"""Returns an encoding of a passed symbol as a string
		Raises KeyError if there is no such symbol
		"""
		self.curs.execute(
	'SELECT encoding FROM utf8 WHERE symbol="{0}"'.format(symbol))

		result = self.curs.fetchone()
		print(result)


		if result == None:
			raise KeyError()

		return result['encoding']

	def symbol_query(self, encoding: str) -> str:
		"""Returns a symbol which a passed encoding represents
		Raises KeyError if there is no such symbbol
		"""
    	
		self.curs.execute('SELECT symbol FROM utf8 WHERE encoding="{0}"'.format(encoding))

		result = self.curs.fetchone()

		if result == None:
			raise KeyError()

		return result['symbol'] 