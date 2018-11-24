from imapclient import IMAPClient


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
        for msgid, data in self.client.fetch(messages, ['ENVELOPE'], ).items():
            yield data[b'ENVELOPE']

    


