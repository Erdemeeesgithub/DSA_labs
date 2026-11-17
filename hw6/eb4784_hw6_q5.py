from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(cur1, cur2, result):
        if cur1 is srt_lnk_lst1.trailer and cur2 is srt_lnk_lst2.trailer:
            return result
        if cur2 is srt_lnk_lst2.trailer or (cur1 is not srt_lnk_lst1.trailer and cur1.data <= cur2.data):
            result.add_last(cur1.data)
            return merge_sublists(cur1.next, cur2, result)
        else:
            result.add_last(cur2.data)
            return merge_sublists(cur1, cur2.next, result)

    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next, DoublyLinkedList())
