from flask import Flask,render_template,request,flash,redirect,url_for,make_response,abort
import pymysql as sql
import locale
import random
import string
import codecs
locale.setlocale(locale.LC_MONETARY,'en_IN')

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

def getDatabaseConnection():
    try:
        return sql.connect(host='localhost',port=3306 , user='grras', password='grras@123', database='mybankapp')
    except Exception as e:
        print(e)
        abort(404, description="Database not connected!")


app = Flask(__name__)
@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html',msg=error),404

def create_app(config_filename):
    app = Flask(__name__)
    app.register_error_handler(404, not_found)
    return app

app.secret_key = 'mysecret_key'

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home/')
def home():
    if request.cookies.get('acc'):
        db = getDatabaseConnection()
        cur = db.cursor()
        email = request.cookies.get('email')
        user_data = cur.execute("select * from users where Email='{}'".format(email))
        if user_data:
            user_data = cur.fetchall()
            user_data = {
                'acc':user_data[0][0],
                'fname':user_data[0][1],
                'lname':user_data[0][2],
                'email':user_data[0][3],
                'bal':locale.currency(float(user_data[0][5]),grouping=True,symbol=False)
                }
            transaction_data = cur.execute("select transaction_id,transaction_date,transaction_with,transaction_type,transaction_amt from {} order by sr_no desc".format('mba'+request.cookies.get('acc')))
            transaction_data = cur.fetchall()
            return render_template('user_home.html',user_data=user_data,transaction_data=transaction_data)
        else:
            # panding delete cookies
            abort(404, description="User Data not found")
    else:
        return render_template('home.html')

@app.route('/home/signup/')
def signup():
    if request.cookies.get('acc'):
        return redirect(url_for('home'))
    else:
        return render_template('signup.html')

@app.route('/home/login/')
def login():
    if request.cookies.get('acc'):
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/home/about/')
def about():
    return render_template('about.html')

@app.route('/home/user/transaction/')
def transaction():
    if request.cookies.get('acc'):
        return render_template('transaction.html')
    else:
        abort(404, description="Resource not found")

@app.route('/home/user/transaction/deposit/',methods=["POST","GET"])
def deposit():
    if request.cookies.get('acc'):
        if request.method=="POST":
            credit_amt = int(request.form.get('credit_amt'))
            if credit_amt>=100 and credit_amt<=100000:
                psw = request.form.get('psw')
                db = getDatabaseConnection()
                cur = db.cursor()
                acc_no = request.cookies.get('acc')
                user_data = cur.execute("select Balance from users where Acc_no='{}' and Password='{}'".format(acc_no,psw))
                if user_data:
                    balance = cur.fetchall()
                    balance = balance[0][0] + credit_amt
                    cur.execute("update users set Balance='{}' where Acc_no='{}'".format(balance,acc_no))
                    cur.execute(f"insert into {'mba'+acc_no} (transaction_id,transaction_type,transaction_amt) values('{get_random_alphaNumeric_string(10)}','credit',{credit_amt})")
                    db.commit()
                    flash(f'Deposit successful and your balance is {balance}')
                    return redirect(url_for('transaction')) 
                else:
                    flash('Wrong Password')
                    return redirect(url_for('transaction')) 
            else:
                flash("Invalid Amount Try 100 - 100000")
                return redirect(url_for('transaction'))      
        else:
            abort(404, description="Form not Response")
    else:
        abort(404, description="Resource not found")

@app.route('/home/user/transaction/withdraw/',methods=["POST","GET"])
def withdraw():
    if request.cookies.get('acc'):
        if request.method=="POST":
            debit_amt = int(request.form.get('debit_amt'))
            if not(debit_amt>=100 and debit_amt<=100000):
                flash("Invalid Amount Try 100 - 100000")
                return redirect(url_for('transaction')) 
            else:
                psw = request.form.get('psw')
                db = getDatabaseConnection()
                cur = db.cursor()
                acc_no = request.cookies.get('acc')
                user_data = cur.execute("select Balance from users where Acc_no='{}' and Password='{}'".format(acc_no,psw))
                if user_data:
                    balance = cur.fetchall()
                    if debit_amt>balance[0][0]:
                        flash("Insufficient Balance")
                        return redirect(url_for('transaction')) 
                    else:
                        balance = balance[0][0] - debit_amt
                        cur.execute("update users set Balance='{}' where Acc_no='{}'".format(balance,acc_no))
                        cur.execute(f"insert into {'mba'+acc_no} (transaction_id,transaction_type,transaction_amt) values('{get_random_alphaNumeric_string(10)}','debit',{debit_amt})")
                        db.commit()
                        msg = f'Withdraw successful and your remain balance is {balance}.'
                        if balance<500:
                            msg = msg+' Warning : Your account balance is less then 500 please add some amount.'
                        flash(msg)
                        return redirect(url_for('transaction')) 
                else:
                    flash('Wrong Password')
                    return redirect(url_for('transaction'))  
        else:
            abort(404, description="Form not Response")
    else:
        abort(404, description="Resource not found")


@app.route('/home/user/transaction/transfer/',methods=["POST","GET"])
def transfer():
    if request.cookies.get('acc'):
        if request.method=="POST":
            candidate_acc_no = request.form.get('acc_no')
            send_amt = int(request.form.get('send_amt'))
            psw = request.form.get('psw')
            if not(send_amt>=1 and send_amt<=50000):
                flash("Invalid Amount Try 1 - 50000")
                return redirect(url_for('transaction')) 
            else:
                db = getDatabaseConnection()
                cur = db.cursor()
                acc_no = request.cookies.get('acc')
                user_data = cur.execute("select Balance from users where Acc_no='{}' and Password='{}'".format(acc_no,psw))
                if user_data:
                    user_data = cur.fetchall()
                    candidate_data = cur.execute("select Balance,Email from users where Acc_no='{}'".format(candidate_acc_no))
                    if not(candidate_data):
                        flash("Incorrect Account Number.")
                        return redirect(url_for('transaction'))
                    candidate_data = cur.fetchall()
                    balance = user_data[0][0] - send_amt
                    transaction_id = get_random_alphaNumeric_string(10)
                    cur.execute("update users set Balance='{}' where Acc_no='{}'".format(balance,acc_no))
                    cur.execute(f"insert into {'mba'+acc_no} (transaction_id,transaction_with,transaction_type,transaction_amt) values('{transaction_id}','{str(candidate_acc_no)+'/'+candidate_data[0][1]}','debit',{send_amt})")
                    flash(f"Transfer Successfully and your remain balance is {balance}")
                    balance = candidate_data[0][0] + send_amt
                    cur.execute("update users set Balance='{}' where Acc_no='{}'".format(balance,candidate_acc_no))
                    cur.execute(f"insert into {'mba'+candidate_acc_no} (transaction_id,transaction_with,transaction_type,transaction_amt) values('{transaction_id}','{str(acc_no)+'/'+request.cookies.get('email')}','credit',{send_amt})")
                    db.commit()
                    return redirect(url_for('transaction'))    
                else:
                    flash('Wrong Password')
                    return redirect(url_for('transaction'))
        else:
            abort(404, description="Form not Response")
    else:
        abort(404, description="Resource not found")



@app.route('/home/signup/submit/',methods=["POST","GET"])
def createUser():
    if request.method=="POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        psw = request.form.get('psw')

        db = getDatabaseConnection()
        cur = db.cursor()
        params = [email]
        email_exist = cur.execute('select Email from users where Email=%s',params[0])
        if email_exist:
            flash(f'{params[0]} is already register! try with new email id.')
            return render_template('signup.html')
        else:
            try:
                qry = "insert into users(FirstName,LastName,Email,Password) values('{}','{}','{}','{}')".format(fname,lname,email,psw)
                cur.execute(qry)
                db.commit()
            except Exception as e:
                print(e)
            else:
                qry = "select FirstName,LastName,Acc_no from users order by Acc_no desc limit 1"
                cur.execute(qry)
                user_data = cur.fetchall()
                qry = '''create table {} (sr_no int not null primary key auto_increment,transaction_id 
                varchar(20)not null unique,transaction_date timestamp(0) default current_timestamp,
                transaction_with varchar(40) default 'self',transaction_type varchar(10)not null,
                transaction_amt double(10,2)not null)'''.format("mba"+str(user_data[0][2]))
                cur.execute(qry)
                qry = 'alter table {} auto_increment = 1'.format("mba"+str(user_data[0][2]))
                cur.execute(qry)
                flash('Hello, Mr./Mrs. {} {} You are Successfully Register! Your Account No. is {}. Now you are ready for login.'.format(user_data[0][0], user_data[0][1], user_data[0][2]))
                return redirect(url_for('home'))
    else:
        return redirect(url_for('signup'))

@app.route('/home/login/submit/',methods=["POST","GET"])
def check_login():
    if request.method=="POST":
        uname = request.form.get('uname')
        psw = request.form.get('psw')
        try:
            db = getDatabaseConnection()
        except Exception as e:
            print(e)
            abort(404, description="Database not connected!")
        cur = db.cursor()
        params = [uname]
        if params[0].isnumeric():
            user_exist = cur.execute("select Acc_no,Email,FirstName from users where Acc_no = {} and Password = '{}'".format(params[0],psw))
        else:
            user_exist = cur.execute("select Acc_no,Email,FirstName from users where Email = '{}' and Password = '{}'".format(params[0],psw))
        if user_exist:
            user_data = cur.fetchall()
            if user_data:
                resp = make_response(redirect(url_for('home')))
                resp.set_cookie('acc',str(user_data[0][0]))
                resp.set_cookie('email',user_data[0][1])
                resp.set_cookie('username',user_data[0][2])
                return resp
        else:
            flash('Invalid Username and Password',category='error')
            return redirect(url_for('login'))
        
    else:
        flash("form request faild!")
        return redirect(url_for('login'))

@app.route('/home/user/logout/')
def logout():
    flash('Logged Out!')
    resp=make_response(redirect(url_for('login')))
    resp.delete_cookie('email')
    resp.delete_cookie('acc')
    resp.delete_cookie('username')
    return resp

if __name__=='__main__':
    app.run(host='192.168.1.9',port='2020',debug=True)