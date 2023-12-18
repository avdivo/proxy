import requests


data = open('cml.xml', 'rb').read()
url = "https://store.tilda.cc/connectors/commerceml/?type=catalog&mode=file&filename=import.xml"
headers = {
  'Host': 'store.tilda.cc',
  'User-Agent': '1C+Enterprise/8.2',
  'Authorization': 'Basic NzM2MjI3MjoyN2MwZDliNzNkNDViNjliYTgwZWJhOTI0M2I2YjI0OA==',
  'Cookie': 'PHPSESSID=tcenu5dgmt61ju5enupjfhkqjb',
  'Content-Type': 'application/xml',
  'Cache-Control': 'no-cache',
  'Accept': 'text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2'
}
response = requests.request("POST", url, headers=headers, data=data)
print(response.text)