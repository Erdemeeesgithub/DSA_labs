from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    result = DoublyLinkedList()
    for elem in lnk_lst:
        result.add_last(elem)          
    return result
 
 
def deep_copy_linked_list(lnk_lst):
    result = DoublyLinkedList()
    for elem in lnk_lst:
        if isinstance(elem, DoublyLinkedList):
            result.add_last(deep_copy_linked_list(elem))  
        else:
            result.add_last(elem)                        
    return result
 