# Make sure to source the environment if on mac
## source ./request_env/bin/activate
import requests

request = requests.get('http://api.github.com/events')
user_request = requests.get('https://api.github.com/users/macwilly')
print(user_request.text)

with open('test.txt', 'w') as f:
    f.write(user_request.text)
    f.close()