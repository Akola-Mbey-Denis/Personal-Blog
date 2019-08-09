from flask import Flask
from config import Configuration
from Email import mail

def create_app():
    '''
    This method loads the configurations and dependencies for my Flask Application.
    '''
    app=Flask(__name__,template_folder='templates',static_folder='static')
    
    app.config.from_object(Configuration)
    #initialising the mail server 
    mail.init_app(app)

    #Mail sending blueprint
    from main import contact_mail as email_blue_print
    app.register_blueprint(email_blue_print)
    

    return app


