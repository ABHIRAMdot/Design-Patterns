#strategic pattern
class PyamentStrategy:
    def pay(self, amount):
        pass

class UpiPayment(PyamentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} uaing UPI")

class CardPayment(PyamentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")

class Checkout:
    def __init__(self, pay_method):
        self.pay_method = pay_method

    def make_payment(self, amount):
        self.pay_method.pay(amount)


pay_method = UpiPayment()

strategy = Checkout(pay_method)

strategy.make_payment(10000)

checkout = Checkout(CardPayment())
checkout.make_payment(50000)
