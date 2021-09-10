import pyttsx3
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Check the voices options
# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print("\n")

engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# text = str(input("Paste link related to article\n"))
text = 'https://saude.estadao.com.br/noticias/geral,escassez-de-astrazeneca-afeta-mais-de-95-dos-postos-da-cidade-de-sao-paulo,70003836689'
res = requests.get(text)
soup = BeautifulSoup(res.text, 'html.parser')
body = soup.find('body')
content = body.find(class_='n--noticia__content content')

articles = []

for i in range(len(content.select('p'))):
    article = soup.select('p')[i].getText().strip()
    articles.append(article)
    text = " ".join(articles)

    # Speak the article
    # speak(article)

engine.save_to_file(text, 'test.mp3')
# If you want to save the speech as a audio file

engine.runAndWait()
