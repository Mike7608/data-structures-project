"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue, Node


class TestStack(unittest.TestCase):
    node = Node("123", None)
    node2 = Node("321", node)

    def test_init_node(self):
        self.assertEqual(self.node.data, "123")
        self.assertEqual(self.node.next_node, None)
        self.assertEqual(self.node2.data, "321")
        self.assertEqual(self.node2.next_node, self.node)

    def test_init_queue(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        self.assertEqual(queue.head.data, "data1")
        queue.enqueue("data2")
        self.assertEqual(queue.head.next_node.data, "data2")

    def test_is_empty(self):
        queue = Queue()
        self.assertEqual(queue.is_empty(), True)

    def test_dequeue(self):
        queue = Queue()
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue('data1')
        self.assertEqual(queue.head.data, "data1")
        queue.enqueue("data2")

        # удаляем запись (data1)
        queue.dequeue()
        self.assertEqual(queue.head.data, "data2")

        # удаляем запись (data2)
        queue.dequeue()
        self.assertEqual(queue.tail, None)

    def test___str__(self):
        queue = Queue()
        self.assertEqual(str(queue), "")
        queue.enqueue('data1')
        self.assertEqual(str(queue), "data1")
