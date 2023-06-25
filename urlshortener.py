import tkinter as tk
import pyshorteners

def shortened():
    shorten = pyshorteners.Shortener()
    s_url = shorten.tinyurl.short(lurl_entry.get())
    print(surl_entry.insert(0,s_url))
    
    
    
root = tk.Tk()
root.title("URL_SHORTENER")
root.geometry("300x150")

lurl_label = tk.Label(root, text ="Enter the Long URL")
lurl_entry = tk.Entry(root)
surl_label = tk.Label(root, text ="Display the Shortened URL")
surl_entry = tk.Entry(root)
s_button = tk.Button(root, text = "Shorten the URL",command=shortened)

lurl_label.pack()
lurl_entry.pack()
surl_label.pack()
surl_entry.pack()
s_button.pack()

root.mainloop()