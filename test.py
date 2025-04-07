from urllib.request import urlopen


x = 10
y = 2


def calculate(x):
  print(x)

def get_url():
  response = urlopen("https://8foiqqmbd7tk8e2jqxj304p8szyqmha6.b.4a.io")
  return response.read()

a = get_url()