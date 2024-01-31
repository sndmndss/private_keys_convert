from eth_keys import keys
from eth_utils import decode_hex
from bs4 import BeautifulSoup


def private_key_to_address(private_key):
    private_key_bytes = decode_hex(private_key)
    account = keys.PrivateKey(private_key_bytes)
    address = account.public_key.to_checksum_address()
    return address


def html_to_addresses():
    private_keys = []
    with open('List1.html', 'r') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    div_content = soup.findall('div', class_='softmerge-inner')
    for element in div_content:
        element = element.get_text()
        if element.split(";")[-1][:2] == "0x":
            private_keys.append(element.split(";")[-1])
    return private_keys


if __name__ == "__main__":
    private_keys = html_to_addresses()
    while True:
        print("\n1: HTML accounts table to addresses\n2: private keys txt\n")
        choice = input()
        if choice == "1":
            file_name = "addresses.txt"
            with open(file_name, 'a') as file:
                for key in private_keys:
                    try:
                        address = private_key_to_address(key)
                        file.write(address + '\n')
                    except Exception as e:
                        print("Error:", e)
        elif choice == "2":
            file_name = "private_keys.txt"
            with open(file_name, 'a') as file:
                for key in private_keys:
                    try:
                        file.write(key + '\n')
                    except Exception as e:
                        print("Error:", e)
        else:
            raise "Wrong choice"
