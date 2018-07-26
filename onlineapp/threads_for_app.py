import threading
import requests
from requests import request


def get_college_details(clg_id):

    url = "http://127.0.0.1:8000/api/colleges/"+str(clg_id)+"/"

    data = request('get',url).json()

    print(data)


#get_student_details()
for i in range(221,251):
    thread = threading.Thread(target=get_college_details, args=(i,))
    thread.start()
    #thread.join()