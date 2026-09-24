# Autograded task 1 

# Open text file with read operator
with open("DOB.txt", "r+") as file: 
    lines = file.readlines()
    print("Name")
    for line in lines: 
        names = line.split(" ")[0:2]
        joined_name = (",".join(names)).replace(",", " ")
        print(joined_name)

    print("\nBirthdate")
    for line in lines: 
        unstripped_dob = line.split(" ")[2:]
        joined_dobs = (",".join(unstripped_dob)).replace(",", " ").strip()
        print(joined_dobs)
