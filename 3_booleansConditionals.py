#-----------------------------------------------    1     -----------------------------------------------
def sign(number):
    if(number>0):
        return 1
    elif(number<0):
        return -1
    else:
        return 0
#-----------------------------------------------    2     -----------------------------------------------
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies == 1:
        print("Splitting 1 candy")
    else: 
        print("Splitting", total_candies, "candies")
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

#-----------------------------------------------    3     -----------------------------------------------
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not (rain_level > 0 and is_workday)

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

#-----------------------------------------------    4     -----------------------------------------------
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0

#-----------------------------------------------    5a     -----------------------------------------------

def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

#-----------------------------------------------    5b     -----------------------------------------------

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion

#-----------------------------------------------    5c     -----------------------------------------------
    
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    number_toppings = int(ketchup) + int(mustard)
    print(number_toppings)
    return number_toppings == 1

#-----------------------------------------------    6     -----------------------------------------------

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    number_toppings = int(ketchup) + int(mustard) + int(onion)
    return number_toppings == 1
