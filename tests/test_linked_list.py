"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList, Node
from io import StringIO
from unittest.mock import patch


class TestLinkedList(unittest.TestCase):

    def test_init_node(self):
        node = Node({"id": 1})
        self.assertEqual(node.data,  {"id": 1})
        self.assertEqual(node.next, None)

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(str(ll), "{'id': 1} -> None")

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 2} -> None")

    def test_insert_at_end_no_begin(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 3})
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test___str__(self):
        ll = LinkedList()
        self.assertEqual(str(ll), "None")

    def test_to_list(self):
        ll = LinkedList()
        self.assertEqual(ll.to_list(), None)

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = ll.to_list()
        self.assertEqual(lst[0],  {'id': 0, 'username': 'serebro'})
        self.assertEqual(lst[1],  {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(lst[2],  {'id': 2, 'username': 'mik.roz'})
        self.assertEqual(lst[3],  {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id(self):
        ll = LinkedList()
        self.assertEqual(ll.get_data_by_id(3), None)

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        test = ll.get_data_by_id(3)
        self.assertEqual(test, {'id': 3, 'username': 'mosh_s'})

    @patch('sys.stdout', new_callable=StringIO)
    def test_TypeError_get_data_by_id(self, mock):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

