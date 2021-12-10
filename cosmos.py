from tkinter import *
import urllib
import json
import sys

def on_key_pressing(event, entry, label):
    ean = entry.get()
    init(ean)
    
    
def forget(widget):
    widget.forget()

    
class PrintToT1(object):
    def write(self, s):
        t1.insert(END, s)
        t1.tag_add("center", "1.0", "end")
        
        
root = Tk()
root.geometry('1220x500')
root.minsize(1220, 500)
root.config(bg='pink')
root.title("API COSMOS")
# root.attributes('-fullscreen', True)
root.resizable(True, True)
entry = Entry(root)
entry.pack(side="top")
entry.bind("<Return>", lambda e: on_key_pressing(e, entry, root))
t1 = Text(root, bg='black', fg='white')
t1.tag_configure("center", justify='center')
t1.config(font=("Courier", 40))
t1.pack(expand=True, fill='both')
sys.stdout = PrintToT1()
    
def init(ean):
    if ean:
        headers = {'X-Cosmos-Token':'e4VaSr-smzGgmxO6zm3X_A','Content-Type':'application/json','User-Agent':'Cosmos-API-Request'}
        req      = urllib.request.Request(f'https://api.cosmos.bluesoft.com.br/gtins/{ean.strip()}.json', None, headers)
        response = urllib.request.urlopen(req)
        data     = json.loads(response.read())
        print(f"Nome: {data['description']}")
        print(f"Ean: {data['gtin']}")
        print(f"Preço: {data['price']}\n Preço médio: R$ {data['avg_price']:.2f}")
        print(f"Quantidade da caixa: {data['gtins'][0]['commercial_unit']['quantity_packaging']}")
        

root.mainloop()
