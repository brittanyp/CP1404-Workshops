import random
MAX_INCREASE = 0.175 # 10%
MAX_DECREASE = 0.05 # 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0
day = 0
price = INITIAL_PRICE

def format_currency(value):
    restr="${:,.2f}".format(value)
    return(restr);
print(format_currency(price))
while price >= MIN_PRICE and price <= MAX_PRICE:
 priceChange = 0
 # generate a random integer of 1 or 2
 # if it's 1, the price increases, otherwise it decreases
 if random.randint(1, 2) == 1:
 # generate a random floating-point number
 # between 0 and MAX_INCREASE
    priceChange = random.uniform(0, MAX_INCREASE)
 else:
 # generate a random floating-point number
 # between negative MAX_INCREASE and 0
    priceChange = random.uniform(-MAX_DECREASE, 0)
 price *= (1 + priceChange)
 priceStr=format_currency(price)
 print("On day {} price is: {}".format(day, priceStr))
 day = day + 1