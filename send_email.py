# Standard imports
import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Local imports
from kindle_clipper import  kindle_clipper
from parse_url import  return_random_link

def send_email(from_address, password, to_address, clips_path):
    """
    Sends a email from a google email addresses

    Args:
        from_address (str) : sender email address
        password (str) : sender email password
        to_address (str) : recipient email
    
    """
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "Daily email!"

    # URLs from csv file
    csv_urls_df = pd.read_csv('urls.csv')
    csv_url_random = []
    try:
        for index, csv_url in enumerate(csv_urls_df.iloc[:, 0]):
            print(f"Processing row {index}:")
            print(f"CSV URL: {csv_url}")
            
            try:
                url = return_random_link(csv_url)
                print(f"Random URL: {url}")
                csv_url_random.append(url)
            except Exception as e:
                print(f"Error processing row {index}: {str(e)}")
            
            print("---")  # Separator between rows
    except Exception as e:
        print(f"An error occurred: {str(e)}")



    # Create email body2
    body = "<html><body><p>Read these posts:</p><ul>"
    for url in csv_url_random:
        body += f"<li><a href='{url}'>{url}</a></li>"  # Create a list item for each URL
    body += f"<li><a>{str(kindle_clipper(clips_path))}</a></li>"
    body += "</ul></body></html>"

    # Add bodies to email
    msg.attach(MIMEText(body, 'html'))

    # Sending the email
    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()  # Terminate the SMTP session

parser = argparse.ArgumentParser(description='Send emails')
parser.add_argument('--from-address', required = True, help='From email addres')
parser.add_argument('--password', required = True, help='Email address authentication password')
parser.add_argument('--to-address', required = True, help='To email addres')
parser.add_argument('--clips', required = True, help='Path to kindle clippings text file')
args = parser.parse_args()

sender_email = args.from_address
sender_password = args.password
recipient_email = args.to_address
clips_path=args.clips

send_email(sender_email, sender_password, recipient_email, clips_path)