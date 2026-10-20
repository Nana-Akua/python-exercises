

#Exercise 2: create a sum function to that does the same thing as the built in sum function

def mysum(*numbers):
    sumval = 0
    for num in numbers:
        sumval += num
    return sumval

print(f'q1: {mysum(10, 20, 30, 40)}')


#write a funciton that takes in a optional second argument which is used as a starting point for the summing 
def mysum_args(*numbers, strtpoint = None):
    sumval = 0 

    #evaluate whether strt point has a value 
    if strtpoint is None:
        strtpoint = 0
    else:
        strtpoint = strtpoint

    #sum up all of the values 
    for num in numbers:
        sumval += num

    return sumval + strtpoint

print(f'q2: {mysum_args(1,23,4,5,strtpoint= 4)}')

#write a function that takes a list of numbers and returns the average of those numbers
def avgcalc(*numbers):
    sumval = 0
    amountofnum = len(numbers)

    for num in numbers:
        sumval += num

    return sumval/amountofnum
print(f'q3: {avgcalc(2,3,45,6,40)}')

#write a function that takes a list of words. return a tuple contianing 3 integers represneting the length of the shortest word, longest word, average word length
def len_of_words(*words):
    word_len_tup = ()
    sumoflen = 0

    for word in words:
        word_len = len(word)
        sumoflen += word_len
        word_len_tup +=(word_len,)

    average_len = sumoflen / len(word_len_tup)

    max_len = max(word_len_tup)
    min_len = min(word_len_tup)

    return min_len, max_len, average_len
       
print(f'q4: {len_of_words("Hi", "NanaAkuaOfosu", "why", "sweet")}')

#write a function that takes a list of python objects. Sum the objects that are either integers or can be turned into integers and ignoring the rest
def list_converter(*lists):
    sum = 0
    for val in lists:
        try:
            converted_num = int(val)
            sum += converted_num
        except ValueError:
            pass
    return sum
print(f'q5: {list_converter("Nana", 4, 6, 10, "10")}')