import requests, schedule, time, os, smtplib
from bs4 import BeautifulSoup
from replit import db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


username = os.environ['mail_username']
password = os.environ['mail_password']


def sendEmail(price, budget, link):
  server = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host = server, port=port)
  s.starttls()
  s.login(username, password)
  email = f"""<p><a href='{link}'>This item</a> is now CAD ${price}, which is below your budget of CAD ${budget}0!</p>"""
  msg = MIMEMultipart()
  msg["To"] = username
  msg["From"] = username
  msg["Subject"] = "New Price Drop!"
  msg.attach(MIMEText(email, 'html'))
  s.send_message(msg)
  del msg


def sendLink():
  url = "https://www.ebay.ca/itm/314856806741?var=613371645570&epid=14060759650&itmmeta=01HQ216H17WW86BPPEPWB1CK6N&hash=item494eed9955:g:uWkAAOSwZTZlLY~L&itmprp=enc%3AAQAIAAAAwES2brUdP0yf186sWfVFfS9IFMqnlK4s8H88BxtluAg3gt4eRn6GZfZ7SqbEqMDr7zNm3gZAAUVcSHHdo%2BTHdgykzFBYb751D9kYBXQCZqcNOBqjS03OhvYoApNxthF49H3YKlgiilnLI9HR5NekIHavREOXbnlz92jJVIgGIMXCqHOB9gkPDO9jRuLpS4d7O2AjafZW9bTZcn2TECD2NqZkwqAlNCgjErcehzjItKcYWkDIFYAFwQbW3Af0Ajjf3w%3D%3D%7Ctkp%3ABk9SR_iQmsG4Yw"

  response = requests.get(url)
  html = response.text

  soup = BeautifulSoup(html, "html.parser")

  costs = soup.find_all("div", {"class": "x-price-approx"})

  for cost in costs:
    db["Budget"] = float(130)
    budget = db["Budget"]
    cost = cost.text
    cost = cost.replace("$", "")
    cost = cost.replace("C", "")
    cost = cost.replace("Approximately", "")
    keys = db.keys()
    if cost not in keys:
      cost = cost.strip()
      if float(cost) <= db["Budget"]:
        db[cost] = cost
        sendEmail(cost, budget, url)


schedule.every(24).hours.do(sendLink)

while True:
  schedule.run_pending()
  time.sleep(1)

    
  
  