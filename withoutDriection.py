import tkinter as tk


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp.data
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            temp = current.next
            current.next = None
            return temp.data


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Linked List")
        self.master.geometry("400x300")

        self.list = LinkedList()

        self.output_label = tk.Label(master, text="", font=("Arial", 16))
        self.output_label.pack(side="top", pady=10)

        self.insert_button = tk.Button(
            master, text="Insert", font="arial 10 bold", width=15, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=10, command=self.insert_window)
        self.insert_button.pack(side="left", padx=10)

        self.delete_button = tk.Button(
            master, text="Delete", font="arial 10 bold", width=15, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=10, command=self.delete)
        self.delete_button.pack(side="right", padx=10)

        self.delete_button = tk.Button(
            master, text=" << EXIT", font="arial 10 bold", width=20, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=10, command=master.destroy)
        self.delete_button.pack(side="right", padx=10)

    def insert_window(self):
        self.insert_window = tk.Toplevel(self.master)
        self.insert_window.geometry("350x200+100+100")
        self.insert_window.title("Insert")

        self.entry_label = tk.Label(
            self.insert_window, text="Enter a value:", font="arial 15 bold")
        self.entry_label.pack(pady=10)

        self.entry_box = tk.Entry(
            self.insert_window, borderwidth=3, width=10, font="arial 15 bold")
        self.entry_box.pack()

        self.add_button = tk.Button(
            self.insert_window, text="Add", font="arial 10 bold", width=10, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=5, command=self.add)
        self.add_button.pack(pady=10)

    def add(self):
        value = self.entry_box.get()
        self.list.insert(value)
        self.output_label.configure(
            text="Linked List: " + str(self.list_values()))
        self.insert_window.destroy()

    def delete(self):
        deleted_value = self.list.delete()
        if deleted_value is None:
            self.output_label.configure(text="Linked List: Empty")
        else:
            self.output_label.configure(
                text="Linked List: " + str(self.list_values()) + "\nDeleted: " + str(deleted_value))

    def list_values(self):
        current = self.list.head
        values = []
        while current is not None:
            values.append(current.data)
            current = current.next
        return values


root = tk.Tk()
root.geometry("750x560+400+100")
app = App(root)
root.mainloop()
