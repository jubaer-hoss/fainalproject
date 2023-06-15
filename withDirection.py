import tkinter as tk


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def delete(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            node = self.head
            self.head = None
            return node.value
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            node = current.next
            current.next = None
            return node.value


class LinkedListGUI:
    def __init__(self, master):
        self.master = master
        master.title("Linked List")

        self.linked_list = LinkedList()

        self.top_frame = tk.Frame(master)
        self.top_frame.pack(side=tk.TOP)

        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack(side=tk.BOTTOM)

        self.insert_label = tk.Label(
            self.top_frame, text="Insert Value:", font="arial 20 bold")
        self.insert_label.pack()  # side=tk.LEFT

        self.insert_fast_button = tk.Button(
            self.top_frame, text="Insert first", font="arial 10 bold", width=15, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=10, command=self.insert_value)
        self.insert_fast_button.pack(side=tk.LEFT)

        self.insert_entry = tk.Entry(
            self.top_frame, borderwidth=3, width=10, font="arial 15 bold")
        self.insert_entry.pack(side=tk.LEFT)

        self.insert_button = tk.Button(
            self.top_frame, text="Insert last", font="arial 10 bold", width=15, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=10, command=self.insert_value)
        self.insert_button.pack(side=tk.LEFT)

        self.output_text = tk.Text(
            self.bottom_frame, height=10, font="arial 15 bold")
        self.output_text.pack()

        self.delete_button = tk.Button(
            self.bottom_frame, text="<< EXIT", font="arial 10 bold", width=15, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=10, command=quit)
        self.delete_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(
            self.bottom_frame, text="Delete", font="arial 10 bold", width=15, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=10, command=self.delete_value)
        self.delete_button.pack(side=tk.LEFT)

        self.update_button = tk.Button(
            self.bottom_frame, text="update", font="arial 10 bold", width=15, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=10, command=self.update_value)
        self.update_button.pack(side=tk.LEFT)

        self.sarch_button = tk.Button(
            self.bottom_frame, text="search", font="arial 10 bold", width=15, borderwidth=5, fg="#1A044D", bg="#CCCCFF", pady=10, command=self.update_value)
        self.sarch_button.pack(side=tk.LEFT)

    def update_value(self):
        pass

    def insert_value(self):
        value = self.insert_entry.get()
        self.linked_list.insert(value)
        self.update_output()

    def delete_value(self):
        value = self.linked_list.delete()
        if value is not None:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"{value}\n")
        self.update_output()

    def update_output(self):
        current = self.linked_list.head
        self.output_text.delete("1.0", tk.END)
        while current is not None:
            self.output_text.insert(
                tk.END, f"{current.value} -> ")
            current = current.next
        self.output_text.insert(tk.END,  "None\n")


root = tk.Tk()
root.geometry("1000x550+10+10")
linked_list_gui = LinkedListGUI(root)
root.mainloop()
