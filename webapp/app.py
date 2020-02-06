from flask import Flask, render_template
import pymysql.cursors

app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='jp6884xv',
                             password='Baseball.6',
                             db='jp6884xv_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Get user input for a first name
        # name = input("Enter a name to search for in the database: ")

        # execute the SQL command
        cursor.execute("SELECT * from Students")
        data = cursor.fetchall()
            
finally:
    connection.close()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/database')
def database():
    return render_template('database.html', output=data)


@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='6884')
