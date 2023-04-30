import requests
import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter import PhotoImage
import os



class MyApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("1920x1080")
        self.master.title("Block Chain Tracker App")
        self.master.configure(bg="#f2f2f2")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.logo = tk.PhotoImage(file="blockchain1.png")
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.pack(side="top", pady=20)

        self.title_label = tk.Label(self, text="Block Chain Tracker App", font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#0c5e8a")
        self.title_label.pack(side="top")

        self.author_label = tk.Label(self, text="Author: SYED IBRAHIM", font=("Arial", 15), bg="#f2f2f2")
        self.author_label.pack(side="top", pady=(0, 10))

        self.project_label = tk.Label(self, text="Project: HCL Mini Project", font=("Arial", 15), bg="#f2f2f2")
        self.project_label.pack(side="top")

        self.description_label = tk.Label(self, text="Click Block Chain Button To Enter Block Chain Tracker App", font=("Arial", 12), bg="#f2f2f2", fg="#4d4d4d")
        self.description_label.pack(side="top", pady=(30, 10))



        self.quit_button = tk.Button(self, text="Block Chain", font=("Arial", 12), bg="#0c5e8a", fg="white", command=self.master.destroy)
        self.quit_button.pack(side="bottom", pady=(20, 0))
        

    def enter_blockchain(self):
        print("Entering Block Chain Tracker App...")

root = tk.Tk()
app = MyApplication(master=root)
app.mainloop()


# Assuming the image file is in the same directory as your script:
icon_path = os.path.join(os.path.dirname(__file__), 'blockchain.png')


def update_data():
    # Update number of transactions
    try:
        data = requests.get('https://api.blockchain.info/charts/n-transactions?format=json').json()
        entry_transactions.config(state='normal')
        entry_transactions.delete(0, tk.END)
        entry_transactions.insert(0, data['values'][-1]['y'])
        entry_transactions.config(state='readonly')
    except:
        print('Error fetching number of transactions')

    # Update number of blocks
    try:
        data = requests.get('https://api.blockchain.info/stats?format=json').json()
        entry_blocks.config(state='normal')
        entry_blocks.delete(0, tk.END)
        entry_blocks.insert(0, data['n_blocks_total'])
        entry_blocks.config(state='readonly')
    except:
        print('Error fetching number of blocks')

    # Update network hashrate
    try:
        data = requests.get('https://api.blockchain.info/charts/hash-rate?format=json').json()
        entry_hashrate.config(state='normal')
        entry_hashrate.delete(0, tk.END)
        entry_hashrate.insert(0, data['values'][-1]['y'])
        entry_hashrate.config(state='readonly')
    except:
        print('Error fetching network hashrate')

    # Update blockchain size data
    try:
        data = requests.get('https://blockchain.info/q/24hrtransactioncount').text
        entry_blocksize.config(state='normal')
        entry_blocksize.delete(0, tk.END)
        entry_blocksize.insert(0, data)
        entry_blocksize.config(state='readonly')
    except:
        print('Error fetching blockchain size data')

    # Update unique addresses
    try:
        data = requests.get('https://api.blockchain.info/charts/n-unique-addresses?format=json').json()
        entry_addresses.config(state='normal')
        entry_addresses.delete(0, tk.END)
        entry_addresses.insert(0, data['values'][-1]['y'])
        entry_addresses.config(state='readonly')
    except:
        print('Error fetching unique addresses')

    # Update current bitcoin price


    try:
        data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        price = f"${data['bpi']['USD']['rate']}"  # add $ symbol to price
        entry_price.config(state='normal')
        entry_price.delete(0, tk.END)
        entry_price.insert(0, price)
        entry_price.config(state='readonly')
    except:
        print('Error fetching current bitcoin price')

        
    # Schedule the next update after 15 seconds
    root.after(15000, update_data)        


def animate_button():
    update_button.config(bg='#F7931A')
    root.after(100, lambda: update_button.config(bg='#F9A03F'))


root = tk.Tk()
root.title('Blockchain Tracker')
root.geometry('1280x720')
root.configure(bg='#FFFFFF')

# Set the window icon
icon_path = 'blockchain.png'
icon = ImageTk.PhotoImage(Image.open(icon_path))
root.iconphoto(root._w, PhotoImage(file=icon_path))
#Create a custom font for the title
title_font = Font(family='Helvetica', size=24, weight='bold')

#Create a label for the title
title_label = tk.Label(root, text='Blockchain Tracker', font=title_font, bg='#FFFFFF')
title_label.pack(pady=20)

#Create a frame to hold the data entry widgets
data_frame = tk.Frame(root, bg='#FFFFFF')
data_frame.pack()

#Create labels for each data entry widget
transactions_label = tk.Label(data_frame, text='Number of Transactions:', bg='#FFFFFF')
blocks_label = tk.Label(data_frame, text='Number of Blocks:', bg='#FFFFFF')
hashrate_label = tk.Label(data_frame, text='Network Hashrate:', bg='#FFFFFF')
blocksize_label = tk.Label(data_frame, text='Blockchain Size:', bg='#FFFFFF')
addresses_label = tk.Label(data_frame, text='Unique Addresses:', bg='#FFFFFF')
price_label = tk.Label(data_frame, text='Current Bitcoin Price($):', bg='#FFFFFF')

#Pack the labels into the data frame
transactions_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
blocks_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
hashrate_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
blocksize_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
addresses_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
price_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')

#Create entry widgets for the data
entry_transactions = tk.Entry(data_frame, bg='#F9F9F9', relief='flat', justify='center', state='readonly')
entry_blocks = tk.Entry(data_frame, bg='#F9F9F9', relief='flat', justify='center', state='readonly')
entry_hashrate = tk.Entry(data_frame, bg='#F9F9F9', relief='flat', justify='center', state='readonly')
entry_blocksize = tk.Entry(data_frame, bg='#F9F9F9', relief='flat', justify='center', state='readonly')
entry_addresses = tk.Entry(data_frame, bg='#F9F9F9', relief='flat', justify='center', state='readonly')
entry_price = tk.Entry(data_frame, bg='#F9F9F9', relief='flat', justify='center', state='readonly')

#Pack the entry widgets into the data frame
entry_transactions.grid(row=0, column=1, padx=10, pady=10)
entry_blocks.grid(row=1, column=1, padx=10, pady=10)
entry_hashrate.grid(row=2, column=1, padx=10, pady=10)
entry_blocksize.grid(row=3, column=1, padx=10, pady=10)
entry_addresses.grid(row=4, column=1, padx=10, pady=10)
entry_price.grid(row=5, column=1, padx=10, pady=10)

#Create a button to manually update the data
update_button = tk.Button(root, text='Update', bg='#F9A03F', fg='#FFFFFF', relief='flat', command=animate_button)
update_button.pack(pady=20)

#Schedule the first update
root.after(0, update_data)

#Start the main loop
root.mainloop()




