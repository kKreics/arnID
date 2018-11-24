import mailbox
import email
import re
import base64
import binascii

mbox = mailbox.mbox('my_mails.mbox')
verification = re.compile('order|privacy|account|confirm|sign\s?(up|out)|verif|address|phone|auth|passw|user|name|log(in|out)|mail|\bid\b', flags=re.IGNORECASE)
b64checker = re.compile('([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?')

def get_mytext(payload):
    if payload.get_content_maintype() == 'text':
        if b64checker.match(payload.get_payload()):
            try:
                bla = base64.b64decode(payload.get_payload())
                return bla.decode()
            except binascii.Error:
                pass
            except UnicodeDecodeError:
                pass
            except ValueError:
                pass
        return payload.get_payload()
    return None

def parse_email(from_header):
    return email.utils.parseaddr(from_header)[1].split('@')[-1]

def get_body(mail):
    l = []
    if mail.is_multipart():
        for part in mail.get_payload():
            sdss = get_mytext(part)
            if sdss is not None:
                l.append(sdss)
    else:
        if mail.get_content_maintype() == 'text':
            sdss = get_mytext(mail)
            if sdss is not None:
                l.append(sdss)
    
    return '\n'.join(l)

services = set()
for msg in mbox:
    f = parse_email(msg['From'])
    body = get_body(msg)
    if verification.match(body):
        if f not in services:
            services.add(f)
            print(f)
