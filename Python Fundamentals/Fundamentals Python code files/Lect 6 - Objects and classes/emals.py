class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send_true(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list_of_emails = []

data_entry = input()
while data_entry != "Stop":
    info = data_entry.split(" ")
    sender_info = info[0]
    receiver_info = info[1]
    content_info = info[2]
    email = Email(sender_info, receiver_info, content_info)
    list_of_emails.append(email)
    data_entry = input()

sent_entry = list(map(int, input().split(", ")))

for index in sent_entry:
    list_of_emails[index].send_true()

for emails in list_of_emails:
    print(emails.get_info())
