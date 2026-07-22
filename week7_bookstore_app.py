# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Qiansen
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: games and add-ons
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.
class Games:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, new_price):
        if new_price < 0:
            print("Price cannot be below zero.")
        else:
            self.price = new_price

    def play(self):
        print (f"starting the game: {self.name}")
item1 =Games("Elden Ring", 50)
item2 = Games ("RE2r", 40)
#print(item1.name)
#print(item2.name)
#item1.set_price(-5)
#print(item1.play())

# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: It will print "Price cannot be below zero." and the price will not change.
#   Paste the message you see here: Price cannot be below zero.


# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.
class Action(Games):
    pass
    def play(self):
        print (f"Action game starting")

#print (item2.play())
# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: ______________


# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: ______________



# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
        print (item.name + " added!")
    def checkout (self):
        total = 0
        for item in self.items:
            item.play()
            total = total + item.price
        print ("Total: $" +str(total))
# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.


# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
store = {"1": item1, "2": item2}
cart = Cart()


# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: it'll add game 1 to cart 
shopping = True 
while shopping:
    choice = input ("Pick 1, 2, or 'done': ")
    if choice == "done":
        shopping = False
    else:
        cart.add(store[choice])

cart.checkout()
# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.


# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================