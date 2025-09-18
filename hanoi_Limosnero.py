#hanoi_Limosnero

print("This is the Tower of Hanoi")

def hanoi(n, a, b, c):
    if n == 1:
     print(f"Move disk 1 from {a} to {c}")
    return

    hanoi(n-1, a, c, b)
    print(f"Move disk {n} from {a} to {c}")

    hanoi(n-1, b, a, c)
    print(f"Move disk {n} from {b} to {c}")

#MAIN PROG
while True:
    try:
        num_disk = int(input("\nEnter  the number of disks: "))
        if num_disk <= 0:
            print("\nPlease enter a positive integer only!")
            continue
        print(
            f"The moves involved in the Tower of Hanoi with {num_disk} are:")
        hanoi(num_disk, 'A','B', 'C')
        print(f"\nTotal moves: {2**num_disk - 1}")

    except ValueError:
        print("n\Invalid input! Enter a positive  integer.")

