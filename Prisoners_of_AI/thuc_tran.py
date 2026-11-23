def net_worth_before(assets, debts):
    """Net worth = assets - debts."""
    return assets - debts


def total_loss(fine, court_fees, restitution, forfeiture,
               yearly_income, sentence_years):
    """Total money lost because of the conviction."""
    lost_income = yearly_income * sentence_years
    return fine + court_fees + restitution + forfeiture + lost_income


def net_worth_after(before, loss):
    """Net worth after conviction = before - total loss."""
    return before - loss


# ---------- GUI ----------

class NetWorthFrame(tk.Frame):
    # (label shown on screen, key name)
    FIELDS = [
        ("Total assets ($)", "assets"),
        ("Total debts ($)", "debts"),
        ("Yearly income ($)", "yearly_income"),
        ("Fine ($)", "fine"),
        ("Court fees / legal fees ($)", "court_fees"),
        ("Restitution ($)", "restitution"),
        ("Forfeited assets ($)", "forfeiture"),
        ("Years in prison", "sentence_years"),
    ]

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.entries = {}

        tk.Label(self, text="Net Worth Before & After Conviction",
                 font=("Arial", 14, "bold")).grid(row=0, column=0,
                                                  columnspan=2, pady=10)

        row = 1
        for label_text, key in self.FIELDS:
            tk.Label(self, text=label_text).grid(row=row, column=0,
                                                 sticky="w", padx=5, pady=2)
            entry = tk.Entry(self, width=20)
            entry.grid(row=row, column=1, padx=5, pady=2)
            self.entries[key] = entry
            row += 1

        tk.Button(self, text="Calculate",
                  command=self.calculate).grid(row=row, column=0,
                                               columnspan=2, pady=10)

        self.result_label = tk.Label(self, text="", justify="left")
        self.result_label.grid(row=row + 1, column=0, columnspan=2)

    def get_number(self, key):
        """Read a number from an entry box. Empty = 0."""
        text = self.entries[key].get().strip()
        if text == "":
            return 0.0
        return float(text)

    def calculate(self):
        try:
            assets = self.get_number("assets")
            debts = self.get_number("debts")
            income = self.get_number("yearly_income")
            fine = self.get_number("fine")
            fees = self.get_number("court_fees")
            restitution = self.get_number("restitution")
            forfeiture = self.get_number("forfeiture")
            years = self.get_number("sentence_years")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return

        before = net_worth_before(assets, debts)
        loss = total_loss(fine, fees, restitution, forfeiture, income, years)
        after = net_worth_after(before, loss)

        self.result_label.config(
            text=("Net worth BEFORE: ${:,.2f}\n"
                  "Total loss: ${:,.2f}\n"
                  "Net worth AFTER: ${:,.2f}").format(before, loss, after))


# Run this file alone to test: python networth.py
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Net Worth")
    NetWorthFrame(root).pack(padx=10, pady=10)
    root.mainloop()
