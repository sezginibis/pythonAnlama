#Bu benim bulduğum çözüm yöntemi idi
cumle = "bugün hava çok güzel"

for i in cumle.split(" "):
    print(i,"\n")

#Bu da eğitmenin gösterdiği yöntem idi.
cumle1 = "Bugün hava gerçekten ama gerçekten çok güzel."

kelimeler = cumle1.split(" ")
kelimeler.sort()

print(kelimeler)

for kelime in kelimeler:
    print(kelime) 

print("--------------Şimdi de daha sade bir çözüm bulalım.-----------")
cumle2 = "Bugün hava -çok |güzel. \$%()\{\}\[\]bana \" hava \' gerçekten.,!:;/ Evet güzel bir gün, gerçekten. Havada bulut yok ve işte bu yüzden güzel bir gün."

for noktalama in '''-|\$%(){}[]"'.,!:;/''':
    cumle2=cumle2.replace(noktalama,' ')
cumle2 = cumle2.lower()

cumleKelimeleri = cumle2.split()
tumKelimeler = {}
for kelime1 in cumleKelimeleri:
    if kelime1 not in tumKelimeler:
        tumKelimeler[kelime1] = 1
    else:
        tumKelimeler[kelime1] += 1

for key in tumKelimeler.keys():
    print("Kelime: %s => %s adet" %(key, tumKelimeler[key]))
print("Toplam:",len(tumKelimeler),"kelime bulundu.")
