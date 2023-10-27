from PIL import Image
from tkinter import filedialog
from secrets import token_hex
from math import floor

DENSITY ="Ñ@&#W$9876543210?K!bac;:+=-,. "
file = filedialog.askopenfilename(title="Choose a file to convert to ASCII") #opens the image
out = ''
if file == "":
    quit() #quits if no file is chosen
im = Image.open(file)
pix = im.load()
for j in range(im.size[1]): #scans thru pixels by y-value
    for i in range(im.size[0]): #scans thru pixels by x-value
        col = pix[i,j] #pix[i,j] is a tuple containing the (r,g,b) values of the pixel at coordinate (i,j)
        col = round((col[0] + col[1] + col[2])/3) #sets col to grayscale using the rounded mean (average) of the rgb values
        im.putpixel((i,j),(col,col,col)) #replaces the pixel i,j with the grayscale version
        out += f"{DENSITY[-floor(col/8.5)]} " #divide by 8.5 because 255/8.5 == 30, which is the length of DENSITY.
    out +='\n' #newline when at the end of the pixel row

saveas = filedialog.asksaveasfile(defaultextension=("Text Document","*.txt"), filetypes=[("All Files","*.*")],initialfile=f"{token_hex(8)}.txt") #token_hex generates a random hex token of length 8
outfile = open(saveas,"w") #opens saveas in "w" mode (writing mode)
outfile.write(out) #writes the ascii converted
outfile.write(
    " _______    _______    _______   ___    __    ___  ______  ___    __    ___   ______\n"
    "/   _   \  /   _   \  /  _____\  \  \  /  \  /  / | _____| \  \  /  \  /  /  | _____|\n"
    "|  | |  |  |  | |  |  |  |  ____  \  \/    \/  /  | |__     \  \/    \/  /   | |__\n"
    "|  |_|  |  |  |_|  |  |  | _|  |   \    /\    /   |  __|_    \    /\    /    | ___|_\n"
    "\_______/  \_______/  \________/    \__/  \__/    |______|    \__/  \__/     |______|"
    ) #writes my signature
outfile.close() #closes file