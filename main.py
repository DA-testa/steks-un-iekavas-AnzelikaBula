#221RDC032 18.gr Anzelika Bula 

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(right, left):

    return (right + left) in ["()", "[]", "{}"]


def find_mismatch(text):
    
    opening_brackets_stack = []
    for i, next in enumerate(text):
        
        if next in "([{":
            
            # Process opening bracket, write your code here
            
            opening_brackets_stack.append(Bracket(next, i))
            pass


        if next in ")]}":
            
            # Process closing bracket, write your code here
            
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[len(opening_brackets_stack)-1][0], next):
                return i + 1 

            if are_matching(opening_brackets_stack[len(opening_brackets_stack)-1][0], next):
                opening_brackets_stack.pop()

            pass

    if opening_brackets_stack :
        return opening_brackets_stack[len(opening_brackets_stack)-1][1] + 1

def main():
    
    text = input("Ievad iekavas: ")

    mismatch = find_mismatch(text)

    if not mismatch :
        print("Success")
        
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
