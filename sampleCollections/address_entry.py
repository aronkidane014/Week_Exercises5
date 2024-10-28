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
