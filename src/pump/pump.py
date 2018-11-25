from imapclient import IMAPClient
import email


class EmailPump:
    def __init__(self, host, user, password):
        client = IMAPClient(host)
        client.login(user, password)
        self.client = client
    
    def get_email_count(self, folder):
        select = self.client.select_folder(folder)
        return select[b'EXISTS']

    def get_emails(self, criteria):
        messages = self.client.search(criteria)
        for msgid, data in self.client.fetch(messages, ['ENVELOPE', 'RFC822', 'BODY[TEXT]']).items():
            parsedEmail = email.message_from_string(data[b'RFC822'].decode())
            body = email.message_from_string(data[b'BODY[TEXT]'].decode())
            if parsedEmail.is_multipart():
                parsedBody = parsedEmail.get_payload(0)
            else:
                parsedBody = parsedEmail.get_payload()
                
            yield data[b'ENVELOPE'], parsedBody

    


