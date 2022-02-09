import random
from time import thread_time
class LinkedList:
    
    # The __Node class is used internally by the LinkedList class. It is 
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name). 
    class __Node:
        def __init__(self,item,next=None):
            self.item = item
            self.next = next
            
        def getItem(self):
            return self.item
        
        def getNext(self):
            return self.next
        
        def setItem(self, item):
            self.item = item
            
        def setNext(self,next):
            self.next = next
            
    def __init__(self,contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. The both point to a 
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item. 
        # Its purpose is to eliminate special cases in the code below. 
        self.first = LinkedList.__Node(None,None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)
          
    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
                
            return cursor.getItem()
        
        raise IndexError("LinkedList index out of range")
    
    def __setitem__(self,index,val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
                
            cursor.setItem(val)
            return 
        
        raise IndexError("LinkedList assignment index out of range")
    
    def insert(self,index,item):
        cursor = self.first
        
        if index < self.numItems: 
            for i in range(index):
                cursor = cursor.getNext()
                
            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)
            
            
    def __add__(self,other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                str(type(self)) + " + " + str(type(other)))

        result = LinkedList()
        
        cursor = self.first.getNext()
        
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
            
        cursor = other.first.getNext()
                    
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
   
        return result
    
    
    def __contains__(self,item):
      for i in self:
        if i == item:
          return True
      return False
 
    def __delitem__(self,index):
      cursor = self.first.getNext()

      for i in range(index-1):
        cursor = cursor.getNext()
      newNext = cursor.getNext().getNext()
      cursor.setNext(newNext)
      self.numItems -= 1
            
    def __eq__(self,other):
        if type(other) != type(self):
            return False
        
        if self.numItems != other.numItems:
            return False
        
        cursor1 = self.first.getNext()
        cursor2 = other.first.getNext()
        while cursor1 != None:
            if cursor1.getItem() != cursor2.getItem():
                return False
            cursor1 = cursor1.getNext()
            cursor2 = cursor2.getNext()
            
        return True
    
    def __iter__(self):
        # This is left as an exercies for the reader.
        cursor = self.first.getNext()
        while cursor != None:
          yield cursor.getItem()
          cursor = cursor.getNext()

    def __len__(self):
        return self.numItems

    def append(self,item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

        
    def __str__(self):
        cursor = self.first.getNext()
        outString = "["

        while True:
          outString += str(cursor.getItem())
          cursor = cursor.getNext()

          if cursor != None:
            outString += ","
          else:
            break
        return outString + "]"
    
    def __repr__(self):
        # This is left as an exercise for the reader.
        pass              
    def split(self, index):
      cursor = self.first.getNext()
      newList = LinkedList()
      for i in range(index-1):
        cursor = cursor.getNext()

      newLast = cursor

      cursor = cursor.getNext()
      while cursor != None:
        newList.append(cursor.getItem())
        cursor = cursor.getNext()

      newLast.setNext(None)
      newList.numItems = self.numItems - index
      self.numItems = index
      return newList

    def sorted(self):
      cursor = self.first.getNext()
 
      while cursor.getNext() != None:
        prev = cursor.getItem()
        cursor = cursor.getNext()
        if prev > cursor.getItem():
          return False
      return True

    def merge(self, other):
      if type(self) != type(other):
        raise TypeError("Merge undefined for " + \
          str(type(self)) + " + " + str(type(other)))
      
      cursor_self = self.first.getNext()
      cursor_other = other.first.getNext()
      merged_list = LinkedList()

      while cursor_self != None:
        if cursor_other != None:
          if cursor_self.getItem() < cursor_other.getItem():
            merged_list.append(cursor_self.getItem())
            cursor_self = cursor_self.getNext()
          else:
            merged_list.append(cursor_other.getItem())
            cursor_other = cursor_other.getNext()
        else:
          merged_list.append(cursor_self.getItem())
          cursor_self = cursor_self.getNext()
      while cursor_other != None:
        merged_list.append(cursor_other.getItem())
        cursor_other = cursor_other.getNext()
      
      self.first = merged_list.first
      self.numItems = merged_list.numItems
    
    def mergesort(self):
      if self.numItems == 1:
        pass
      else:
        halftwo = self.split(self.numItems // 2)
        halftwo.mergesort()
        self.mergesort()
        self.merge(halftwo)




                
def main():
    lst = LinkedList()
    
    for i in range(100):
        lst.append(i)
    
    lst2 = LinkedList(lst)
    
    print(lst)
    print(lst2)
    
    if lst == lst2:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
    
    lst3 = lst + lst2
    
    if len(lst3) == len(lst) + len(lst2):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")
        
    
    if 1 in lst3:
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")        
    
    if 2 in lst3:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")        
    
    del lst[1]
    
    if 1 in lst:
        print("Test 5 Failed")
    else:
        print("Test 5 Passed")        
    
    if len(lst) == 99:
        print("Test 6 Passed")
    else:
        print("Test 6 Failed")        
        
    if lst == lst2:
        print("Test 7 Failed")
    else:
        print("Test 7 Passed")        
    
    del lst2[2]
    
    if lst == lst2:
        print("Test 8 Failed")
    else:
        print("Test 8 Passed")  
        
    
    lst4 = LinkedList(lst)
    lst.insert(0,100)
    lst4 = LinkedList([100]) + lst4
    
    if lst == lst4:
        print("Test 9 Passed")
    else:
        print("Test 9 Failed")
        
    lst.insert(1000,333)
    lst4.append(333)

    if lst == lst4:
        print("Test 10 Passed")
    else:
        print("Test 10 Failed")  
        
    print(lst)
    print(lst4)

    l5t = LinkedList([1,2,3,4,5,6,7,8])
    lst6 = l5t.split(4)
    
    if (l5t == LinkedList([1,2,3,4]) and (lst6 == LinkedList([5,6,7,8]))):
      print("Test 11 Passed")
    else:
      print("Test 11 Failed")

    lst7 = LinkedList([1,3,5,7,9])
    lst8 = LinkedList([0,2,4,6,8])
    lst7.merge(lst8)
    if lst8.sorted():
      print("Test 12 Passed")
    else:
      print("Test 12 Failed")
    
    lst9 = LinkedList([4,9,6,3,1,5,2,7,8])
    lst9.mergesort()
    if lst9.sorted():
      print("Test 13 Passed")
    else:
      print("Test 13 Failed")
    
if __name__ == "__main__":
    pass
f = open('random.csv', 'w')
for i in range(1,10000):
  bruh = list(range(i))
  random.shuffle(bruh)
  linkedbruh = LinkedList(bruh)
  runtime = thread_time()
  linkedbruh.mergesort()
  bruhntime = thread_time() - runtime
  f.write('{},{}\n'.format(i, bruhntime))
f.close()