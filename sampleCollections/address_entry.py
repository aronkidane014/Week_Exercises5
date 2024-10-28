personal_info={
    "name": "Arne Slot",
    "address": "2040 west town",
    "city": "Chicago",
    "state": "Illinois",
    "Zip": "87654321"

}
print(personal_info)
del personal_info["name"]

personal_info = f"""\
{personal_info['name']}
{personal_info['address']}
{personal_info['city']}, {personal_info['state']}, {personal_info['Zip']}"""

print(personal_info)

del personal_info["name"]

personal_info = f"""\
{personal_info['address']}
{personal_info['city']}, {personal_info['state']}, {personal_info['Zip']}"""


print(personal_info)

personal_info = {
    "address": "2040 West Town",
    "city": "Chicago",
    "state": "Illinois",
    "zip": "87654321"
}
full_name = (("first name", "Arne"), ("last name", "Slot"))
personal_info.update(dict(full_name))
personal_info.update({"honorific": "Mr."})

formatted_address = f"""\
{personal_info['honorific']} {personal_info['first name']} {personal_info['last name']}
{personal_info['address']}
{personal_info['city']}, {personal_info['state']} {personal_info['zip']}"""

print(formatted_address)
