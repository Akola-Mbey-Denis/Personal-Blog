from flask_mail import Mail,Message
mail = Mail()
 
 
def send_email(subject, sender, recipients,text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    mail.send(msg)