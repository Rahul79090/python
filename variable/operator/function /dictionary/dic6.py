student = {
    "name": "Rahul kumar",
    "subject": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

new_dict ={"city" : "Rahul kumar", "age":-16}
# student.update({"city" : "delhi"})
student.update(new_dict)
print(student)