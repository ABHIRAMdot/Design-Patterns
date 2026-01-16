#Observer Pattern
class Observer:
    def update(self, message):
        pass

class SMSNotifier(Observer):
    def update(self, message):
        print("SMS", message)

class EmailNotifier(Observer):
    def update(self, message):
        print("Email", message)

class Order:
    def __init__(self):
        self.observers = []
        self.status = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update(F"Order updated to {self.status}")

    def set_status(self, status):
        self.status = status
        self.notify()



order = Order()

sms = SMSNotifier()
email = EmailNotifier()

order.add_observer(sms)
order.add_observer(email)

order.set_status("shipped")
order.set_status("Delivered")

