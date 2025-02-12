"""
Assignment Questions on Dictionaries
Q 1. Write a python program to add key to the dictionary.
    Sample Dictionary = {0:10,1:20}
    Expected Result = {0:10,1:20,2:30}
  
Q 2. Below are the two list convert them into Dictonary.
keys=['Ten','Twenty','Thirty']
values = [10,20,30]
Expected Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    
Q 3. Access the value of key 'history'
sampleDict = {
    "class":{
        "student":{
            "name":"mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}

 Q 4. Given the following Dictonary:
    inventory = {
        'gold':500,
        'pouch':['flint','twine','gemstone'],
        'backpack':['xylophone','dagger','bedroll','bread loaf']
    }
    
    a) Add a key to inventory called 'pocket'
    b) set the value of 'pocket' to be a list consisting of [ '/]
      the strings 'seashell','strange breey' and 'lint'
    c) .sort() the items of the list stored under backpack key.
    d) then .remove('dagger') from the list of items stored under the 'backpack' Key.
    e) Add 50 to the number stored under gold key.

Q 5- A) Given a dictionary D, print the support count of each unique values and form a new dictionary with unique values as keys and supoort count as values. Print the new dictionary (D1).
Input:
D={
T1: [E, K, M, N, O,Y],
T2: [D,E,K,N,O,Y],
T3:[A,E,K,M],
T4:[C,K,M,U,Y],
T5:[C,E,I,K,O,O]
}
B) Considering the above support count of dictionary D1, sort the dictionary in decreasing order.
C) Remove the key and values from dictionary D1, that does not satisfy minimum support count. (Minimum Support count=3)
D) Given the updated dictionary D1 that satisfy minimum support count and the original Dictionary D, delete the values from D which is not present in D1. Now, print the dictionary D.
"""