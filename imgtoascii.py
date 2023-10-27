from PIL import Image
from tkinter import filedialog
from secrets import token_hex
from math import floor

DENSITY ="Ñ@&#W$9876543210?K!bac;:+=-,. "
file = filedialog.askopenfilename(title="Choose a file to convert to ASCII")
out = ''
if file == "":
    quit() 
im = Image.open(file)
pix = im.load()
for j in range(im.size[1]): 
    for i in range(im.size[0]): 
        col = pix[i,j] 
        col = round((col[0] + col[1] + col[2])/3) 
        im.putpixel((i,j),(col,col,col)) 
        out += f"{DENSITY[-floor(col/8.5)]} " 
    out +='\n' 

saveas = filedialog.asksaveasfile(defaultextension=("Text Document","*.txt"), filetypes=[("All Files","*.*")],initialfile=f"{token_hex(8)}.txt") 
outfile = open(saveas,"w") 
outfile.write(out) 
outfile.write(
    " _______    _______    _______   ___    __    ___  ______  ___    __    ___   ______\n"
    "/   _   \  /   _   \  /  _____\  \  \  /  \  /  / | _____| \  \  /  \  /  /  | _____|\n"
    "|  | |  |  |  | |  |  |  |  ____  \  \/    \/  /  | |__     \  \/    \/  /   | |__\n"
    "|  |_|  |  |  |_|  |  |  | _|  |   \    /\    /   |  __|_    \    /\    /    | ___|_\n"
    "\_______/  \_______/  \________/    \__/  \__/    |______|    \__/  \__/     |______|"
    ) 
outfile.close() 