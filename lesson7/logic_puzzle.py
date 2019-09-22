"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
"""
concept inventory:
person: 5
arrive: 5
role: programer, writer, manager, designer
buy: laptop, droid, tablet, iphone
"""
import itertools


def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    orderings = list(itertools.permutations([1, 2, 3, 4, 5]))
    order = next((Hamming, Knuth, Minsky, Simon, Wilkes)
                for Hamming, Knuth, Minsky, Simon, Wilkes in orderings
                if Knuth == 1 + Simon # 6
                for programmer, writer, manager, designer, _ in orderings
                if Knuth == manager + 1  # 10
                if designer != 4  # 7
                if programmer !=  Wilkes  # 2
                if writer != Minsky  # 4
                for laptop, droid, tablet, iphone, _ in orderings
                if (laptop == 1 and Wilkes == writer) or (laptop == writer and Wilkes == 1)  # 11
                if set([Wilkes, Hamming]) == set([droid, programmer]) # 3
                if (iphone == 2 or tablet ==2) # 12
                if designer != droid  # 9
                if Knuth != manager and tablet != manager  # 5
                if laptop == 3  # 1
                if tablet != 5  # 8
    )
    mapping = dict(zip(("Hamming", "Knuth", "Minsky", "Simon", "Wilkes"), order))
    return sorted(mapping, key=mapping.get)


print(logic_puzzle())
