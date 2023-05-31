import math


def main():
    print("Enter the value of modulo (q) :")
    q = int(input())
    print("Enter the primituve of  ",q," : ")
    p = int(input())

    print("Enter the private key of Alice (person1) : ")
    a = int(input())

    print("Enter the private key of Bob (person 2) : ")
    b = int(input())

    # Calculating their public key

    Y_A = (p ** a) % q  # public key of alice
    Y_B = (p ** b) % q # public key of bob


    # Calculating secret key of alice and bob

    K_A = (Y_B ** a) % q
    K_B = (Y_A ** b) % q

    print("The secret key of Alice :",K_A)
    print("The secret key of Bob :",K_B)

    if K_A == K_B:
        print("Alice and Bob can communicate")
        print("They share secret number : ",K_B)

    else:
        print("They cannot communicate")

if __name__ == "__main__":
    main()


