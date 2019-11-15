import webapp2
import MySQLdb
import passwords
import random
import cgi

class MainPage(webapp2.RequestHandler):
	def get(self):
		conn = MySQLdb.connect(unix_socket = passwords.SQL_HOST,
        	user = passwords.SQL_USER,
        	passwd = passwords.SQL_PASSWD,
        	db = "clinton")

		cursor = conn.cursor()
		cursor2 = conn.cursor()
        	cursor.execute(sql)
        	conn.commit()
        	results = cursor.fetchall()
		id = "%032x" % random.getrandbits(128)
		self.response.headers["Content-Type"] = "text/html"
		self.response.write("Hello World\n")

		cookie = self.request.cookies.get("cookie_name")
		if cookie == None:
			self.response.set_cookie("cookie_name", id, max_age)
			cursor2.execute("INSERT INTO sessions (id) VALUES (%s);", [id])
		

app = webapp2.WSGIApplication([
	("/", MainPage),
], debug=True)
