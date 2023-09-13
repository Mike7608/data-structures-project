class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data: dict):
        """
        Конструктор класса Node

        """
        self.data = data
        self.next = None


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next

        ll_string += ' None'
        return ll_string.strip()

    def to_list(self):
        """ Возвращает список с данными """
        node = self.head
        if node is None:
            return None

        ll_list = []

        while node:
            l_data = node.data
            ll_list.append(l_data)
            node = node.next

        return ll_list

    def get_data_by_id(self, value):
        """ Возвращает первый найденный в LinkedList словарь с ключом 'id' """

        node = self.head
        if node is None:
            return None

        while node:
            try:
                if node.data["id"] == value:
                    return node.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет id")
            node = node.next

