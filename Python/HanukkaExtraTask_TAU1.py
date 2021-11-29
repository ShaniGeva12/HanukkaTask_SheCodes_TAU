# we need to sum the candles used in 8 days of Hanukka
# every day we light 1 shamash + X candles according to the day number

# begginers
# we create a counter
# we add 8 times 1 + dayNumber (which starts from 1 and increases every time)

# mid level
def sum_the_candles():
    # we create a counter
    sum = 0

    # we add 8 times 1 + dayNumber (which starts from 1 and increases every time)
    for dayNumber in range(1, 9):
        sum += 1 + dayNumber
        
    return sum
    
print(sum_the_candles())

# expert
# create another func to print the candles
# use | for the candles
# use ! for the shamash
def let_there_be_light():
    for dayNumber in range(1, 9):
        # to print just 1 line for each day we'll use a var to save our Menorah
        # and initialize it with the shamash
        result = "!"
        # for evety day passed we'll light a candle
        for x in range(dayNumber):
            result += ' |'
        # for the remaining days we leave a place in our Menorah
        for x in range(8-dayNumber):
            result += ' _'
        # and then we print the complite Menorah
        print (result)
        
let_there_be_light()
        
        