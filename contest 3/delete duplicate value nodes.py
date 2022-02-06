def removeDuplicates(llist):
    # Write your code here
        temp = llist
        if(llist == None):
            return None
        while(llist.next != None):
            if (llist.data == llist.next.data):
                llist.next = llist.next.next
            else :
                llist = llist.next
        
        return temp
