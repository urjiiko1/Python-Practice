# here is function code

def greet(name):
    return f"Hello {name}, welcome to Ethiopian Airlines!"
print(greet("Gemachis Tesfaye"))
print(greet("Donald Trump😁"))   #this is simple greeting function only  use print for different passengers
print(greet("Elon Musk🚀"))
print(greet("Barack Obama"))
print(greet("Bill Gates💻"))

print("          ")
# calculate ticket price after dsicount
def calculate(price, discount):
    final_price=price-(price*discount/100)
    return final_price

print("The final price after discount is $", calculate(100,10))
print("The final price after discount is $", calculate(50.3,5))
print("The final price after discount is $", calculate(200,15))