import requests
import time

PAGE_TOKEN = "EAAOCqtZBPzcIBRTK3ZBby5LE9Ixr8595jBRqQZA9xZANyw5nEmD6FJbTakTrri8nUuST5jq5l1lT6Qr4BWIXALn7qC5f4idzKlQvdkUj5CoLvSxS0Q3FBGLWNKDCTkrfGxcNFXZBgHnbq7UsGytvo4xKXuFo6jyDhbzihhZC0fIz5Bf8QLgsRVngBjDrOKbjCahZAZC2bNNYexdrFiCG1QXZBExfnZAgudc6YZCfrQqIgZDZD"
PAGE_ID = "202568206273016"
NEWS_API_KEY = "744c32d0ea194d33807c80a77ae35bff"

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?q=futbol&language=es&apiKey={NEWS_API_KEY}"
    r = requests.get(url)
    articles = r.json().get("articles", [])
    if articles:
        return articles[0]["title"], articles[0]["url"]
    return None, None

def post_to_facebook(message):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    payload = {"message": message, "access_token": PAGE_TOKEN}
    requests.post(url, data=payload)

while True:
    title, link = get_news()
    if title:
        post_to_facebook(f"⚽ {title}\n\n{link}")
    time.sleep(7200)
