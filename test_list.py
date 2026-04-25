from double_linked_list import AdvancedLinkedList


def test_advanced_linked_list():

    ll = AdvancedLinkedList()

    print("Добавление элементов:")
    ll.insert_at_head(10)
    ll.insert_at_head(5)
    ll.insert_at_tail(20)
    ll.insert_at_tail(30)

    print("\nВывод списка с головы:")
    ll.print_ll_from_head()

    print("\nВывод списка с хвоста:")
    ll.print_ll_from_tail()

    print(f"\nДлина списка: {ll.len_ll()}")

    print("\nВставка элемента 15 на позицию 2:")
    ll.insert_at_index(15, 2)
    ll.print_ll_from_head()

    print(f"\nПроверка наличия:")
    print(f"   15 в списке? {ll.contains_from_head(15)}")
    print(f"   99 в списке? {ll.contains_from_tail(99)}")

    print("\nУдаление элемента на позиции 3:")
    ll.remove_node_index(3)
    ll.print_ll_from_head()

    print("\nУдаление элемента со значением 15:")
    ll.remove_node_data(15)
    ll.print_ll_from_head()

    print(f"\nФинальная длина списка: {ll.len_ll()}")
    print("Оставшиеся элементы:")
    ll.print_ll_from_head()

if __name__ == "__main__":
    test_advanced_linked_list()