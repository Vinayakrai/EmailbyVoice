# EmailbyVoice

**EmailbyVoice** is a Python-based application that enables users to send emails through voice commands. Utilizing libraries such as `smtplib`, `SpeechRecognition`, `pyttsx3`, and `EmailMessage`, this project offers a hands-free approach to composing and sending emails.

## 🚀 Features

- **Voice-Activated Email Composition**: Compose emails by speaking, eliminating the need for manual typing.
- **Text-to-Speech Feedback**: The system provides audio prompts and confirmations using text-to-speech capabilities.
- **Email Sending via SMTP**: Sends emails through SMTP protocol, compatible with various email services.

## 🛠️ Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Required Libraries**:
  - `smtplib`
  - `SpeechRecognition`
  - `pyttsx3`
  - `email.message`

## 📦 Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/Vinayakrai/EmailbyVoice.git
cd EmailbyVoice
```

2. **Install Required Packages**:

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install SpeechRecognition pyttsx3
```

*Note*: `smtplib` and `email.message` are part of Python's standard library and do not require separate installation.

## 🚀 Usage

1. **Configure Email Credentials**:

- Open the `email_bot.py` file.
- Locate the section where email credentials are set.
- Replace the placeholder values with your actual email address and password.

2. **Run the Script**:

```bash
python email_bot.py
```

The script will:

- Prompt you to speak the recipient's email address.
- Prompt you to speak the subject of the email.
- Prompt you to speak the body of the email.
- Send the composed email to the specified recipient.

## ⚠️ Notes

- Ensure your microphone is properly connected and configured.
- For Gmail users, you may need to enable access for less secure apps or use an app-specific password.
- Always handle your email credentials securely and avoid hardcoding them in scripts.

