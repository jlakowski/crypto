import urllib, json
import numpy as np
import matplotlib.pyplot as plt
n = 660 # 660 hours or 27 days of data

#TODO create a method or a few lines that build up the api call from scratch
#so you can choose the asset / time period / limit etc

url = "https://min-api.cryptocompare.com/data/histohour?fsym=LTC&tsym=USD&limit=660&aggregate=1&e=CCCAGG"

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

sigma = np.zeros(n/24 *3)
mean = np.zeros(n/24 *3)
cov = np.zeros(n/24 *3)
ts = np.zeros(n/24 *3)
uprdown = []
covup = np.zeros(n/24 *3)
covdn = np.zeros(n/24 *3)

for i in range(0, (n/24 *3)):
    #so we're taking data every hour which means that 8 hours is 1/3 of a day
    sigma[i] = np.std(closep[8*i:8*(i+1)])
    mean[i] =  np.mean(closep[8*i:8*(i+1)])
    cov[i] = sigma[i] / mean[i] *np.sqrt(0.333333)
    ts[i] = t[8*i]
    if closep[8*i] > closep[8*(i+1)]:
        uprdown.append('#FF0000') #there is a loss on the 8 hour time interval
        covup[i] = 0
        covdn[i] = cov[i]
    else:
        uprdown.append('#00FF00')
        covup[i] = cov[i]
        covdn[i] = 0



f, axarr = plt.subplots(2,sharex=True)
axarr[0].plot(t, closep)

axarr[1].hold(True)
#plt.scatter(ts, cov, c=uprdown)
markerlineu, stemlinesu, baselineu = axarr[1].stem(ts,covup, markerfmt=" ")
plt.setp(stemlinesu, 'color', 'g', 'linewidth', 4)
markerlined, stemlinesd, baselined = axarr[1].stem(ts,covdn, markerfmt=" ")
plt.setp(stemlinesd, 'color', 'r', 'linewidth', 4)


plt.show()
