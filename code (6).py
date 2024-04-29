class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printlinkedlist(head):
    curr = head
    while curr != None:
        print(curr.data,end = "-->")
        curr = curr.next
    else:
        print("None")
    print()
def insertatendoftail(head,ele):
    newblock = Node(ele)
    if head == None:
        return newblock

    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newblock

    return head

def deleteNodeAtSpecificPositon(head,position):
    if position == 1:
    curr = head
    index = 1
    while index != position - 1:
        curr = curr.next
        index += 1
    mainNode = curr.next
    nextNode = mainNode.next
    mainNode.next = None
    curr.next

n = int(input())
l = list(map(int,input().split()))
head = None
for ele in l:
    head = insertatendoftail(head,ele)
printlinkedlist(head)

