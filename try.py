quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'

with open('quotes.txt', 'a', encoding='utf-8') as f:
    f.write(quote)

    f.close()