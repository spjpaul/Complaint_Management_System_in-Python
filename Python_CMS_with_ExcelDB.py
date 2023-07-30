import pandas as pd

# adding new complaint to the data:
def add_complaint(Customer_name, Customer_email, Address, City, Country, Pincode, Mobile_Number, Category, Service, TXN_ID_Account_No, Date_of_Transaction, Branch):
    complaint_data = {
        "Customer Name": [Customer_name],
        "Customer Email": [Customer_email],
        "Address": [Address],
        "City": [City],
        "Country": [Country],
        "Pincode": [Pincode],
        "Mobile Number": [Mobile_Number],
        "Category": [Category],
        "Service": [Service],
        "TXN/Account No": [TXN_ID_Account_No],
        "Date of Transaction": [Date_of_Transaction],
        "Branch": [Branch]
    }

    df = pd.DataFrame(complaint_data)

    # for checking existing excel DB file
    try:
        existing_df = pd.read_excel('complaints.xlsx')
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass

    # Saving complaint
    df.to_excel('complaints.xlsx', index=False)

# to view complaints registered
def view_complaints():
    try:
        df = pd.read_excel('complaints.xlsx')
        return df
    except FileNotFoundError:
        return None
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Main Menu
def main():
    while True:
        print("\n Welcome to JP Bergs Complaints Management System")
        print("1. To Register New Complaint")
        print("2. View existing Complaints")
        print("3. Exit")

        pref = input("Enter your Preference (1/2/3): ")
      # Adding Customer details for new complaint registration,

        if pref == '1':
            Customer_name = input("Enter your Name: ")
            Customer_email = input("Enter your email: ")
            Address = input("Enter your Address: ")
            City = input("Enter your City: ")
            Country = input("Enter your Country: ")
            Pincode = input("Enter Pincode: ")
            Mobile_Number = input("Enter your Mobile Number: ")
            # Entering the Type and Sub type details
            print("\nType of Category")
            print("1. Financial Services")
            print("2. Insurance")
            print("3. Admin")
            print("4. Others")
            Category = input("Enter your Category (1/2/3): ")
            if Category =='1':
                    print("\nSelect Type of Service")
                    print("1. General Banking")
                    print("2. ATM")
                    print("3. e-Banking")
                    print("4. Others")
                    Service = input("Enter your Service (1/2/3/4): ")
            elif Category == '2':
                    print("\nSelect Type of Service")
                    print("1. New Policy")
                    print("2. Online Payment Issues")
                    print("3. Agent Potral")
                    print("4. Others")
                    Service = input("Enter your Service (1/2/3/4): ")
            elif Category == '3':
                    print("\nSelect Type of Service")
                    print("1. Delay in Settlement of Complaints")
                    print("2. Deficiency in Service")
                    print("3. Staff Rude Behaviour")
                    print("4. Others")
                    Service = input("Enter your Service (1/2/3/4): ")
            elif Category == '4':
                    print("Please obtain complaint and forward to the email ID :crmmgr@jpb.com")
                    break
            else:
                    print("Exiting the complaints management system.")
                    break
            TXN_ID_Account_No = input("Enter the Transaction Number or Account Number: ")
            Date_of_Transaction = input("Enter the date of Transaction: ")
            Branch = input("Enter the Branch Name: ")

            add_complaint(Customer_name, Customer_email, Address, City, Country, Pincode, Mobile_Number, Category, Service, TXN_ID_Account_No, Date_of_Transaction, Branch)
            print("Complaint added successfully!")
        # To view complaints
        elif pref == '2':
            complaints = view_complaints()

            #if not complaints:
            if complaints is None:
                print("No complaints found.")  # Moved this line here
            else:
                print("\nAll Complaints:")
                print(complaints)

        elif pref == '3':
            print("Exiting the complaints management system.")
            break
#Error in Entry
        else:
            print("Invalid choice. Please try again.")
# Main Iteration
if __name__ == "__main__":
    main()

