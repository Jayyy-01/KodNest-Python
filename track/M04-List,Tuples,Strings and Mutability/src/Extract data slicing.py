    # Input: Python
    #        10
    #        20
    #        30
    
    # to get ouput as 
    # Middle: ytho
    # First Two: [10, 20]
    # Reverse Tuple: (30, 20, 10) 

word = input()

first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
records = (first, second, third)

middle = word[1:-1]
first = numbers[0:2]
reverse = records[::-1]

print(f"Middle: {middle}")
print(f"First Two: {first}")
print(f"Reverse Tuple: {reverse}")