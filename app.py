from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os,requests

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail SMTP server
app.config['MAIL_PORT'] = 465  # SSL port
app.config['MAIL_USE_TLS'] = False  # Use TLS (True for non-SSL ports like 587)
app.config['MAIL_USE_SSL'] = True  # Use SSL
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')  # Your email address (set via environment variables)
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')  # Your email password (set via environment variables)
app.config['MAIL_DEFAULT_SENDER'] = 'customer'  # Sender's email address

mail = Mail(app)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html') 

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/advertise')
def advertise():
    return render_template('indevlopment.html')

@app.route('/distribute')
def distribute():
    return render_template('indevlopment.html')


@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    recaptcha_response = request.form.get('g-recaptcha-response')
    print(recaptcha_response)
    print(f"Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")

    # Verify reCAPTCHA
    secret_key = '6Lch_cQqAAAAAOyqXoGtofZXqmojr99lwmjDNb9y'  # Replace with your secret key
    recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
    recaptcha_payload = {
        'secret': secret_key,
        'response': recaptcha_response
    }

    recaptcha_request = requests.post(recaptcha_url, data=recaptcha_payload)
    recaptcha_result = recaptcha_request.json()
    print(recaptcha_result)

    if not recaptcha_result.get('success'):
        return "reCAPTCHA verification failed. Please try again."
    else:
    # If reCAPTCHA succeeds, proceed with sending the message
        msg = Message(
            subject="New Contact Form Message",
            recipients=["stayhydratedrj@gmail.com"],
            body=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        )

        try:
            mail.send(msg)
            return "Message sent successfully!"
        except Exception as e:
            return f"Failed to send message. Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)


# 6Lch_cQqAAAAAOTJmE6Vv9YemzX3geISeGubK_SV

# secret 
# 6Lch_cQqAAAAAOyqXoGtofZXqmojr99lwmjDNb9y