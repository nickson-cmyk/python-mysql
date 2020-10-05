import requests

def signup():
    x=requests.post("http://localhost:5000/signup",json={"name":"nicj","lastname":"vin","sex":"male"})
    print(x.text)
    return x.text
def update():
    x1=requests.post("http://localhost:5000/update",json={"name":"nicj"})
    print(x1.text)
def delete():
    x2=requests.post("http://localhost:5000/delete")
    print(x2.text)
def get():
    x3=requests.get("http://localhost:5000/get")
    print(x3.text)
y=input("enter operation")

def operation(y):
   if y =="signup":

       res_x = signup()
   if y =="delete":
       res_x = delete()
   if y =="get":
       res_x = get()
#    elif y == "update":
#     return x1
# def operation(y):
   elif y =="update":
       res_x = update()
#    elif y == "update":
#     return x1
operation(y)