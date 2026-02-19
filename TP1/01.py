string = "Sítio do pica-pau amarelo \n 2023"

char_filter = [char for char in string if not
               char.isspace()]

print(char_filter)