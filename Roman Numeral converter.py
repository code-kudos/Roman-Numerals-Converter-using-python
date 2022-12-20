# Hi, I'm Code Kudos.
## Roman Numerals Converter using python
### Hope you like it!!!!
#### To see more like this Subscribe to 
##### Youtube: @codekudos
###### Instagram: @codekudos
####### Twitter: @code_kudos

def checkVal(val):
    try:
        val = int(val)
        return intToRoman(val)
    except ValueError:
        return romanToInt(val)

def romanToInt(val):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(val)):
        if i > 0 and rom_val[val[i]] > rom_val[val[i - 1]]:
            int_val += rom_val[val[i]] - 2 * rom_val[val[i - 1]]
        else:
            int_val += rom_val[val[i]]
    return int_val

def intToRoman(val):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    rom = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = len(rom)-1
    roman_val=""
      
    while val:
        div = val // num[i]
        val %= num[i]
        while div:
            roman_val+=rom[i]
            div -= 1
        i -= 1
    return roman_val

if __name__=="__main__":
    while(True):
        val = input("Enter the Value: ")
        if val=='0':
            break
        print(checkVal(val))