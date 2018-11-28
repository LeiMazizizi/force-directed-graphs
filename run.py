import configparser
from flask import Flask, render_template, request
import mysql.connector

# Read configuration from file.
config = configparser.ConfigParser()
config.read('config.ini')

# Set up application server.
app = Flask(__name__)

# Create a function for fetching data from the database.
def sql_query(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result


def sql_execute(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


@app.route('/', methods=['GET', 'POST'])
def template_response_with_data():
    print(request.form)
    if "random-graph" in request.form:
        book_id = int(request.form["random-graph"])
        #sql = "delete from book where id={book_id}".format(book_id=book_id)
        #sql_execute(sql)
    template_data = {}
    #sql = "select id, title from book order by title"
    books = sql_query(sql)
    template_data['books'] = books
    return render_template('index.html', template_data=template_data)

if __name__ == '__main__':
    app.run(**config['app'])
