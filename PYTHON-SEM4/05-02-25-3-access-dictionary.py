dict = {
    "class": {
        "student": {
            "name": "mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

history_marks = dict["class"]["student"]["marks"]["history"]
print("History marks:", history_marks)
