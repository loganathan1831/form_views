from django import froms

#django froms
class StudentForm(froms.Form):
    name=froms.charField(max_length=100)
    age=froms.IntegerField()