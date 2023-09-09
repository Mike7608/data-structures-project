"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList, Node


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