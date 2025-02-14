# 1

# def mx(x, y):
#     return x if x > y else y

# print(mx(5, 20)) 


# 2

# number_input = int(input("enter your num:"))

# def fizz_buzz(num):
#     if num % 15 == 0:
#         return "fizzbuzz"
#     if num % 3 == 0:
#         return "fizz"
#     if num % 5 == 0:
#         return "buzz"
    
#     else:
#         print(num)

# print(fizz_buzz(number_input))

# 3

# speed_lim = 70
# actual_speed = int(input("speed:"))
# points = 0

# def demerit(speed):
#     if speed < speed_lim:
#         return "ok"
#     points = (speed - speed_lim) // 5
#     if points > 12:
#         return "License suspended"
    
#     return f"points: {points}"

# print(demerit(actual_speed))

# 4

ask_limit = int(input("limit "))
def showNumbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(f"{i} EVEN")
        else:
            print(f"{i} ODD")

print(showNumbers(ask_limit))

# 5

