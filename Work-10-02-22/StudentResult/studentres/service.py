from studentres import utils

# logic to update student status and chance given to student or not (business logic)
def service_insert(new_student,db):
    markdicts1 = {}

    markdicts1.update({'Maths':new_student.Maths })
    markdicts1.update({'History': new_student.History})
    markdicts1.update({'English': new_student.English})
    markdicts1.update({'Geography': new_student.Geography})
    markdicts1.update({'Civics': new_student.Civics})
    markdicts1.update({'Economics': new_student.Economics})
    marks1 = markdicts1.values()

    total_per = sum(marks1) / 6

    count1 = 0
    for i in marks1:
        if i >= 95.0:
            count1 = count1 + 1

    count2 = 0
    subname = []
    for i, j in markdicts1.items():
        if j <= 75.0:
            sname = i
            subname.append(sname)
            count2 = count2 + 1

    if total_per >= 90:
        if count1 >= 3:
            # return {"Gold medal and distinciton":total_per}
            new_student.status = "Gold medal and distinciton"
            new_student.chance_given = "No"
            return utils.insert_marks(new_student,db)
        else:
            # return {"Distinction":total_per}
            new_student.status = "Distinction"
            new_student.chance_given = "No"
            return utils.insert_marks(new_student, db)

    if 75.0 <= total_per < 90.0:
        # return {"Average":total_per}
        new_student.status = "Average"
        new_student.chance_given = "No"
        return utils.insert_marks(new_student, db)

    if total_per < 75.0:
        if count2 > 3:
            new_student.status = "Failed"
            new_student.chance_given = "No"
            return utils.insert_marks(new_student, db)
            #return {"Failed":total_per}
        else:
            new_student.chance_given = "Yes"
            new_student.status = "Passed"
            return utils.insert_marks(new_student, db)


def service_retrive(db):
    return utils.database_retrive(db)

def service_retrive_one(id,db):
    return utils.database_retrive_one(id,db)

def service_delete(id,db):
    return utils.database_delete(id,db)

