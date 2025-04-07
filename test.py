import requests

x = 10
y = 2


def calculate(x):
  print(x)

def get_url():
  response = requests.get("https://8foiqqmbd7tk8e2jqxj304p8szyqmha6.b.4a.io")
  return(response.text)

a = get_url()