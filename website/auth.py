from flask import Blueprint,render_template,request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login() :
    return render_template('login.html')

@auth.route('/logout')
def logout() :
    return render_template('logout.html')

@auth.route('/sign-up',methods=['GET','POST'])
def sign_app() :
    if request.method == 'POST':
        email= request.form.get('email')
        firstName= request.form.get('firstName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')
        
        if len(email) < 4 :
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('Name must be greater than 2 characters', category='error')
        elif password1!=password2 :
            flash('Password not matching ', category='error')
        elif len(password1) <  7:
            flash('password must be greater than 7 characters', category='error')
            
        else :
            flash('Account created succesfully', category='success')
    return render_template('sign_up.html')