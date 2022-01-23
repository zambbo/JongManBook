# 토핑을 최대 20개까지 추가할 수 있는 피자를 비트마스킹을 이용해 나타내보자!

zero_topping = 0

full_topping = (1<<20)-1

def add_topping(toppings,pizza_bit):
    toppings |= (1<<pizza_bit)
    return toppings

def isadded(toppings,pizza_bit):
    if toppings & (1<<pizza_bit):
        return 'added'
    else:
        return 'not added'

def remove_topping(toppings,pizza_bit):
    toppings &= ~(1<<pizza_bit)
    return toppings

def remove_lsb(toppings):
    toppings &= (toppings-1)
    return toppings

def get_lsb(toppings):
    toppings &= (-toppings)
    return toppings

if __name__ == '__main__':
    toppings = int(input())

    print(add_topping(toppings,2))
    print(isadded(toppings,3))
    print(remove_topping(toppings,2))
    print(get_lsb(toppings))
    print(remove_lsb(toppings))