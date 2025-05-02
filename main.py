from mpin_functions import isCommon, isCommon2, isWeakByDemographics, isWeakByDemographics2, isWeakByDemographics3

def get_mpin(): #validate 4-digit mpins
    while True:
        mpin = input("Enter MPIN (4 digits): ").strip()
        if mpin.isdigit() and len(mpin) == 4:
            return mpin
        print("Invalid MPIN. Please enter a 4 digit MPIN.")

def get_mpin2(): #validate 6-digit mpins
    while True:
        mpin = input("Enter MPIN (4 or 6 digits): ").strip()
        if mpin.isdigit() and len(mpin) in (4, 6):
            return mpin
        print("Invalid MPIN. Please enter a 4 or 6 digit MPIN.")

def get_date(prompt): #validate dates
    while True:
        date_str = input(prompt).strip()
        if date_str.isdigit() and len(date_str) == 8:
            return date_str
        print("Invalid date. Please enter date in DDMMYYYY format.")


def part_a(): #for commonly used 4-digit mpins
    mpin = get_mpin()
    if isCommon(mpin):
        print("MPIN is commonly used")
    else:
        print("MPIN is not commonly used")

def part_b(): #for commonly used mpins and demographics
    dob = get_date("Enter your DOB (DDMMYYYY): ")
    spouse_dob = get_date("Enter spouse's DOB (DDMMYYYY): ")
    anniversary = get_date("Enter your anniversary date (DDMMYYYY): ")
    mpin = get_mpin()
    result = isWeakByDemographics(mpin, dob, spouse_dob, anniversary)
    if result or isCommon(mpin):
        print("WEAK")
    else:
        print("STRONG")

def part_c(): #reasons for weak or strong mpin-strength
    dob = get_date("Enter your DOB (DDMMYYYY): ")
    spouse_dob = get_date("Enter spouse's DOB (DDMMYYYY): ")
    anniversary = get_date("Enter your anniversary date (DDMMYYYY): ")
    mpin = get_mpin()
    reasons = []
    if isCommon(mpin):
        reasons.append("COMMONLY_USED")
    reasons.extend(isWeakByDemographics2(mpin, dob, spouse_dob, anniversary))
    if reasons:
        print("Strength: WEAK")
        print("Reasons:", reasons)
    else:
        print("Strength: STRONG")

def part_d(): #4 and 6-digit mpin checks
    dob = get_date("Enter your DOB (DDMMYYYY): ")
    spouse_dob = get_date("Enter spouse's DOB (DDMMYYYY): ")
    anniversary = get_date("Enter your anniversary date (DDMMYYYY): ")
    mpin = get_mpin2()
    reasons = []
    if isCommon2(mpin):
        reasons.append("COMMONLY_USED")
    reasons.extend(isWeakByDemographics3(mpin, dob, spouse_dob, anniversary))
    if reasons:
        print("Strength: WEAK")
        print("Reasons:", reasons)
    else:
        print("Strength: STRONG")

def main():
    while True: #menu for executing desired part
        print("\nSelect a part to run:")
        print("1. Part A - Commonly Used MPIN Check")
        print("2. Part B - Demographic + Common Check")
        print("3. Part C - Demographics + Common Check with Reasons")
        print("4. Part D - 4 or 6 Digit MPIN with All Checks and Reasons")
        print("5. Exit")
        choice = input("Enter your choice (1–5): ").strip()

        if choice == "1":
            part_a()
        elif choice == "2":
            part_b()
        elif choice == "3":
            part_c()
        elif choice == "4":
            part_d()
        elif choice == "5":
            print("Exiting Menu.")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")

if _name_ == "_main_":
    main()