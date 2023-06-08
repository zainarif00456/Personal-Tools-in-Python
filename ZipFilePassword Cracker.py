import os
from tkinter import Tk
from tkinter import filedialog as fd
import zipfile

import rarfile

root = Tk()
root.withdraw()


def passwrodCracker(file, password):
    """
    Only for .ZIP Files
    :param file:
    :param password:
    :return:
    """
    try:
        file.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        return None


# def RaRExtractor(file, password):
#     try:
#         file.extractall(pwd=bytes(password, 'utf-8'))
#         return password
#     except:
#         return None


def execution():
    count = 0
    filename = fd.askopenfilename()
    file = zipfile.ZipFile(filename)
    with open('combinations.txt', 'r') as f:
        payload = f.readlines()
    for keywords in payload:
        passwd = keywords.strip('\n')
        print(f">>>>>>>>>> Testing with Keyword: {passwd}")
        correct_pass = passwrodCracker(file, passwd)
        count += 1
        if correct_pass:
            os.system('color 0a')
            print(f"Password Found >>>>>>>> [{correct_pass}]")
            print(f"Total Attempts >>>>>>>> [{count}]")
            os.system('pause')
            break


if __name__ == '__main__':
    os.system('color 0c')
    execution()

