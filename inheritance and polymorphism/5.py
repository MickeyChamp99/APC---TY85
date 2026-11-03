class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")

class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")

e = EmailNotification()
s = SMSNotification()
p = PushNotification()

e.send()
s.send()
p.send()