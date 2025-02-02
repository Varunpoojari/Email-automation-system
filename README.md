# 📧 Email Automation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A powerful, user-friendly Flask-based email automation system that enables you to send personalized emails to multiple recipients with template support and file attachments.

## ✨ Features

### 📝 Email Management
- Send emails to multiple recipients simultaneously
- Real-time delivery status tracking
- HTML email support for rich formatting
- Custom subject lines and message bodies

### 📁 Template System
- Save and reuse email templates
- Pre-built templates for common scenarios
- Easy template management
- HTML support in templates
- Quick template selection

### 📎 Attachments
- Support for multiple file attachments
- Drag and drop file upload
- Supported formats:
  - Documents (PDF, DOC, DOCX)
  - Spreadsheets (XLS, XLSX)
  - Images (JPG, PNG)
  - Text files (TXT)
- 16MB file size limit per attachment

### 🔒 Security
- Environment-based configuration
- Secure file upload handling
- Gmail App Password support
- Input sanitization

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Gmail account with App Password

### Installation

1. Clone the repository
```bash
git clone https://github.com/Varunpoojari/email-automation-system.git
cd email-automation-system
```

2. Create and activate virtual environment
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create necessary directories
```bash
mkdir uploads
mkdir templates/email_templates
```

5. Configure environment variables
Create a `.env` file in the root directory:
```env
EMAIL=your_gmail@gmail.com
PASSWORD=your_app_password
```

### 🔐 Gmail App Password Setup

1. Go to your Google Account settings
2. Enable 2-Step Verification if not already enabled
3. Generate an App Password:
   - Go to Security settings
   - Find "App passwords" under 2-Step Verification
   - Select "Mail" and your device
   - Copy the generated 16-character password

### 🖥️ Running the Application

1. Start the server
```bash
python app.py
```

2. Access the web interface at `http://localhost:5000`

## 💡 Usage Guide

### Sending Emails
1. Enter recipient email addresses (one per line)
2. Write your subject line
3. Compose your message (HTML supported)
4. Add attachments if needed
5. Click "Send Emails"

### Using Templates
1. Select an existing template from the dropdown
2. Modify the content as needed
3. Save new templates with the "Save Template" button

### Managing Attachments
1. Click "Choose File" to select files
2. Remove attachments using the × button
3. View all attached files in the attachment list

## 🛠️ Advanced Configuration

### Customizing File Upload Limits
Modify `app.py` to adjust file size limits:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
```

### Adding Custom Templates
Create new JSON files in `templates/email_templates/`:
```json
{
    "name": "Template Name",
    "subject": "Email Subject",
    "body": "HTML Email Body"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Flask framework
- Python email libraries
- Gmail SMTP services

## 📞 Support

For issues, questions, or contributions, please:
1. Check existing [Issues](https://github.com/Varunpoojari/email-automation-system/issues)
2. Open a new issue if needed
3. Contact the maintainers

---
Made with ❤️ by [Varun Poojari](https://github.com/Varunpoojari)