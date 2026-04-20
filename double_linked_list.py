class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
        self.head = new_node
        print(f"Теперь в голове узел с данными {self.head.data}")

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        print(f"Теперь в хвосте узел с данными {self.tail.data}")

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        print(f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}")
        return removed_node.data

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        print(f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}")
        return removed_node.data

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        print("Список выведен с начала")


class AdvancedLinkedList(LinkedList):

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        print("Список выведен с конца")

    def len_ll(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next_node
        return count

    def insert_at_index(self, data, index):
        if index < 0 or index > self.len_ll():
            print("Индекс вне диапазона. Элемент не добавлен.")
            return

        if index == 0:
            self.insert_at_head(data)
            return

        if index == self.len_ll():
            self.insert_at_tail(data)
            return

        new_node = Node(data)
        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        new_node.prev_node = current_node
        current_node.next_node.prev_node = new_node
        current_node.next_node = new_node
        print(f"Элемент с данными {data} добавлен на позицию {index}")

    def remove_node_index(self, index):
        if self.head is None:
            print("Список пуст, удалять нечего.")
            return

        length = self.len_ll()
        if index < 0 or index >= length:
            print("Индекс вне диапазона.")
            return

        if index == 0:
            return self.remove_from_head()

        if index == length - 1:
            return self.remove_from_tail()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node

        current_node.prev_node.next_node = current_node.next_node
        current_node.next_node.prev_node = current_node.prev_node
        print(f"Удалён элемент с данными {current_node.data} на позиции {index}")
        return current_node.data

    def remove_node_data(self, data):
        if self.head is None:
            print("Список пуст, удалять нечего.")
            return

        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node == self.head:
                    return self.remove_from_head()
                elif current_node == self.tail:
                    return self.remove_from_tail()
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    print(f"Удалён элемент с данными {data}")
                    return data
            current_node = current_node.next_node

        print(f"Элемент с данными {data} не найден.")
        return None

    def contains_from_head(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):
        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, from_head=True):
        if from_head:
            return self.contains_from_head(data)
        else:
            return self.contains_from_tail(data)