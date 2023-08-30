"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack, Node


class TestStack(unittest.TestCase):
    node = Node("123", None)
    node2 = Node("321", node)

    def test_init_node(self):
        self.assertEqual(self.node.data, "123")
        self.assertEqual(self.node.next_node, None)
        self.assertEqual(self.node2.data, "321")
        self.assertEqual(self.node2.next_node, self.node)

    def test_stack_push(self):
        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        self.assertEqual(stack.top.data, "data2")
        self.assertEqual(stack.top.next_node, stack.top.next_node)
        self.assertEqual(stack.top.next_node.data, "data1")
        self.assertEqual(stack.top.next_node.next_node, None)

    def test_stack_pop(self):
        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        stack.pop()
        self.assertEqual(stack.top.data, "data1")
        self.assertEqual(stack.top.next_node, None)
        stack.pop()
        self.assertEqual(stack.top, None)

    def test___str__(self):
        stack = Stack()
        self.assertEqual(str(stack), "Stack (None)")
        stack.push("data1")
        self.assertEqual(str(stack), "Stack (data1)")