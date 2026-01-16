class Razorpay:
    def makepayments(self,amount):
        print(f"Razorpayay {amount}")
    

class RazorpayAdapter:
    def __init__(self, razorpay):
        self.razorpay = razorpay
    
    def pay(self, amount):
        self.razorpay.makepayments(amount)

gateway = RazorpayAdapter(Razorpay())
gateway.pay(100)




# class Razorpay:
#     def make_payment(self, money):
#         print(f"Paid {money} using Razprpay")

# class PaymentAdapter:
#     def __init__(self, gateway):
#         self.gateway = gateway
    
#     def pay(self, amount):
#         self.gateway.make_payment(amount)


# raz = Razorpay()

# adapter = PaymentAdapter(raz)
# adapter.pay(50000)
