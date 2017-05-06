from flask import Flask, request
import sqlite3 as sql

app = Flask(__name__)

#Save type of seizure and time of seizure into database (yy/mm/dd/hh/mm/ss)
@app.route('/<type>/<year>/<month>/<day>/<hour>/<min>/<sec>', methods=['POST'])
def main(type, year, month, day, hour, min, sec):
	if request.method == 'POST':
		sqlFile = 'data.db'
		connection = sql.connect(sqlFile)
		c = connection.cursor()
		values = ""
		values = type+','+ year+','+month+','+day+','+hour+','+min+','+sec
		c.execute('INSERT into data values(' + values + ');')
		connection.close()
		return 'INSERT into data values(' + values + ');'


if __name__ == '__main__':
	app.run(debug=True)
