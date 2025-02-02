from flask import Flask, render_template, request, jsonify, send_file
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
load_dotenv()

# Configuration
UPLOAD_FOLDER = 'uploads'
TEMPLATE_FOLDER = 'templates/email_templates'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'jpg', 'png'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TEMPLATE_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

class EmailSender:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")

    def send_email(self, recipient, subject, body, attachments=None):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'html'))

            if attachments:
                for attachment in attachments:
                    with open(os.path.join(app.config['UPLOAD_FOLDER'], attachment), 'rb') as f:
                        part = MIMEApplication(f.read(), Name=attachment)
                        part['Content-Disposition'] = f'attachment; filename="{attachment}"'
                        msg.attach(part)

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    templates = []
    for filename in os.listdir(TEMPLATE_FOLDER):
        if filename.endswith('.json'):
            with open(os.path.join(TEMPLATE_FOLDER, filename), 'r') as f:
                template = json.load(f)
                templates.append({
                    'name': template['name'],
                    'subject': template['subject'],
                    'body': template['body']
                })
    return render_template('index.html', templates=templates)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'filename': filename})
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/save_template', methods=['POST'])
def save_template():
    data = request.get_json()
    template_name = secure_filename(data['name'])
    
    template_data = {
        'name': data['name'],
        'subject': data['subject'],
        'body': data['body']
    }
    
    with open(os.path.join(TEMPLATE_FOLDER, f'{template_name}.json'), 'w') as f:
        json.dump(template_data, f)
    
    return jsonify({'success': True})

@app.route('/send_emails', methods=['POST'])
def send_emails():
    data = request.get_json()
    recipients = data.get('recipients', [])
    subject = data.get('subject', '')
    body = data.get('body', '')
    attachments = data.get('attachments', [])
    
    sender = EmailSender()
    results = []
    
    for recipient in recipients:
        success = sender.send_email(recipient, subject, body, attachments)
        results.append({
            'email': recipient,
            'success': success
        })
    
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)