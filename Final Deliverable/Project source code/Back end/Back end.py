from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re

app = Flask(__name__)

app.secret_key = 'a'

conn = ibm_db.connect("DATABASE= ;HOSTNAME=;PORT=;SECURITY=;SSLSServerCertificate=;UTD=;phD=",'','',)

@app.route('/') 

def home():
    return render_template('home.html')

    @app.route('/login',methods = ['GET','POST'])
    def login():
        global Userid

        msg=''

    if request.method == 'POST':
        username = request.form['username']
        Password = request.form['password'] 
        sql = "SELECT * FORM users WHERE username =? AND password=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,1,password)
        ibm_db.excute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print (account)
        if account:
            session['logged']=true
            session['id']= account ['USERNAME']
            userid = account['USERNAME']
            session['username'] = account['username']
            msg = 'logged in successfully !'

            return render_template('dashboard.html',msg = msg)

        else:
            msg = 'Incorrect username / password !'
        return render_template('login.html',msg=msg)

@app.route('/register', methods = ['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username == request.form['username']
        email = request.form['email']
        password = request.form['password']
        sql = "SELETE * FROM users WHERE username = ?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+',username):
            msg = 'Name must contain only characters and numbers!'
        else: 
            insert_sql = "INSERT INTO users VALUES (?,?,?,)"
            pre_stmt= ibm_db.prepare(conn,insert_sql)
            ibm_db.bind_param(prep_stmt,1 , username);
            ibm_db.bind_param(prep_stmt,2, email)
            ibm_db.bind_param(prep_stmt,3,password)
            ibm_db.execute(prep_stmt)
            msg = 'Name must contain only characters and numbers!'
    elif request.method == 'POST':
            msg = 'please fill out the form!'
    return tender_template('register.html',msg = msg)    

@app.rout('/dashboard')
def dash():
  
    return render_template('dashboard.html')

@app.route('/apply',methods=['GET','POST'])
def appy():
    msg=''
    if request.methods == 'POST' :
        username = request.form['username']
        email=request.form['email']
        qualifications= request.form['qualifications']
        skills = request.form['skills']
        job = request.form['s']
        sql = 'SELECT * FROM users WHERE username= ?'
        insert_sql = "INSERT INTO job VALUES (?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn,insert_sql)
        ibm_db.bind_param(prep_stmt,1,username)
        ibm_db.bind_param(prep_Stmt,2,email)
        ibm_db.bind_param(prep_stmt,3,qualification)
        ibm_db.bind_param(prep_stmt,4,skills)
        ibm_db.bind_param(prep_stmt,5,jobs)
        ibm_db.execute(prep_stmt)
        msg = 'you have successfully applied for job !'
        session['loggedin']=True
    elif request.method == 'POST':
        mag='please fill out the form !'
    return render_template('apply.html',msg = msg)

@app.route('/display')
def display():

    print(session["username"],session['id'])
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM jop WHERE userid = % s',(session['id']))
    account = cursor.fetchone()

    print("accountdisplay",account)

    return render_template('display.html',account = account)      

@app.route('/logout')
def logout():

    session.pop('loggedin',none)
    session.pop('id',none)
    session.pop('username',none)

    return render_template('home.html')

if__name__=='__main__';
app.run(host='0.0.0.0')





    


                
