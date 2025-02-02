# Email Automation System

A Flask-based email automation system with template support and file attachments.

## Features

- Send emails to multiple recipients
- Email template support
- File attachment handling
- HTML email support
- Template management system

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Varunpoojari/email-automation-system.git
cd email-automation-system
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create necessary directories:
```bash
mkdir uploads
mkdir templates/email_templates
```

5. Set up environment variables:
Create a .env file with:
```
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
```

6. Run the application:
```bash
python app.py
```

## Usage

1. Access the web interface at `http://localhost:5000`
2. Use existing templates or create new ones
3. Add recipients (one email per line)
4. Add attachments if needed
5. Send emails and track delivery status

## Security Notes

- Never commit the .env file
- Use App Passwords for Gmail
- Keep the uploads folder secure

## License

MIT License