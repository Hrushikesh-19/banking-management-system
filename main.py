print("=================================")
print("     BANKING MANAGEMENT SYSTEM")
print("=================================")

print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Check Balance")
print("5. Transaction History")
print("6. Exit")

choice = input("\nEnter your choice (1-6): ")

if choice == "1":
    print("Create Account Selected")
elif choice == "2":
    print("Deposit Money Selected")
elif choice == "3":
    print("Withdraw Money Selected")
elif choice == "4":
    print("Check Balance Selected")
elif choice == "5":
    print("Transaction History Selected")
elif choice == "6":
    print("Thank you for using Banking Management System!")
else:
    print("Invalid Choice")
