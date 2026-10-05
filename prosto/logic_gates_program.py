import tkinter as tk
from tkinter import ttk, messagebox

# Логические операции
def calc_gate(gate, a, b=None):
    a = int(a)
    if gate == "NOT":
        return 1 - a

    b = int(b)
    if gate == "AND":
        return a & b
    if gate == "OR":
        return a | b
    if gate == "NAND":
        return 1 - (a & b)
    if gate == "NOR":
        return 1 - (a | b)
    if gate == "XOR":
        return a ^ b
    if gate == "XNOR":
        return 1 - (a ^ b)


EXPRESSIONS = {
    "AND": "Y = A ∧ B",
    "OR": "Y = A ∨ B",
    "NOT": "Y = ¬A",
    "NAND": "Y = ¬(A ∧ B)",
    "NOR": "Y = ¬(A ∨ B)",
    "XOR": "Y = A ⊕ B",
    "XNOR": "Y = ¬(A ⊕ B)",
}


class LogicGatesApp:
    def __init__(self, root):
        self.root = root
        root.title("Лаборатория логических элементов")
        root.geometry("820x650")
        root.minsize(720, 580)

        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        title = ttk.Label(
            root,
            text="Логические элементы и таблицы истинности",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=(15, 5))

        subtitle = ttk.Label(
            root,
            text="Выберите логический элемент и получите результат для входов A и B.",
            font=("Arial", 10)
        )
        subtitle.pack(pady=(0, 12))

        controls = ttk.Frame(root)
        controls.pack(fill="x", padx=25)

        ttk.Label(controls, text="Элемент:", font=("Arial", 11, "bold")).grid(
            row=0, column=0, padx=(0, 8), pady=8, sticky="w"
        )

        self.gate_var = tk.StringVar(value="AND")
        self.gate_box = ttk.Combobox(
            controls,
            textvariable=self.gate_var,
            values=["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"],
            state="readonly",
            width=12
        )
        self.gate_box.grid(row=0, column=1, padx=5, pady=8)
        self.gate_box.bind("<<ComboboxSelected>>", lambda e: self.update_ui())

        ttk.Label(controls, text="A:", font=("Arial", 11, "bold")).grid(
            row=0, column=2, padx=(30, 5)
        )
        self.a_var = tk.IntVar(value=0)
        self.a_box = ttk.Combobox(
            controls, textvariable=self.a_var, values=[0, 1],
            state="readonly", width=5
        )
        self.a_box.grid(row=0, column=3)
        self.a_box.bind("<<ComboboxSelected>>", lambda e: self.calculate())

        ttk.Label(controls, text="B:", font=("Arial", 11, "bold")).grid(
            row=0, column=4, padx=(20, 5)
        )
        self.b_var = tk.IntVar(value=0)
        self.b_box = ttk.Combobox(
            controls, textvariable=self.b_var, values=[0, 1],
            state="readonly", width=5
        )
        self.b_box.grid(row=0, column=5)
        self.b_box.bind("<<ComboboxSelected>>", lambda e: self.calculate())

        self.b_label = controls.grid_slaves(row=0, column=4)[0]

        ttk.Button(
            controls, text="Рассчитать", command=self.calculate
        ).grid(row=0, column=6, padx=(25, 0))

        self.result_label = ttk.Label(
            root, text="Y = 0", font=("Arial", 16, "bold")
        )
        self.result_label.pack(pady=8)

        self.expression_label = ttk.Label(
            root, text=EXPRESSIONS["AND"], font=("Arial", 12)
        )
        self.expression_label.pack(pady=(0, 10))

        # Таблица истинности
        table_frame = ttk.LabelFrame(root, text="Таблица истинности")
        table_frame.pack(fill="both", expand=True, padx=25, pady=10)

        self.tree = ttk.Treeview(
            table_frame, columns=("A", "B", "Y"), show="headings", height=10
        )
        self.tree.heading("A", text="A")
        self.tree.heading("B", text="B")
        self.tree.heading("Y", text="Y")
        self.tree.column("A", width=120, anchor="center")
        self.tree.column("B", width=120, anchor="center")
        self.tree.column("Y", width=120, anchor="center")
        self.tree.pack(pady=15)

        info = ttk.Label(
            root,
            text="0 — ложь, 1 — истина. Для NOT используется только вход A.",
            font=("Arial", 10)
        )
        info.pack(pady=(0, 12))

        self.update_ui()

    def update_ui(self):
        gate = self.gate_var.get()
        is_not = gate == "NOT"

        if is_not:
            self.b_box.configure(state="disabled")
            self.b_label.configure(state="disabled")
        else:
            self.b_box.configure(state="readonly")
            self.b_label.configure(state="normal")

        self.expression_label.configure(text=EXPRESSIONS[gate])
        self.fill_truth_table()
        self.calculate()

    def calculate(self):
        gate = self.gate_var.get()
        a = self.a_var.get()

        if gate == "NOT":
            y = calc_gate(gate, a)
        else:
            b = self.b_var.get()
            y = calc_gate(gate, a, b)

        self.result_label.configure(text=f"Y = {y}")

    def fill_truth_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        gate = self.gate_var.get()

        if gate == "NOT":
            for a in [0, 1]:
                y = calc_gate(gate, a)
                self.tree.insert("", "end", values=(a, "—", y))
        else:
            for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                y = calc_gate(gate, a, b)
                self.tree.insert("", "end", values=(a, b, y))


def main():
    root = tk.Tk()
    app = LogicGatesApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
