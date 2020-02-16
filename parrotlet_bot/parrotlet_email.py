__author__ = 'Timothy Lam'

import smtplib
import config
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

contact = {'me': 'lamt3@lsbu.ac.uk',
           'emeka': 'ugwuanye@lsbu.ac.uk',
           'saptarshi': 'ghoshs4@lsbu.ac.uk',
           'kasra': 'kasra.kassai@lsbu.ac.uk',
           'godwin': 'idojeg@lsbu.ac.uk',
           'brahim': 'elboudab@lsbu.ac.uk',
           'tasos': 'tdagiuklas@lsbu.ac.uk',
           'iqbal': 'm.iqbal@lsbu.ac.uk',
           'safia': 'safia.barikzai@lsbu.ac.uk'
           }


def check(email):

    if re.search(regex, email):
        return 'valid'

    else:
        return 'invalid'


def send_email(subject, msg, _send_email):

    try:
        server = smtplib.SMTP_SSL('smtp.office365.com')
        server.ehlo()
        server.login(config.email_address, config.password)
        _message = 'Subject: {}\n\n{}\n\n Sent By Parrotlet \n\n'.format(subject, msg)
        server.sendmail(config.email_address, _send_email, _message)
        server.quit()
        return f"Email sent to {_send_email}"
    except Exception as e:
        return f"Could not send email \n {e}"
