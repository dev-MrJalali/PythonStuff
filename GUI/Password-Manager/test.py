import tkinter as tk
from tkinter import ttk, messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Data Entry App")
        self.root.geometry("500x500")

        # Apply a modern theme
        style = ttk.Style()
        style.theme_use("clam")

        # Variables for checkboxes and length field
        self.use_number = tk.BooleanVar(value=True)
        self.use_alphabet = tk.BooleanVar(value=True)
        self.length_var = tk.IntVar(value=8)

        # Top frame for data entry
        self.entry_frame = ttk.LabelFrame(self.root, text="Data Entry", padding=(10, 10))
        self.entry_frame.pack(fill="x", padx=10, pady=10)

        # Checkboxes
        options_frame = ttk.Frame(self.entry_frame)
        options_frame.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")
        ttk.Label(options_frame, text="Options:").grid(row=0, column=0, sticky="w")
        ttk.Checkbutton(options_frame, text="Number", variable=self.use_number).grid(row=0, column=1, padx=5)
        ttk.Checkbutton(options_frame, text="Alphabet", variable=self.use_alphabet).grid(row=0, column=2, padx=5)

        # Length field
        ttk.Label(self.entry_frame, text="Length:").grid(row=1, column=0, sticky="e", padx=5)
        self.length_entry = ttk.Entry(self.entry_frame, textvariable=self.length_var, width=10)
        self.length_entry.grid(row=1, column=1, sticky="w")

        # Data fields
        ttk.Label(self.entry_frame, text="Title:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.title_entry = ttk.Entry(self.entry_frame)
        self.title_entry.grid(row=2, column=1, sticky="w", pady=5)

        ttk.Label(self.entry_frame, text="Username:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.username_entry = ttk.Entry(self.entry_frame)
        self.username_entry.grid(row=3, column=1, sticky="w", pady=5)

        ttk.Label(self.entry_frame, text="Password:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.password_entry = ttk.Entry(self.entry_frame, show="*")
        self.password_entry.grid(row=4, column=1, sticky="w", pady=5)

        # Buttons
        self.button_frame = ttk.Frame(self.entry_frame)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.button_frame, text="Add Data", command=self.add_data).grid(row=0, column=0, padx=5)
        ttk.Button(self.button_frame, text="Update Data", command=self.update_data).grid(row=0, column=1, padx=5)
        ttk.Button(self.button_frame, text="Delete Data", command=self.delete_data).grid(row=0, column=2, padx=5)

        # Bottom frame for displaying data
        self.display_frame = ttk.LabelFrame(self.root, text="Stored Data", padding=(10, 10))
        self.display_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(self.display_frame, columns=("Title", "Username", "Password"), show="headings", height=10)
        self.tree.heading("Title", text="Title")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.pack(fill="both", expand=True)

        # Add sample data
        self.load_sample_data()
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def load_sample_data(self):
        """Load some initial data into the treeview."""
        sample_data = [
            ("Admin Panel", "admin", "123456"),
            ("User Portal", "user1", "password1"),
            ("Database", "db_user", "db_pass"),
        ]
        for title, username, password in sample_data:
            self.tree.insert("", "end", values=(title, username, password))

    def on_tree_select(self, event):
        """Handle row selection in the Treeview."""
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            values = item["values"]
            # Populate the entry fields with the selected row's data
            self.title_entry.delete(0, "end")
            self.title_entry.insert(0, values[0])
            self.username_entry.delete(0, "end")
            self.username_entry.insert(0, values[1])
            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, values[2])

    def add_data(self):
        """Add data to the Treeview."""
        title = self.title_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if title and username and password:
            self.tree.insert("", "end", values=(title, username, password))
            self.clear_entries()
        else:
            messagebox.showwarning("Incomplete Data", "Please fill out all fields!")

    def update_data(self):
        """Update the selected row in the Treeview."""
        selected_item = self.tree.selection()
        if selected_item:
            title = self.title_entry.get()
            username = self.username_entry.get()
            password = self.password_entry.get()

            if title and username and password:
                # Update the selected item
                self.tree.item(selected_item, values=(title, username, password))
                self.clear_entries()
            else:
                messagebox.showwarning("Incomplete Data", "Please fill out all fields!")
        else:
            messagebox.showwarning("No Selection", "Please select a row to update!")

    def delete_data(self):
        """Delete the selected row from the Treeview."""
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            self.clear_entries()
        else:
            messagebox.showwarning("No Selection", "Please select a row to delete!")

    def clear_entries(self):
        """Clear all entry fields."""
        self.title_entry.delete(0, "end")
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
