def menora():
    ner = int(input("Enter today's ner number: "))
    candles = ner + 1
    return("For today's Ner you will need %d candles")%(candles)
print(menora())
def paint_menora():
    ner = int(input("Enter today's ner number: "))
    candle = "|"
    shamash = "!"
    menora = ""
    if ner < 5:
        for i in range(ner):
            menora += candle
        return menora + shamash
    else:
        menora += candle*4 + shamash
        for i in range(ner-4):
            menora += candle
        return menora
print(paint_menora())
