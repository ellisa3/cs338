'''
    passwords.py
    Angela Ellis, 9 May 2022

    Password cracking for Brute-Force Password Cracking
    assignment in CS338.

'''

import hashlib
import binascii

hash_counter = 0

# writes to cracked_passwords.txt the username and the password in plaintext
# associated with that account
# user: 4:14
def part1():
    global hash_counter
    cracked_passwords = open("cracked1.txt", "w")
    accounts = [line.strip() for line in open("passwords1.txt", "r")]
    words = [line.strip().lower() for line in open('words.txt')]
    for word in words:
        digest = hash(word)
        hash_counter = hash_counter + 1
        for account in accounts:
            split_account = account.split(":")
            username = split_account[0]
            password = split_account[1]
            if digest == password:
                cracked_account = username + ":" + word
                cracked_passwords.write(cracked_account)
                cracked_passwords.write("\n")

    cracked_passwords.close()
    return

#2 hours for no output
def part2():
    users = {}
    global hash_counter
    cracked_passwords = open("cracked2.txt", "w")
    accounts = [line.strip() for line in open("passwords2.txt", "r")]
    words = [line.strip().lower() for line in open('words.txt')]
    for first_word in words:
        for second_word in words:
            concat_word = first_word + second_word
            digest = hash(concat_word)
            hash_counter = hash_counter + 1
            for account in accounts:
                split_account = account.split(":")
                username = split_account[0]
                password = split_account[1]
                users[password] = username
                result = users.get(digest)
                print(result)
            if result != None:
                cracked_account = result + ":" + concat_word + "\n"
                cracked_passwords.write(cracked_account)

    cracked_passwords.close()
    return

# 21:45
def part3():
    global hash_counter
    cracked_passwords = open("cracked3.txt", "w")
    accounts = [line.strip() for line in open("passwords3.txt", "r")]
    words = [line.strip().lower() for line in open('words.txt')]
    for word in words:
        for account in accounts:
            split_account = account.split(":")
            split_hash = split_account[1].split("$")
            salt = split_hash[2]
            password = split_hash[3]

            concat_salt_pw = salt + word
            digest = hash(concat_salt_pw)
            hash_counter = hash_counter + 1
            if digest == password:
                cracked_account = split_account[0] + ":" + word
                cracked_passwords.write(cracked_account)
                cracked_passwords.write("\n")

    cracked_passwords.close()
    return

# computes the digest of the input string and returns the digest
# as a hex string
def hash(word):
    encoded_password = word.encode('utf-8')
    hasher = hashlib.sha256(encoded_password)
    digest = hasher.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    return digest_as_hex_string

def main():
    #part1()
    #part2()
    #part3()
    print("hash counter: ", hash_counter)


if __name__=="__main__":
    main()
