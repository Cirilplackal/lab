def update_probe():
    num = int(input("Enter a number: "))
    file_path = r"C:\Users\ciril\OneDrive\Desktop\probe.txt"  # Updated file path
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        new_line = '\nstop -create -time ' + str(num) + 'ns-absolute-execute "save mysnap_' + str(num) + 'n-overwrite" -continue\n'
        lines.append(new_line)
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print("Updated probe")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def update_probe_again():
    num = int(input("Enter the same number again: "))
    file_path = r"C:\Users\ciril\OneDrive\Desktop\probe.txt"  # Updated file path
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        new_line = '\n-r mySnap_'+ str(num)+'n'
        lines.append(new_line)
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print("Updated probe")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def update_xrunArgs():
    file_path = r"C:\Users\ciril\OneDrive\Desktop\xrunArgs.txt"  # Updated file path
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        new_line = '\n-process_save\n'
        lines.append(new_line)
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print("Updated xrunArgs")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def replace_string_in_tran():
    file_path = r"C:\Users\ciril\OneDrive\Desktop\editable.txt"  # Updated file path
    new_value = input("Enter the new stop time value (in ns): ")
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        found = False
        for i, line in enumerate(lines):
            if "tran tran stop=" in line:
                parts = line.split("tran tran stop=")
                if len(parts) > 1:
                    end_part = parts[1].split("n", 1)
                    if len(end_part) > 1:
                        lines[i] = parts[0] + "tran tran stop=" + new_value + "n" + end_part[1]
                        found = True
                        break
        
        if found:
            with open(file_path, 'w') as file:
                file.writelines(lines)
            print(f"Replaced stop time value with '{new_value}n' in the file.")
        else:
            print("Stop time value not found.")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def main():
    while True:
        print("Select an operation:")
        print("1. Update Probe")
        print("2. Update xrunArgs")
        print("3. Replace Stop Time in Tran")
        print("4. Update the probe again")
        print("0. Exit")

        choice = input("Enter your choice (0/1/2/3/4): ")
        if choice == '0':
            print("Exiting the program.")
            break

        if choice in ['1', '2', '3','4']:
            if choice == '1':
                update_probe()
            elif choice == '2':
                update_xrunArgs()
            elif choice == '3':
                replace_string_in_tran()
            elif choice == '4':
                update_probe_again()
        else:
            print("Invalid choice. Please enter a valid option.")

main()


