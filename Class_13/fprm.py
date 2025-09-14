import tkinter as tk
from tkinter import ttk, messagebox

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

        # ======== Variables =========
        # Customer Details
        self.customer_name = tk.StringVar()
        self.customer_phone = tk.StringVar()
        self.bill_number = tk.StringVar()
        # For searching, we can initialize bill_number
        self.bill_number.set("1001")

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


        # ======== Customer Details Frame =========
        customer_frame = tk.LabelFrame(
            self.root,
            text="Customer Details",
            font=("Arial", 12, "bold"),
            fg=label_fg_color,
            bg=frame_bg_color,
            relief=tk.GROOVE,
            bd=10
        )
        customer_frame.pack(fill=tk.X, padx=10, pady=5)

        self.create_customer_widgets(customer_frame, label_fg_color, entry_bg_color, button_bg_color)

        # ======== Products Frame (Container for Cosmetics, Grocery, Cold Drinks) =========
        products_container = tk.Frame(self.root, bg=bg_color)
        products_container.pack(fill=tk.BOTH, expand=True, padx=10)

        # ======== Cosmetics Frame ========
        cosmetics_frame = self.create_product_frame(products_container, "Cosmetics", label_fg_color, frame_bg_color, entry_bg_color)
        cosmetics_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        cosmetic_items = {
            "Bath Soap": self.bath_soap, "Face Cream": self.face_cream,
            "Face Wash": self.face_wash, "Hair Spray": self.hair_spray,
            "Hair Gel": self.hair_gel, "Body Lotion": self.body_lotion
        }
        self.populate_product_widgets(cosmetics_frame, cosmetic_items, label_fg_color, entry_bg_color)

        # ======== Grocery Frame ========
        grocery_frame = self.create_product_frame(products_container, "Grocery", label_fg_color, frame_bg_color, entry_bg_color)
        grocery_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        grocery_items = {
            "Rice": self.rice, "Oil": self.oil, "Daal": self.daal,
            "Wheat": self.wheat, "Sugar": self.sugar, "Tea": self.tea
        }
        self.populate_product_widgets(grocery_frame, grocery_items, label_fg_color, entry_bg_color)


        # ======== Cold Drinks Frame ========
        cold_drinks_frame = self.create_product_frame(products_container, "Cold Drinks", label_fg_color, frame_bg_color, entry_bg_color)
        cold_drinks_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        cold_drink_items = {
            "Water": self.water, "Cake": self.cake, "Chocolate": self.chocolate,
            "Apple": self.apple, "Lemon": self.lemon, "Pizza": self.pizza
        }
        self.populate_product_widgets(cold_drinks_frame, cold_drink_items, label_fg_color, entry_bg_color)

        # ======== Bill Area ========
        bill_area_frame = tk.LabelFrame(
            products_container,
            text="Bill Area",
            font=("Arial", 12, "bold"),
            fg=label_fg_color,
            bg="white",
            relief=tk.GROOVE,
            bd=10
        )
        bill_area_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        yscroll = tk.Scrollbar(bill_area_frame, orient=tk.VERTICAL)
        self.bill_text_area = tk.Text(bill_area_frame, yscrollcommand=yscroll.set)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        yscroll.config(command=self.bill_text_area.yview)
        self.bill_text_area.pack(fill=tk.BOTH, expand=True)
        self.welcome_bill()


        # ======== Bill Menu Frame =========
        bill_menu_frame = tk.LabelFrame(
            self.root,
            text="Bill Menu",
            font=("Arial", 12, "bold"),
            fg=label_fg_color,
            bg=frame_bg_color,
            relief=tk.GROOVE,
            bd=10
        )
        bill_menu_frame.pack(fill=tk.X, padx=10, pady=5)
        self.create_bill_menu_widgets(bill_menu_frame, label_fg_color, entry_bg_color, button_bg_color)

    def create_customer_widgets(self, parent_frame, fg_color, entry_bg, btn_bg):
        # Name
        tk.Label(parent_frame, text="Name", font=("Arial", 12), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=0, padx=20, pady=5, sticky="w")
        tk.Entry(parent_frame, width=20, textvariable=self.customer_name, font="arial 12", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=1, padx=10, pady=5)
        # Phone Number
        tk.Label(parent_frame, text="Phone Number", font=("Arial", 12), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=2, padx=20, pady=5, sticky="w")
        tk.Entry(parent_frame, width=20, textvariable=self.customer_phone, font="arial 12", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=3, padx=10, pady=5)
        # Bill Number
        tk.Label(parent_frame, text="Bill Number", font=("Arial", 12), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=4, padx=20, pady=5, sticky="w")
        tk.Entry(parent_frame, width=20, textvariable=self.bill_number, font="arial 12", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=5, padx=10, pady=5)
        # Search Button
        tk.Button(parent_frame, text="SEARCH", width=10, bd=7, font="arial 12 bold", bg=btn_bg, fg="white", command=self.find_bill).grid(row=0, column=6, padx=10, pady=10)

    def create_product_frame(self, parent_container, text, fg_color, bg_color, entry_bg):
        frame = tk.LabelFrame(
            parent_container,
            text=text,
            font=("Arial", 12, "bold"),
            fg=fg_color,
            bg=bg_color,
            relief=tk.GROOVE,
            bd=10
        )
        return frame

    def populate_product_widgets(self, parent_frame, items, fg_color, entry_bg):
        row_num = 0
        for item, var in items.items():
            tk.Label(parent_frame, text=item, font=("Arial", 12), bg=parent_frame['bg'], fg=fg_color).grid(row=row_num, column=0, padx=10, pady=10, sticky="w")
            tk.Entry(parent_frame, width=10, textvariable=var, font="arial 12", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=row_num, column=1, padx=10, pady=10)
            row_num += 1
    
    def create_bill_menu_widgets(self, parent_frame, fg_color, entry_bg, btn_bg):
        # Prices
        tk.Label(parent_frame, text="Cosmetic Price", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.cosmetic_price, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(parent_frame, text="Grocery Price", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.grocery_price, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(parent_frame, text="Cold Drink Price", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.cold_drink_price, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=2, column=1, padx=5, pady=5)

        # Taxes
        tk.Label(parent_frame, text="Cosmetic Tax", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=0, column=2, padx=10, pady=5, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.cosmetic_tax, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(parent_frame, text="Grocery Tax", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=1, column=2, padx=10, pady=5, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.grocery_tax, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=1, column=3, padx=5, pady=5)

        tk.Label(parent_frame, text="Cold Drink Tax", font=("Arial", 11), bg=parent_frame['bg'], fg=fg_color).grid(row=2, column=2, padx=10, pady=5, sticky="w")
        tk.Entry(parent_frame, width=15, textvariable=self.cold_drink_tax, font="arial 11", bd=5, relief=tk.SUNKEN, bg=entry_bg).grid(row=2, column=3, padx=5, pady=5)

        # Buttons
        button_frame = tk.Frame(parent_frame, bd=7, relief=tk.GROOVE, bg="#2E8B57")
        button_frame.grid(row=0, column=4, rowspan=3, padx=20, pady=5)

        tk.Button(button_frame, text="Total", bg=btn_bg, fg="white", pady=15, width=10, bd=5, font="arial 12 bold", command=self.total).pack(pady=5)
        tk.Button(button_frame, text="Bill", bg=btn_bg, fg="white", pady=15, width=10, bd=5, font="arial 12 bold", command=self.generate_bill).pack(pady=5)
        tk.Button(button_frame, text="Email", bg=btn_bg, fg="white", pady=15, width=10, bd=5, font="arial 12 bold", command=self.send_email).pack(pady=5)
        tk.Button(button_frame, text="Print", bg=btn_bg, fg="white", pady=15, width=10, bd=5, font="arial 12 bold", command=self.print_bill).pack(pady=5)
        tk.Button(button_frame, text="Clear", bg=btn_bg, fg="white", pady=15, width=10, bd=5, font="arial 12 bold", command=self.clear_data).pack(pady=5)

    # ======== Functionality =========
    def welcome_bill(self):
        self.bill_text_area.delete('1.0', tk.END)
        self.bill_text_area.insert(tk.END, "\tWelcome To Retail Billing\n")
        self.bill_text_area.insert(tk.END, f"\n Bill Number : {self.bill_number.get()}")
        self.bill_text_area.insert(tk.END, f"\n Customer Name : {self.customer_name.get()}")
        self.bill_text_area.insert(tk.END, f"\n Phone Number : {self.customer_phone.get()}")
        self.bill_text_area.insert(tk.END, f"\n======================================")
        self.bill_text_area.insert(tk.END, f"\n Products\t\tQTY\t\tPrice")
        self.bill_text_area.insert(tk.END, f"\n======================================")

    def total(self):
        # Placeholder for total calculation logic
        print("Total button clicked")
        messagebox.showinfo("Action", "Calculating total...")

    def generate_bill(self):
        # Placeholder for bill generation logic
        print("Generate Bill button clicked")
        self.welcome_bill() # Re-populate with customer info
        # Add bill items here
        self.bill_text_area.insert(tk.END, f"\n\n--- Bill content goes here ---")
        messagebox.showinfo("Action", "Generating bill...")
        
    def send_email(self):
        # Placeholder for email functionality
        print("Email button clicked")
        messagebox.showinfo("Action", "Sending email...")

    def print_bill(self):
        # Placeholder for printing functionality
        print("Print button clicked")
        messagebox.showinfo("Action", "Printing bill...")

    def clear_data(self):
        # Placeholder for clearing all fields
        print("Clear button clicked")
        self.customer_name.set("")
        self.customer_phone.set("")
        # ... clear all other variables ...
        self.welcome_bill()
        messagebox.showinfo("Action", "All fields cleared.")

    def find_bill(self):
        # Placeholder for finding an existing bill
        print("Find Bill button clicked")
        messagebox.showinfo("Action", f"Searching for bill number: {self.bill_number.get()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RetailBillingSystem(root)
    root.mainloop()
