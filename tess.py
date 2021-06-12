f = open('fr_exp_result.txt', encoding='utf-8')
o = open('en_exp_result.txt', encoding='utf-8')
en = []
fr = []
for i in o:
    en.append(i.replace('\n', ''))
for j in f:
    fr.append(j.replace('\n', ''))
r = open('result.txt','a', encoding='utf-8')
for y in range(len(en)):
    r.write(f'msgid {fr[y]}\nmsgstr {en[y]}\n\n')
