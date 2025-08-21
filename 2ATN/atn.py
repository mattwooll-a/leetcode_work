# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 =0 
        num2 =0

        tens = 0 
        fin = False
        while fin != True:
            num1 += (l1.val * pow(10,tens))
            if l1.next != None:
                l1 = l1.next
                tens += 1
            else: 
                fin = True

        tens = 0 
        fin = False
        while fin != True:
            num2 += (l2.val * pow(10,tens))
            if l2.next != None:
                l2 = l2.next
                tens += 1
            else: 
                fin = True

        total = num1 + num2 
        print(total)


        l3 = ListNode()
        current = l3     

        for i in range(len(str(total))):
            digit = int(str(total)[-(i+1)])
            current.next = ListNode(val=digit)
            current = current.next
        l3 = l3.next



        return (l3)