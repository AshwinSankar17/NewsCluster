from newspaper import Article

article = Article('https://www.thequint.com/news/india/india-china-faceoff-in-sikkim-small-indian-lt-who-punched-a-big-chinese-major')
article.download()
article.parse()
title = article.title
news = article.text
print((title,news))