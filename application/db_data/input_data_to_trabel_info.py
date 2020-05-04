# from application import db
from application import create_app
from application.models.travel_info import TravelInfo

data = open('C:\\Users\\khtks\\OneDrive\\Desktop\\data.txt', 'r', -1, 'utf-8')
data2 = open('C:\\Users\\khtks\\OneDrive\\Desktop\\data2.txt', 'r', -1, 'utf-8')

app = create_app()

while True:
    array1 = []
    array2 = []

    for i in range(5):
        line = data.readline()
        line = line.rstrip("\n")
        array1.append(line)

    for i in range(6):
        line = data2.readline()
        line = line.rstrip("\n")
        array2.append(line)

    print(array1)
    print(array2)
    print()

    print(array1)
    print(array2)
    print()

    if array1[0] == '' and array2[0] == '':
        break

    with app.app_context():
        from application import db
        travel_info = TravelInfo(contentID=array1[1], title=array2[2], addr=array2[3], phone_number=array2[4], img=array1[2], overview=array1[3])
        db.session.add(travel_info)
        db.session.commit()