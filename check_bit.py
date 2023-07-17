def CheckBit(number,bit_position):
    if(number&(1<<bit_position)==0):
        print("0")
    else:
        print("1")
        
number=int(input("Enter the number: "))
bit_position=int(input("enter the bit position to be checked: "))
print(CheckBit(number,bit_position))
