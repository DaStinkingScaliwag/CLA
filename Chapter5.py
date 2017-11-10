from itertools import permutations
from itertools import groupby

def probabilityOfTriangle(sticks):
    """
    This function takes a list of the lengths of sticks in a bag, and
    outputs the probability that Alice would be able to pull three sticks
    and make a triangle from them.
    """
    pulls = removeDuplicates([sorted(i) for i in permutations(sticks, 3)])
    triangles = [a+b>c and b+c>a and c+a>b for a, b, c in pulls]
    return (sum(triangles)/len(triangles))*100

def removeDuplicates(iterable):

    """
    This function removes the duplicate items from a list
    """
    return list(k for k, _ in groupby(sorted(iterable)))

def questionOne():
    """
    This functions outputs the probability that in a bag of sticks measuring
    1", 3", 5", 7", and 9" that Alice could make a triangle from 3 random sticks
    """
    print("Answer to question 1:")
    print("{}% chance".format(probabilityOfTriangle([1, 3, 5, 7, 9])))


def questionTwo():
    sticks = [1, 3, 5, 7, 9]
    numberCorrect = 0
    for n in range(1, 16):
        """
        The number 0 is set as a lower limit because no side of a triangle can 0" long.
        The number 16 is used as an upper limit because the sum of the two largest sticks
        in the original bag is 16" (9" + 7"), so this replacement side must be less than
        the sum of the other two sides .
        """
        for i in range(5):
            test = [stick for stick in sticks]
            test[i] = n
            if probabilityOfTriangle(test) == 50:
                numberCorrect += 1
                print('Replace stick {}" with stick {} in'.format(sticks[i], n))
    if numberCorrect == 0:
        print("No Answer")

def questionThreeAndFour():
    """
    This function reuses the probabilityOfTriangle function to determine whether a bag has a 0% chance of
    producing a triangle, which would explain Alice's confidence. This is done by creating every combination
    of 3 unique sticks with measures less than 10" and plugging them into the probabilityOfTriangle function
    """
    answers = 0
    sticks = range(1,10)
    combos = removeDuplicates([sorted(i) for i in permutations(sticks, 5)])
    a=[]
    for bag in combos:
        if probabilityOfTriangle(bag) == 0:
            answers += 1
            a.append(bag)
            print('The bag could contain sticks with the lengths of ' + '", '.join(map(str,bag))+'"')
    if answers == 0:
        print("No Answer")

"""
These lines are just used to output my solutions
"""
questionOne()
print()
print("Answer to question 2:")
questionTwo()
print()
print("Answers to questions 3 & 4:")
questionThreeAndFour()