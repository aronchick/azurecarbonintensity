# azurecarbonintensity

Need to set application settings for:
    "watttime_USERNAME": YOUR_EMAIL,
    "watttime_PASSWORD": YOUR_PASSWORD

You will have to have registered with WattTime before you do so. Below is a function to do so:

```
def register(username, password, email, org):
    url = 'https://api2.watttime.org/register'
    params = {'username': username,
              'password': password,
              'email': email,
              'org': org}
    rsp = requests.post(url, json=params)
    print(rsp.text)
```