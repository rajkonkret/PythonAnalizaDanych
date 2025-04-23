ceny = [123, 456, 789]

# context manager
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("plik.txt", "w") as file:
    file.write(str(ceny))

with open("plik.txt", "a") as f:
    f.write(str(ceny))

with open("plik.txt", "r") as file:
    zawartosc = file.read()

print(zawartosc)  # [123, 456, 789][123, 456, 789]
print(type(zawartosc))  # <class 'str'>
