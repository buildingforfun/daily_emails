# Project: Daily emails

I want to create my own daily email newsletter.

Tasks:
- [x] Sending email python script
- [x] Create an executable bash script to run python script
- [x] Edit the crontab file to run the script automatically
- [x] Make the email inputs using argparse
- [x] Write a script to parse any url and get the links from the URL
- [x] Connect up random url to email script in body of email
- [x] Move code to Raspberry pi to send the email so not reliant on laptop being on

## Bash script
```bash
#!/bin/bash

# Change to the directory containing the Python script
cd /path/to/directory

# Run the Python script
python3 send_email.py --from-address [INSERT] --password [INSERT] --to-address [INSERT]
```

## csv file format
urls,subfolder

## Crontab
Crontab allows us to schedule tasks on the machine. I'm currently using the raspberry pi to run this everyday.

Run:
export EDITOR=nano
crontab -e

Write:
min hour * * * /path/to/bash
