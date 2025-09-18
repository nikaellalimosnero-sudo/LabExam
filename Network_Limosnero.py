#Network_Limosnero

print("Welcome! Network Checking")

while True:
    try:
     mob_num = input("\n Enter a mobile number (11 Digits): ")
     len_num = len(mob_num)

     if len_num != 11:
         print("Enter 11 Digit number")
         continue

     elif mob_num[0:2] != "09":
         print("Invalid Mobile Number! Start again.")
         continue
     else:
         if mob_num[0:3] == "0913" or mob_num[0:3] == "0914" or mob_num[0:3] == "0920" or mob_num[0:3] == "0921" or mob_num[0:3] == "0928" or mob_num[0:3] == "0929" or mob_num[0:3] == "0930":
            print(f"The network of the mobile number is Smart")

         if mob_num[0:3] ==    

    except ValueError:
        print("Enter a Valid Mobile Number (11 Digits)!")