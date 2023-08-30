#-----------------------------------------------    1     -----------------------------------------------
def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    result = None
    if len(L)>1:
        result=L[1]
    return result

#-----------------------------------------------    2     -----------------------------------------------
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    worst_team=teams[-1]
    worst_team_capitain=worst_team[1]
    return worst_team_capitain

#-----------------------------------------------    3     -----------------------------------------------
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    first_place = racers[0]
    last_place = racers[-1]
    racers[0] = last_place
    racers[-1] = first_place

#-----------------------------------------------    4     -----------------------------------------------
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [ 3 ,2 ,0 ,2 ]

#-----------------------------------------------    5     -----------------------------------------------
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    ind = arrivals.index(name) # gets the index
    
    half = len(arrivals)/2
    return ind >= half and ind != len(arrivals) -1