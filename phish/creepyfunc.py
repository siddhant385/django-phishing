import requests

def send_msg(text):
   token = "2098196046:AAEYk9xSkSiR5VurgpvrXfLcApWKMzoTsjs"
   chat_id = "1747538159"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)
   print(results.json())

