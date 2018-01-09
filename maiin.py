from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def signup_form():
    return render_template('home.html')

@app.route("/signup", methods=['POST'])
def signup():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    pass_error = ''
    verify_error = ''
    email_error = ''

    username = str(username)
    password = str(password)
    verify = str(verify)
    email = str(email)

#Errors for leaving stuff empty 
    if len(username) ==0:
        user_error = "Your username field is empty!"
    if len(password) ==0:
        pass_error = "Your password field is empty!"
    if len(verify) ==0:
        verify_error = "Your verify password field is empty!"
    if len(email) >20:
        email_error = "Please enter a valid email or leave it blank!"

#Errors for spaces in fields
    if " " in username:
        user_error = "You have a space in your username!"
    if " " in password:
        pass_error = "You have a space in your password!"
    if " " in email:
        email_error = "You have a space in your email!"

#Errors for lenth of username and password
    if len(username) <3 or len(username) >20:
        user_error = "You username must be between 3 and 20 characters long!"
    if len(password) <3 or len(password) >20:
        pass_error = "Your password must be between 3 and 20 characters long!"

#Error for non-matching password 
    if password != verify:
        verify_error = "Your passwords do not match!"
    if len(email) >=3:
        if "@" not in email or "." not in email:
            email_error = "Please enter a valid email!"


#if not any errors return the whole form
    if not user_error and not pass_error and not verify_error and not pass_error and not email_error:
        return redirect('/valid-user?username={0}'.format(username))
    else:
        return render_template('home.html', 
                                user_error=user_error, pass_error=pass_error, 
                                verify_error=verify_error, email_error=email_error)

@app.route('/valid-user')
def valid_user():
    name = request.args.get('username')
    return '<h1>Welcome, {0}!</h1>'.format(name)
    
   

app.run()