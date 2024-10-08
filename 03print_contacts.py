# Write a function called `print_contacts` that takes a
# dictionary of key-value pairs for names and phone numbers,
# then outputs the `name` with the contact info.
#
# Try iterating over a dictionary with a for loop and printing
# out what values come back.
#
# Example function call:
#
# print_contacts(contacts)
#
# > Brian has a phone number of 333-333-3333
# > Lenny has a phone number of 444-444-4444
# > Daniel has a phone number of 777-777-7777
#
# Use the contacts below



def print_contacts(contacts):
  for key in contacts:
    print(f"{key} has a phone number of {contacts[key]}")


def main():
  contacts = {
    'John': '555-1234',
    'Jane': '555-5678',
    'Doe': '555-8765'
  }
  print_contacts(contacts)


main()
