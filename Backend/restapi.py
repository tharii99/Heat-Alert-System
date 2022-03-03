# flask comes with "render_template" - this renders html files

from tkinter.tix import Select
from flask import (Flask, render_template)
from flask_mysqldb import MySQL

#create the application instance
app = Flask(__name__,template_folder="templates")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'solarpanel'



mysql = MySQL(app)


    
 


#create a url rout in our application for "/"

@app.route('/') #this is needed for the server to work
def home():
    """
    This function resonds only to ULR localhost:5000/
    :return   the rendered temlate 'home.html'
    """

    #Creating a connection cursor
    cursor = mysql.connection.cursor()

    #Executing SQL Statements
    #cursor.execute("SELECT * FROM generationdetails")

    cursor.execute("SELECT * FROM generationdetails WHERE  (Date BETWEEN '2022-02-02 14:20:26' AND '2022-02-04 14:22:04')")



    fetchdata = cursor.fetchall()
 
    #Saving the Actions performed on the DB
    #--mysql.connection.commit()
 
    #Closing the cursor
    cursor.close()

    return render_template('home.html',data = fetchdata) # this return statement can display html tags as well

    #if we're running in stand alone mode, run the application


 
app.run(host='localhost', port=10061)


if __name__ == "__main__":
    app.run(debug=True) #what ever the change we make, this updates the change and we can simply check the work just by refreshing the page




