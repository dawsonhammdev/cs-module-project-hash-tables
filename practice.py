# # Add up and print the sum of the all of the minimum elements of each inner array:

# array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# # The expected output is given by:
# # 4 + -1 + 9 + -56 + 201 + 18 = 175

# # we will need to access the inner arrays
# # inner for loops
# # need to compare the value to see which is less
# # once we have the lesser value from each array we need to sum them up and print

# def compare():
#     sum = 0
#     for x in array:
#         # compare
#         sum += min(x)
#     return print(sum)
       

# print(compare())

# # Add up and print the sum of the all of the minimum elements 
# # of each inner array. Each array may contain additional arrays 
# # nested arbitrarily deep, in which case the minimum value for the 
# # nested array should be added to the total.

# arr = [
#   [8, [4]], 
#   [[90, 91], -1, 3], 
#   [9, 62], 
#   [[-7, -1, [-56, [-6]]]], 
#   [201], 
#   [[76, 0], 18], 
# ]

# cache = {

# }

# def fib(n):
#     # this takes a long time because we are rerunning all of the calculations.
#     # basecase
#     if n<= 1:
#         return n
#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)
#     return cache[n]

# for i in range(200):
#     print(f'{i:3}: {fib(i)}')

# ceasar cipher
'''
GOATS
JEHFN
'''

# encode_table = {
#     'A': 'H',
#     'B': 'Z',
#     'C': 'Y',
#     'D': 'W',
#     'E': 'O',
#     'F': 'R',
#     'G': 'J',
#     'H': 'D',
#     'I': 'P',
#     'J': 'T',
#     'K': 'I',
#     'L': 'G',
#     'M': 'L',
#     'N': 'C',
#     'O': 'E',
#     'P': 'X',
#     'Q': 'K',
#     'R': 'U',
#     'S': 'N',
#     'T': 'F',
#     'U': 'A',
#     'V': 'M',
#     'W': 'B',
#     'X': 'Q',
#     'Y': 'V',
#     'Z': 'S'
# }

# decode_table = {}

# # build the reverse map
# for k, v in encode_table.items():
#     decode_table[v] = k

# def encode(s):
#     r = ""
#     for c in s:
#         r+= encode_table[c]
    
#     return r

# def decode(s):
#     r = ""

#     for c in s:
#         r+= decode_table[c]
#     return r

# print(encode("GOATS"))
# print(encode("ELEPHANTS"))

# print(decode("JEHFN"))
# print(decode("OGOXDHCFN"))
import hashlib
import random

def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff

def how_many_before_collision(buckets, loops=1):
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = random.random()
            index = hash_function(random_key) % buckets

            if index not in tried:
                tried.add(index)
                tries += 1

            else:
                break

        print(f"{buckets} buckets, {tries} hashes before collision. ({tries / buckets * 100:.1f}% full)")

how_many_before_collision(65536, 10)




