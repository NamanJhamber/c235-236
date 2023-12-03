# import requests

# for i in range(1 , 100):
#     x = f"http://ec2-3-6-91-214.ap-south-1.compute.amazonaws.com/profile?id={i}"
#     r = requests.get(url = x)
#     if r.status_code==200:
#         print(x)



import requests

for i in range(1, 5000):
    URL = "http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id=1"
    r = requests.get(url=URL)
    if r.status_code == 200:
        print(URL)




# 

