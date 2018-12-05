import pymysql.cursors
def mysql_search_label(key):
	# Connect to the database
	connection = pymysql.connect(host='127.0.0.1',
	                             user='root',
	                             password='sjq_mysql',
	                             db='sql_mini3',
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			# Read a single record
			sql = "SELECT `twitter_id`, `time` FROM `sql_mini3` WHERE `label`=%s"
			cursor.execute(sql, (key,))
			result = cursor.fetchall()
	finally:
			connection.close()
	return result
'''for test
print(mysql_search_label('city'))
'''
