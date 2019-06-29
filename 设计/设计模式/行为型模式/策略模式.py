"""
策略模式
根据不同的输入采用不同的策略
比如买东西超过10个打八折，超过20个打七折
对外暴露统一的接口，内部采用不同的策略计算
"""

class Order:
    def __init__(self,price,discount_strategy=None):
        self.price=price
        self.discount_strategy=discount_strategy
    def price_after_discount(self):
        if self.discount_strategy:
            discount=self.discount_strategy(self)
        else:
            discount=0
        return self.price-discount
    def __repr__(self):
        fmt="<Price:{},price after discount:{}>"
        return fmt.format(self.price,self.price_after_discount())

def ten_percent_discount(order):
    return order.price*0.10

def on_sale_discount(order):
    return order.price*0.25+20

order0=Order(100)
order1=Order(100,discount_strategy=ten_percent_discount)
order2=Order(1000,discount_strategy=on_sale_discount)
print(order0)
print(order1)
print(order2)