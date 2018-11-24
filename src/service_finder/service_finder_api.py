import email
import re
import base64
import binascii

verification = re.compile('(un)?subscrib|order|privacy|account|confirm|sign\s?(up|out)|verif|address|phone|auth|passw|user|name|log(in|out)|mail|\bid\b', flags=re.IGNORECASE)
b64checker = re.compile('([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?')

def get_mytext(payload):
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

def get_body(mail):
    l = []
    sdss = get_mytext(part)
    if sdss is not None:
        return sdss
    else:
        return ''
 
def is_signed_up(sender, body):
    sender = email.utils.parseaddr(sender)[1].split('@')[-1]
    body = get_body(body)
    if verification.match(body):
        return (sender, True)
    else:
        return (sender, False)

