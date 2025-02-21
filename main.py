import random
import China, Austria
from China import cook as China_cook
from Austria import cook as Austria_cook
from latam.Argentina import cook as Argentina_cook
from latam.Brazil import cook as Brazil_cook



def cook():
    print("we are making paella")


print("a random number is:", random.randint(1, 10))
China.cook()
China.greet()
cook()
Austria.greet()
Argentina_cook()
Brazil_cook()


