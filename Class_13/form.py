import tkinter as tk
from tkinter import ttk, messagebox
import random
import os

class RetailBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Retail Billing System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#2E8B57") # SeaGreen background

        # Custom Colors
        title_color = "#FFD700" # Gold
        bg_color = "#2E8B57" # SeaGreen
        frame_bg_color = "#3CB371" # MediumSeaGreen
        label_fg_color = "white"
        entry_bg_color = "#F0FFF0" # Honeydew
        button_bg_color = "#4682B4" # SteelBlue

        # Title
        title_label = tk.Label(
            self.root,
            text="Retail Billing System",
            bd=12,
            relief=tk.GROOVE,
            bg=frame_bg_color,
            fg=title_color,
            font=("Arial", 30, "bold"),
            pady=2
        )
        title_label.pack(fill=tk.X)

        # ======== Item Prices (in BDT for approximation) =========
        self.prices = {
            "cosmetics": {"Bath Soap": 40, "Face Cream": 120, "Face Wash": 150, "Hair Spray": 250, "Hair Gel": 90, "Body Lotion": 180},
            "grocery": {"Rice": 80, "Oil": 180, "Daal": 130, "Wheat": 60, "Sugar": 100, "Tea": 220},
            "cold_drinks": {"Water": 20, "Cake": 350, "Chocolate": 90, "Apple": 200, "Lemon": 15, "Pizza": 500}
        }
        self.tax_rates = {"cosmetics": 0.05, "grocery": 0.02, "cold_drinks": 0.10} # 5%, 2%, 10%

        # ======== Variables =========
        # Customer Details
        self.customer_name = tk.StringVar()
        self.customer_phone = tk.StringVar()
        self.bill_number = tk.StringVar()
        x = random.randint(1000, 9999)
        self.bill_number.set(str(x))

        # Cosmetics
        self.bath_soap = tk.IntVar()
        self.face_cream = tk.IntVar()
        self.face_wash = tk.IntVar()
        self.hair_spray = tk.IntVar()
        self.hair_gel = tk.IntVar()
        self.body_lotion = tk.IntVar()

        # Grocery
        self.rice = tk.IntVar()
        self.oil = tk.IntVar()
        self.daal = tk.IntVar()
        self.wheat = tk.IntVar()
        self.sugar = tk.IntVar()
        self.tea = tk.IntVar()

        # Cold Drinks
        self.water = tk.IntVar()
        self.cake = tk.IntVar()
        self.chocolate = tk.IntVar()
        self.apple = tk.IntVar()
        self.lemon = tk.IntVar()
        self.pizza = tk.IntVar()

        # Bill Menu
        self.cosmetic_price = tk.StringVar()
        self.grocery_price = tk.StringVar()
        self.cold_drink_price = tk.StringVar()
        self.cosmetic_tax = tk.StringVar()
        self.grocery_tax = tk.StringVar()
        self.cold_drink_tax = tk.StringVar()
        self.total_bill = tk.StringVar()


        # ======== Customer Details Frame =========
        customer_frame = tk.LabelFrame(
            self.root, text="Customer Details", font=("Arial", 12, "bold"),
            fg=label_fg_color, bg=frame_bg_color, relief=tk.GROOVE, bd=10
        )
        customer_frame.pack(fill=tk.X, padx=10, pady=5)
        self.create_customer_widgets(customer_frame, label_fg_color, entry_bg_color, button_bg_color)

        # ======== Products Frame (Container) =========
        products_container = tk.Frame(self.root, bg=bg_color)
        products_container.pack(fill=tk.BOTH, expand=True, padx=10)

        # ======== Cosmetics Frame ========
        cosmetics_frame = self.create_product_frame(products_container, "Cosmetics", label_fg_color, frame_bg_color)
        cosmetics_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.cosmetic_vars = {"Bath Soap": self.bath_soap, "Face Cream": self.face_cream, "Face Wash": self.face_wash, "Hair Spray": self.hair_spray, "Hair Gel": self.hair_gel, "Body Lotion": self.body_lotion}
        self.populate_product_widgets(cosmetics_frame, self.cosmetic_vars, label_fg_color, entry_bg_color)

        # ======== Grocery Frame ========
        grocery_frame = self.create_product_frame(products_container, "Grocery", label_fg_color, frame_bg_color)
        grocery_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.grocery_vars = {"Rice": self.rice, "Oil": self.oil, "Daal": self.daal, "Wheat": self.wheat, "Sugar": self.sugar, "Tea": self.tea}
        self.populate_product_widgets(grocery_frame, self.grocery_vars, label_fg_color, entry_bg_color)

        # ======== Cold Drinks Frame ========
        cold_drinks_frame = self.create_product_frame(products_container, "Cold Drinks", label_fg_color, frame_bg_color)
        cold_drinks_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.cold_drink_vars = {"Water": self.water, "Cake": self.cake, "Chocolate": self.chocolate, "Apple": self.apple, "Lemon": self.lemon, "Pizza": self.pizza}
        self.populate_product_widgets(cold_drinks_frame, self.cold_drink_vars, label_fg_color, entry_bg_color)

        # ======== Bill Area ========
        bill_area_frame = tk.Frame(products_container, relief=tk.GROOVE, bd=10)
        bill_area_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tk.Label(bill_area_frame, text="Bill Area", font="arial 12 bold", bd=7, relief=tk.GROOVE).pack(fill=tk.X)
        
        yscroll = tk.Scrollbar(bill_area_frame, orient=tk.VERTICAL)
        self.bill_text_area = tk.Text(bill_area_frame, yscrollcommand=yscroll.set)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        yscroll.config(command=self.bill_text_area.yview)
        self.bill_text_area.pack(fill=tk.BOTH, expand=True)
        self.welcome_bill()

        # ======== Bill Menu Frame =========
        bill_menu_frame = tk.LabelFrame(
            self.root, text="Bill Menu", font=("Arial", 12, "bold"),
            fg=label_fg_color, bg=frame_bg_color, relief=tk.GROOVE, bd=10
        )
        bill_menu_frame.pack(fill=tk.X, padx=10, pady=5)
        self.create_bill_menu_widgets(bill_menu_frame, label_fg_color, entry_bg_color, button_bg_color)

    def create_customer_widgets(self, parent_frame, fg_color, entry_bg, btn_bg):
        tk.Label(parent_frame, text="Name", font=("Arial", 12), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=0, padx=20, pady=5, sticky="w")
        tk.Entry(parent_frame, width=20, textvariable=self.customer_name, font="arial 12", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=1, padx=10, pady=5)
        tk.Label(parent_frame, text="Phone Number", font=("Arial", 12), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=2, padx=20, pady=5, sticky="w")
        tk.Entry(parent_frame, width=20, textvariable=self.customer_phone, font="arial 12", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=3, padx=10, pady=5)
        tk.Label(parent_frame, text="Bill Number", font=("Arial", 12), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=4, padx=20, pady=5, sticky="w")
        tk.Entry(parent_frame, width=20, textvariable=self.bill_number, font="arial 12", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=5, padx=10, pady=5)
        tk.Button(parent_frame, text="SEARCH", width=10, bd=7, font="arial 12 bold", bg=btn_bg, fg="white", command=self.find_bill).grid(row=0, column=6, padx=10, pady=10)

    def create_product_frame(self, parent_container, text, fg_color, bg_color):
        return tk.LabelFrame(parent_container, text=text, font=("Arial", 12, "bold"), fg=fg_color, bg=bg_color, relief=tk.GROOVE, bd=10)

    def populate_product_widgets(self, parent_frame, items, fg_color, entry_bg):
        for i, (item, var) in enumerate(items.items()):
            tk.Label(parent_frame, text=item, font=("Arial", 12), bg=parent_frame['bg'], fg=fg_color).grid(row=i, column=0, padx=10, pady=10, sticky="w")
            tk.Entry(parent_frame, width=10, textvariable=var, font="arial 12", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=i, column=1, padx=10, pady=10)
    
    def create_bill_menu_widgets(self, parent_frame, fg_color, entry_bg, btn_bg):
        tk.Label(parent_frame, text="Cosmetic Price", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=0, padx=10, pady=2, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.cosmetic_price, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=1, padx=5, pady=2)
        tk.Label(parent_frame, text="Grocery Price", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=1, column=0, padx=10, pady=2, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.grocery_price, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=1, column=1, padx=5, pady=2)
        tk.Label(parent_frame, text="Cold Drink Price", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=2, column=0, padx=10, pady=2, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.cold_drink_price, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=2, column=1, padx=5, pady=2)

        tk.Label(parent_frame, text="Cosmetic Tax", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=2, padx=10, pady=2, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.cosmetic_tax, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=3, padx=5, pady=2)
        tk.Label(parent_frame, text="Grocery Tax", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=1, column=2, padx=10, pady=2, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.grocery_tax, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=1, column=3, padx=5, pady=2)
        tk.Label(parent_frame, text="Cold Drink Tax", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=2, column=2, padx=10, pady=2, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.cold_drink_tax, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=2, column=3, padx=5, pady=2)
        
        button_frame = tk.Frame(parent_frame, relief=tk.GROOVE, bg=parent_frame['bg'])
        button_frame.grid(row=0, column=4, rowspan=3, padx=20, pady=5) 

        btn_config = {"bg": btn_bg, "fg": "white", "pady": 8, "width": 9, "bd": 5, "font": "arial 10 bold"}
        tk.Button(button_frame, text="Total", **btn_config, command=self.total).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Bill", **btn_config, command=self.generate_bill).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Email", **btn_config, command=self.send_email).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(button_frame, text="Print", **btn_config, command=self.print_bill).grid(row=0, column=3, padx=5, pady=5)
        tk.Button(button_frame, text="Clear", **btn_config, command=self.clear_data).grid(row=0, column=4, padx=5, pady=5)
        parent_frame.columnconfigure(4, weight=1)

    # ======== Functionality =========
    def total(self):
        # Calculate cosmetics total price and tax
        c_p = sum(var.get() * self.prices["cosmetics"][item] for item, var in self.cosmetic_vars.items())
        c_t = c_p * self.tax_rates["cosmetics"]
        self.cosmetic_price.set(f"Tk. {c_p:.2f}")
        self.cosmetic_tax.set(f"Tk. {c_t:.2f}")

        # Calculate grocery total price and tax
        g_p = sum(var.get() * self.prices["grocery"][item] for item, var in self.grocery_vars.items())
        g_t = g_p * self.tax_rates["grocery"]
        self.grocery_price.set(f"Tk. {g_p:.2f}")
        self.grocery_tax.set(f"Tk. {g_t:.2f}")

        # Calculate cold drinks total price and tax
        d_p = sum(var.get() * self.prices["cold_drinks"][item] for item, var in self.cold_drink_vars.items())
        d_t = d_p * self.tax_rates["cold_drinks"]
        self.cold_drink_price.set(f"Tk. {d_p:.2f}")
        self.cold_drink_tax.set(f"Tk. {d_t:.2f}")
        
        self.total_bill_amount = c_p + g_p + d_p + c_t + g_t + d_t
        
    def welcome_bill(self):
        self.bill_text_area.delete('1.0', tk.END)
        self.bill_text_area.insert(tk.END, "\t\tWelcome To Our Retail Store\n")
        self.bill_text_area.insert(tk.END, f"\n Bill Number : {self.bill_number.get()}")
        self.bill_text_area.insert(tk.END, f"\n Customer Name : {self.customer_name.get()}")
        self.bill_text_area.insert(tk.END, f"\n Phone Number : {self.customer_phone.get()}")
        self.bill_text_area.insert(tk.END, f"\n==============================================")
        self.bill_text_area.insert(tk.END, f"\n Products\t\tQTY\t\tPrice")
        self.bill_text_area.insert(tk.END, f"\n==============================================")

    def generate_bill(self):
        if self.customer_name.get() == "" or self.customer_phone.get() == "":
            messagebox.showerror("Error", "Customer details are required.")
            return
        
        self.total()
        self.welcome_bill()
        
        # Cosmetic items
        if any(var.get() != 0 for var in self.cosmetic_vars.values()):
            self.bill_text_area.insert(tk.END, "\n ---- Cosmetics ----\n")
            for item, var in self.cosmetic_vars.items():
                if var.get() != 0:
                    qty = var.get()
                    price = qty * self.prices['cosmetics'][item]
                    self.bill_text_area.insert(tk.END, f"\n {item}\t\t{qty}\t\tTk. {price:.2f}")
        
        # Grocery items
        if any(var.get() != 0 for var in self.grocery_vars.values()):
            self.bill_text_area.insert(tk.END, "\n ---- Grocery ----\n")
            for item, var in self.grocery_vars.items():
                if var.get() != 0:
                    qty = var.get()
                    price = qty * self.prices['grocery'][item]
                    self.bill_text_area.insert(tk.END, f"\n {item}\t\t{qty}\t\tTk. {price:.2f}")
                    
        # Cold Drink items
        if any(var.get() != 0 for var in self.cold_drink_vars.values()):
            self.bill_text_area.insert(tk.END, "\n ---- Cold Drinks ----\n")
            for item, var in self.cold_drink_vars.items():
                if var.get() != 0:
                    qty = var.get()
                    price = qty * self.prices['cold_drinks'][item]
                    self.bill_text_area.insert(tk.END, f"\n {item}\t\t{qty}\t\tTk. {price:.2f}")
        
        self.bill_text_area.insert(tk.END, f"\n----------------------------------------------")
        if self.cosmetic_tax.get() != "Tk. 0.00":
             self.bill_text_area.insert(tk.END, f"\n Cosmetic Tax:\t\t\t{self.cosmetic_tax.get()}")
        if self.grocery_tax.get() != "Tk. 0.00":
             self.bill_text_area.insert(tk.END, f"\n Grocery Tax:\t\t\t{self.grocery_tax.get()}")
        if self.cold_drink_tax.get() != "Tk. 0.00":
             self.bill_text_area.insert(tk.END, f"\n Cold Drink Tax:\t\t\t{self.cold_drink_tax.get()}")
        
        self.bill_text_area.insert(tk.END, f"\n----------------------------------------------")
        self.bill_text_area.insert(tk.END, f"\n Total Bill:\t\t\tTk. {self.total_bill_amount:.2f}")
        self.bill_text_area.insert(tk.END, f"\n----------------------------------------------")
        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.bill_text_area.get('1.0', tk.END)
            if not os.path.exists("bills"):
                os.makedirs("bills")
            with open(f"bills/{self.bill_number.get()}.txt", "w") as f:
                f.write(self.bill_data)
            messagebox.showinfo("Saved", f"Bill No. : {self.bill_number.get()} saved successfully.")
        else:
            return
            
    def send_email(self):
        messagebox.showinfo("Email", "Email functionality is not implemented yet.")

    def print_bill(self):
        q = self.bill_text_area.get('1.0', 'end-1c')
        filename = f"bills/print_{self.bill_number.get()}.txt"
        with open(filename, "w") as f:
            f.write(q)
        try:
            os.startfile(filename, "print")
        except AttributeError: # For macOS/Linux
            # You may need to install 'lpr'
            os.system(f"lpr {filename}")
        except Exception as e:
            messagebox.showerror("Printing Error", f"Could not print bill: {e}")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear all data?")
        if op > 0:
            for var in list(self.cosmetic_vars.values()) + list(self.grocery_vars.values()) + list(self.cold_drink_vars.values()):
                var.set(0)
            
            for var in [self.cosmetic_price, self.grocery_price, self.cold_drink_price, self.cosmetic_tax, self.grocery_tax, self.cold_drink_tax]:
                var.set("")
            
            self.customer_name.set("")
            self.customer_phone.set("")
            x = random.randint(1000, 9999)
            self.bill_number.set(str(x))
            
            self.welcome_bill()

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.bill_number.get():
                with open(f"bills/{i}", "r") as f:
                    self.bill_text_area.delete('1.0', tk.END)
                    for d in f:
                        self.bill_text_area.insert(tk.END, d)
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

if __name__ == "__main__":
    if not os.path.exists("bills"):
        os.makedirs("bills")
    root = tk.Tk()
    app = RetailBillingSystem(root)
    root.mainloop()

