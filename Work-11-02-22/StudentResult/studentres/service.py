import csv
from studentres import utils, models


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
            new_student.status = "Failed"
            return utils.insert_marks(new_student, db)


def service_retrive(db):
    return utils.database_retrive(db)

def service_retrive_one(id,db):
    return utils.database_retrive_one(id,db)

def service_delete(id,db):
    return utils.database_delete(id,db)

def service_update(update_student,id,db):
    markdicts1 = {}

    markdicts1.update({'Maths': update_student.Maths})
    markdicts1.update({'History': update_student.History})
    markdicts1.update({'English': update_student.English})
    markdicts1.update({'Geography': update_student.Geography})
    markdicts1.update({'Civics': update_student.Civics})
    markdicts1.update({'Economics': update_student.Economics})
    marks1 = markdicts1.values()

    total_per = sum(marks1) / 6

    if total_per < 75.0:
        update_student.status = "Failed"
    else:
        update_student.status = "Passed"

    return utils.database_update(update_student,id,db)

def service_read_all_csv():
    filename = "C:\\Users\\Admin\\Desktop\\Studentdata.csv"
    outer = []
    rows = []
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    for row in rows[:5]:
        i = 0
        dict1 = {}
        # parsing each column of a row
        for col in row:
            dict1[fields[i]] = col
            i += 1
        outer.append(dict1)
    return outer

def service_read_id_csv(id):
    filename = "C:\\Users\\Admin\\Desktop\\Studentdata.csv"
    outer = []
    rows = []
    flag = False
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    for row in rows[:5]:
        i = 0
        dict1 = {}
        # parsing each column of a row
        for col in row:
            dict1[fields[i]] = col
            i += 1
        for key in dict1.keys():
            if key == "sid":
                if dict1.get(key) == id:
                    flag = True
                    outer.append(dict1)
    if flag == True:
        return outer

def service_insert_record(rows,db):
    for element in rows:
        if not rows.index(element) == 0:
            new_student = models.Student_model(sname=element[0], Maths=float(element[1]), History=float(element[2]),
                                               Geography=float(element[3]), English=float(element[4]),
                                               Civics=float(element[5]), Economics=float(element[6]))
            markdicts1 = {}

            markdicts1.update({'Maths': new_student.Maths})
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
                    db.add(new_student)
                    db.commit()
                    db.refresh(new_student)
                else:
                    # return {"Distinction":total_per}
                    new_student.status = "Distinction"
                    new_student.chance_given = "No"
                    db.add(new_student)
                    db.commit()
                    db.refresh(new_student)

            if 75.0 <= total_per < 90.0:
                # return {"Average":total_per}
                new_student.status = "Average"
                new_student.chance_given = "No"
                db.add(new_student)
                db.commit()
                db.refresh(new_student)

            if total_per < 75.0:
                if count2 > 3:
                    new_student.status = "Failed"
                    new_student.chance_given = "No"
                    db.add(new_student)
                    db.commit()
                    db.refresh(new_student)
                else:
                    new_student.chance_given = "Yes"
                    new_student.status = "Failed"
                    db.add(new_student)
                    db.commit()
                    db.refresh(new_student)


    return "CSV Data insert success"
