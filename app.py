

from sunlite.db import connect
db = connect("myDB2")
db.new("books")
db.new('students')


db.push("art0fwar" , 'prince',target='books')
db.push("war" , 'prince')
db.push("happy" , 'prince')



print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(db.pull("war"))
print(db.pull("prince"))
print(db.get("books"))
print(db.get("students"))