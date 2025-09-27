import os
import asyncio
from dotenv import load_dotenv
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from jinja2 import Environment, FileSystemLoader

load_dotenv()

# Set up the Jinja2 environment for loading email templates
templates = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "../templates/email_templates")))

# Load email configuration from environment variables
conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT", 587)),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    MAIL_FROM_NAME="StudyGenie"
)

async def send_email_async(subject: str, email_to: str, template_name: str, body_data: dict):
    """
    Sends an email asynchronously using a Jinja2 template.
    
    Args:
        subject (str): The subject of the email.
        email_to (str): The recipient's email address.
        template_name (str): The name of the HTML template file (e.g., "registration_success.html").
        body_data (dict): A dictionary of data to pass to the template.
    """
    # Get the template and render it with the provided data
    template = templates.get_template(template_name)
    html_content = template.render(**body_data)

    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=html_content,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
