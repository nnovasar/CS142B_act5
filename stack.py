# Given the Node class below, write Mini-Py class called Stack that uses Node to store each data.
class Node (object):
    info: str
    next: "Node"

    def __init__(self: "Node", inf:str, nxt: "Node"):
        self.info = inf
        self.next = nxt

    def print(self: "Node"):
        print(self.info)
        if self.next != None:
            self.next.print()

    def print_node(self: "Node"):
        print(self.info)


# Write a constructor that does not take any parameter. Only initializes the data members 'head' and 'size'.
#   head points to the top of the stack 
#   size is the number of items in the stack


    # Write a push method that takes data (type str) and pushes it on top of the stack.


    # Write a pop method that removes and returns the data on top of the stack.

    # Write is_empty method that returns true if the stack is empty.

    # Write stack_size method that returns the size of the stack.

    # Lastly, write a print method that prints all the items in the stack. 

def main():
    S: "Stack" = Stack()  
    print("**** Stack before push ****")
    S.print()

    months:[str] = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    for s in months:
        S.push(s)
    print("**** Stack after push ****")
    S.print()

    S.pop()
    S.pop()
    print("**** Stack size after 2 pops ****")
    print(S.stack_size())
    
    print("Now pop all the stack")
    while not S.is_empty():
        S.pop().print_node()    
    print("**** Stack after all pops ****")
    S.print()

main()

