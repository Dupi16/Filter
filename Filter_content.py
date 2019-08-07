from underthesea import sent_tokenize
from underthesea import word_tokenize

#demo content


def fil_content(news):
    sentence_li = sent_tokenize(news)
    for sentence in sentence_li:
        word_li = word_tokenize(sentence)

    count = 0
    for word in li_1:
        if word in word_li:
            count += 1
        else:
            continue
    if count >= 2:
        print("Negative content")
    else:
        print("It's ok")


#demo content
news_content = "Việt gian đã tạo ra những điều tởm lợm, đàn áp dân, một chính trị thối nát, thối nát"
li_1 = ["Việt gian", 'đàn áp', "chính trị", "thối nát"]
fil_content(news_content)

            
