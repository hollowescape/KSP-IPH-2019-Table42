from Instagram.Instagram import *
from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
import bs4
import requests
app = Flask(__name__)
cors = CORS(app, resources={r"/home": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/home")
def home():
    
    a = request.args.get("name")
    
    m = ""
    for i in a.split(" "):
        m=m+"+"+i
    m = m[1:]
 
    link = "https://gramuser.com/search/"+m
    # print(link)
    url = link
    data = requests.get(url)

    soup = bs4.BeautifulSoup(data.text, 'html.parser')

    # print(soup.prettify())

    # for links in soup.find_all('td'):
    #     link = links.get('style')
    #     print(link)
    arr = []
    for links in soup.find_all('div'):
        link = links.get('style')
        if link.find("color:#111111;") == 0:
            arr.append(links.text[1:])
        # if(link == 'selectorgadget_suggested'):
        #
        #     print(links.text)
   
    abc=[] 
    c=0 
    a=""
    for i in arr:
     
     try:
        instagram = InstagramOSINT(username=i)
        c=c+1
        a = (instagram.scrape_profile())

     except Exception:
        a = "error"
     abc.append(a)
     if c==10:
      break
    return {"data":abc}

app.run()
