from homework11.task02 import ElderDiscount, MorningDiscount, Order


def test_order_morning_discount():
    order_morning = Order(100, MorningDiscount)
    assert order_morning.final_price() == 50


def test_order_elder_discount():
    order_elder = Order(100, ElderDiscount)
    assert order_elder.final_price() == 10
