class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.is_empty():
            return None
        else:
            removed_node = self.head
            self.head = removed_node.next_node
            if self.head is None:
                self.tail = None
            return removed_node.data

    def is_empty(self):
        """
        Метод проверки очереди на отсутствие записей.
        :return: True если записи отсутствуют
        """
        value = self.head is None
        return value

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = []
        if self.is_empty():
            return ""
        else:
            node = self.head
            while node is not None:
                result.append(node.data)
                node = node.next_node
            return "\n".join(result)
