import requests

for i in range(1,100):
    print(i)
    myurl= f'http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/profile?id={i}'
    r=requests.get(url=myurl)

    if r.status_code == 200:
        print(myurl)