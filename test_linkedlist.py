import unittest
from LinkedLists import linkedlist

class TestLinkedList(unittest.TestCase):
    def test_add_first(self):       
        ll = linkedlist.LinkedList()
        n = linkedlist.Node("Costco")
        ll.add_first(n)
        self.assertEqual(ll.get(0), "Costco")

    def test_empty(self):
        ll = linkedlist.LinkedList()
        self.assertIsNone(ll.head)
        with self.assertRaises(Exception, ll.get(0), "Empty List"):
            ll.get(0)

if __name__ == '__main__':
    unittest.main()