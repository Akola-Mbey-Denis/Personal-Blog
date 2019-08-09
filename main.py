from flask import Blueprint,render_template,request,redirect,url_for
from Email import send_email
from config import Configuration



contact_mail= Blueprint('contact_mail',__name__,template_folder='templates',static_folder='static')
 
@contact_mail.route('/')
@contact_mail.route('/home')
def show_page():
    return render_template('index.html',title='Profile Blog-Denis Mbey Akola')

@contact_mail.route('/')
@contact_mail.route('/home',methods=['POST'])
def contact_me():
    name=request.form.get('name')
  
    email=request.form.get('email')
   
    message=request.form.get('message')
 
     
    # receipents=[Configuration.MAIL_DEFAULT_SENDER]
    send_email(subject='Your Blog Notice-'+name+ 'E-mail: '+ email, sender= request.form.get('email'),recipients=[ 'nforticsinterns@gmail.com'],
    text_body=message 
    )
    return redirect(url_for('contact_mail.show_page'))

