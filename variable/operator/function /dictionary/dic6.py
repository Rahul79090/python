student = {
    "name": "Rahul kumar",
    "subject": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

new_dict ={"city" : "new delhi", "age":-16}
new_dictes={"name" : "Rahul kumar" , "country" : "india"}

# student.update({"city" : "delhi"})
student.update(new_dict)
print(student)