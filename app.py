from flask import Flask,render_template, request, jsonify, abort, make_response
from flask_mysqldb import MySQL, MySQLdb

app=Flask(__name__)

#Make connection with mysql localhost
mysql=MySQLdb.connect("localhost", "root", "root", "flaskapp")

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

#Endpoint to modify user's information --Knowing it's user_id
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

#Endpoint to create a property
@app.route('/insertproperty',methods=['GET','POST'])
def propertycreate():
    if request.method=='POST':
        #Fetch form data
        propertyDetails=request.form
        property_name = propertyDetails['propertyname']
        description = propertyDetails['description']
        type = propertyDetails['type']
        city = propertyDetails['city']
        beds_number = propertyDetails['bedsnumber']
        beds_description = propertyDetails['bedsdescription']
        user_id = propertyDetails['userid']
        cur=mysql.cursor()
        cur.execute("INSERT INTO property(user_id, property_name,description,type,city,beds_number,beds_description ) VALUES(%s,%s,%s,%s,%s,%s,%s) ",(user_id,property_name,description,type,city,beds_number,beds_description) )
        mysql.commit()
        cur.close()
        return 'sucess'
    return render_template ('propertycreation.html')

#Endpoint to modify a property
@app.route('/propertymodification',methods=['GET','POST'])
def propertymodif():
    if request.method=='POST':
        #Fetch form data
        propertymodification=request.form
        property_name = propertymodification['propertyname']
        description = propertymodification['description']
        type = propertymodification['type']
        city = propertymodification['city']
        beds_number = propertymodification['bedsnumber']
        beds_description = propertymodification['bedsdescription']
        user_id = propertymodification['userid']
        property_id = propertymodification['propertyid']
        cur=mysql.cursor()
        cur.execute("UPDATE property SET property_name=%s,description=%s,type=%s,city=%s,beds_number=%s,beds_description=%s WHERE (user_id=%s and property_id=%s)  ",(property_name,description,type,city,beds_number,beds_description,user_id,property_id) )
        mysql.commit()
        cur.close()
        return 'sucess'
    return render_template ('propertymodification.html')

#Endpoint to display user_id results
@app.route('/result', methods=['GET'])
def propertyresult():
    cur = mysql.cursor()
    cur.execute(''' SELECT * FROM property WHERE city="Tunis" ''')
    rv = cur.fetchall()
    return str(rv)

if __name__=='__main__':
    app.run(debug=True)
