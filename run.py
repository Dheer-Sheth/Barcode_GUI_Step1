# import os
# import csv
import barcode
from barcode.writer import ImageWriter
# from sh import lp
from tkinter import *
import random

generatedBarcode=[]

def NumberGenerator():
    num1= "0123456789"
    num2= "0123456789"
    number= num1+num2
    length= 12
    result= "".join(random.sample(number, length))
    return result

   

def barcode_generate():
    product= ProductNameEntry.get()
    barcode_format= barcode.get_barcode_class('code128')
    barcodeNumber= NumberGenerator()
    generated= barcode_format(barcodeNumber, writer= ImageWriter())
    generated.save(product)
    generatedBarcode.append(f"{product}.png")


NumberGenerator()

Generator= Tk()

Generator.title ('Barcode Generator')
Generator.geometry('600x600')

ProductName= Label(Generator, text="Product Name", font= ('bold',10))
ProductName.place(x=150, y=50)

ProductNameEntry= Entry(Generator, width=20)
ProductNameEntry.place(x=250, y=50)

ISBN= Label(Generator, text="ISBN", font= ('bold',10))
ISBN.place(x=150, y=80)

ISBNEntry= Entry(Generator, width=20)
ISBNEntry.place(x=250, y=80)

Button(Generator, text="Generate", width=20, bg='white',command=barcode_generate, font=('bold',10)).place(x=200, y=130)
image= Label(Generator)
image.place(x=150, y=170)



while True:
    for img in generatedBarcode:
        img= PhotoImage(file=img)
        image['image']=img
        label1= Label(Generator, text="Image Saved!!", font=('bold',20)).place(x=250, y=550)
        

    Generator.update ()


# def create_code_png(isbn,title):
#     isbn13 = barcode.get_barcode_class('code128')
#     return isbn13(isbn, writer = ImageWriter())

# def remove_forbidden(string_in):
#     forbidden_chars = ":;<>\"\\/?*|."
#     return "".join([char for char in string_in if char not in forbidden_chars])

# def codes_from_csv(list_location,destination_folder):
#     with open(list_location, newline='') as csvfile:
#         os.chdir(destination_folder)
#         for row in csv.reader(csvfile, dialect='excel'):
#             code = create_code_png(isbn:=row[0],title:=remove_forbidden(row[1]))
#             code.save(isbn + " " + title)


# if __name__ == "__main__":
#     codes_from_csv("/Users/dheersheth/Desktop/Barcodes_TEST/data.csv","/Users/dheersheth/Desktop/Barcodes_TEST/Images")

# import os
# from os import listdir


# folder_dir = "/Users/dheersheth/Desktop/Barcodes_TEST/Images"
# for images in os.listdir(folder_dir):

#     if (images.endswith(".png")):
#         lp(images)
