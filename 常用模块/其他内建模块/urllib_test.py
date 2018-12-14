from urllib import request
with request.urlopen('https://www.multibankfx.com/resource/newwebsite/v1_0/images/about_us/why_multibank/why_multibank_image2@2x.png') as f:
    data = f.read()
    print('Status: ',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' %(k,v))
    #print('Data: ',data.decode('utf-8'))