class Node:                           
     def __init__(self, data):
         self.left = None   
         self.right = None  
         self.data = data        
                                      
     def insert(self, data):               
         if self.data:                     
             if data < self.data:          
                 if self.left is None:     
                     self.left = Node(data)
                 else:                      
                     self.left.insert(data) 
             elif data > self.data:         
                 if self.right is None:     
                     self.right = Node(data)
                 else:                      
                     self.right.insert(data)
         else:               
             self.data = data
                          
     def __next__(self):  
         return self.right
                                   
     def __prev__(self):  
         return self.left          
                                    
     def print_tree(self):         
         if self.left:              
             self.left.print_tree() 