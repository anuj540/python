
import random


def coin_simulation():
    count_heads = 0
    count_tails = 0
    for i in range(1, 10):
     number = random.randint(0, 1)  
     coin = random.choice(["head", "tail"])
     
     if number == 0:
        print ("head")
     else:
        print ("tail") 

     
        print(f"random number:{number}")
        print(f"pick any choice:{coin}")
        if coin == "head":
            count_heads += 1
        else:
            count_tails += 1
    print(f"Total heads: {count_heads}")
    print(f"Total tails: {count_tails}")
    return count_heads, count_tails
    


 

number = coin_simulation 
print(number())


# coin()=random.choice(["head","tail"])
# number=random.randint(1,100)
# print(f"random number:{number}")
# print(f"pick any choice:{coin}")

