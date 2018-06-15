# REST API FLASK AND MYSQL

We'll be using Python, Flask and MySQL to create a real estate management web application. We are going to create a set of microservices. These microservices must allow a user to insert a property with the following characteristics: name, description, type of property, city, rooms, room characteristics, owner) and to consult other properties available on the platform

## Getting Started

### Prerequisites 

Setting up Flask is the first step and it is pretty simple and quick. With pip package manager, all we need to do is: 

```
pip install flask
pip install flask_mysqldb
```

### Create a user
Import Flask,render_template, request, jsonify, abort, make_response to use Flask framework
Import MySQL, MySQLdb to establish the connection with your sql localhost
```
from flask import Flask,render_template, request, jsonify, abort, make_response
from flask_mysqldb import MySQL, MySQLdb
```
Make the connection with mysql local server
```
#Make connection with mysql localhost
mysql=MySQLdb.connect("localhost", "root", "root", "flaskapp")
```
Create an empty database to store new users that we will be creating by compiling the next command in mysql prompt :
```
CREATE TABLE flaskapp.users (
`user_id` BIGINT AUTO_INCREMENT,
`nom` VARCHAR(50) ,
`prenom` VARCHAR(50) ,
`birthday` VARCHAR(50) ,
PRIMARY KEY (`user_id`));
```
Create the first user by running the next lines :
```
app=Flask(__name__)
#endpoint to create new user
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        #Fetch form data
        userDetails=request.form
        nom = userDetails['nom']
        prenom = userDetails['prenom']
        birthday = userDetails['birthday']
        cur=mysql.cursor()
        cur.execute("INSERT INTO users(nom,prenom,birthday) VALUES(%s,%s,%s)",(nom,prenom,birthday))
        mysql.commit()
        cur.close()
        return 'sucess'
    return render_template ('sign_up.html')
```
Check if users table is not empty anymore by typing the next command in mysql prompt :

```
SELECT * FROM USERS ;
```

End with an example of getting some data out of the system or using it for a little demo

## Modify user's information

The user has to declare it's user id and the personal information that he wants to modify

```
#Endpoint to modify user's information knowing it's user_id
@app.route('/usermodification',methods=['GET','POST'])
def usermodif():
    if request.method=='POST':
        #Fetch form data
        userDetails=request.form
        nom = userDetails['nom']
        prenom = userDetails['prenom']
        birthday = userDetails['birthday']
        userid = userDetails['userid']
        cur=mysql.cursor()
        cur.execute("UPDATE users SET nom=%s, prenom=%s, birthday=%s WHERE user_id=%s", (nom,prenom,birthday,userid))
        mysql.commit()
        cur.close()
        return 'sucess'
    return render_template ('usermodification.html')
```
Give an example
```
```

## And coding style tests
