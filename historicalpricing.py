import urllib, json
import numpy as np
import matplotlib.pyplot as plt
n = 60
url = "https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=60&aggregate=3&e=CCCAGG"

response = urllib.urlopen(url)
data = json.loads(response.read())
t = np.zeros(n)
closep =np.zeros(n)
openp = np.zeros(n)
lowp = np.zeros(n)
highp = np.zeros(n)

for i in range(0,n):
    t[i] = data['Data'][i]['time']
    closep[i] = data['Data'][i]['close']
    openp[i]  = data['Data'][i]['open']
    lowp[i]  = data['Data'][i]['low']
    highp[i] = data['Data'][i]['high']


plt.plot(t, openp)
plt.show()
