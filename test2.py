import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.isri import ISRIStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag

st = ISRIStemmer()

text = 'تتصدر بطاقة الجرافيك XFX GeForce 8800Ultra XXX لائحة أفضل 5 بطاقات حسب موقع بي سي ورلد1XFX GeForce 8800Ultra XXX: اداؤه عند تشغيل لعبة Battlefield 2 (1024 by 768): 80.74 صورة في الثانية. اداؤه عند تشغيل لعبة Half-Life 2 (1600 by 1200):128.53 صورة في الثانية.منفذ التوصيل بالكمبيوتر:PCI Express .الشريحة: nVidia GeForce 8800 Ultra.حجم الذاكرة الملحقة (بالميغابايت): 768.سرعة الذكرة (بالميغاهيرتز): 2300.سرعة المعالج (بالميغاهيرتز): 675.المنافذ الخارجية: Two DVI-out، Composite-Video-Out، S-Video-Out، Component Videoملحقات اخرى: 2 DVI-to-VGA adapters، video out adapter، S-Video cable / لعبة Tom Clancy\'s Ghost Reconالسعر عند اعداد التقرير:740 دولاراً.2XFX GeForce 8800GTS 640MB XXX: اداؤه عند تشغيل لعبة Battlefield 2 (1024 by 768):80.9 صورة في الثانية. اداؤه عند تشغيل لعبة Half-Life 2 (1600 by 1200):123.53 صورة في الثانية.منفذ التوصيل بالكمبيوتر: PCI Express.الشريحة: nVidia GeForce 8800 GTSحجم الذاكرة الملحقة (بالميغابايت): 640سرعة الذكرة (بالميغاهيرتز): 1800سرعة المعالج (بالميغاهيرتز):550المنافذ الخارجية: Two DVI-out، Composite-Video-Out، S-Video-Out، Component Videoملحقات أخرى: 2 DVI-to-VGA adapters، video out adapter، cable / S-Video لعبة Tom Clancy\'s Ghost Reconالسعر عند اعداد التقرير: 420 دولاراً.3Gigabyte Radeon HD2900XT(GA-RX29T512VH-B): اداؤه عند تشغيل لعبة Battlefield 2 (1024 by 768): 78.69 صورة في الثانية. اداؤه عند تشغيل لعبة Half-Life 2 (1600 by 1200): 120.5 صورة في الثانية.منفذ التوصيل بالكمبيوتر:PCI Express.الشريحة: ATI Radeon HD 2900 XTحجم الذاكرة الملحقة (بالميغابايت): 512سرعة الذكرة (بالميغاهيرتز): 1650سرعة المعالج (بالميغاهيرتز):740المنافذ الخارجية: Two DVI-out، Composite-Video-Out، S-Video-Out، S-Video-in، Audio Output، Component Videoملحقات أخرى: 2 DVI-to-VGA adapters، DVI to HDMI adapter، S-Video/Composite video I/O cable، component adapter cable، 2 power cables، Crossfire adapter/السعر عند اعداد التقرير: 429دولاراً.4Asus EAH2900XT: اداؤه عند تشغيل لعبة Battlefield 2 (1024 by 768):78.95 صورة في الثانية. اداؤه عند تشغيل لعبة Half-Life 2 (1600 by 1200):119.6 صورة في الثانية.منفذ التوصيل بالكمبيوتر: PCI Express.الشريحة: ATI Radeon HD 2900 XTحجم الذاكرة الملحقة (بالميغابايت): 512سرعة الذكرة (بالميغاهيرتز): 1650سرعة المعالج (بالميغاهيرتز): 740المنافذ الخارجية: Two DVI-out، Composite-Video-Out، S-Video-Out، S-Video-in، Audio Output، Component Videoملحقات أخرى: الالعاب STALKER: Shadow of Chernobyl، Coupon for free Half-Life: Black Box Collection (Half-Life: Episode 2; Team Fortress 2; Portal)السعر عند اعداد التقرير: 419 دولاراً5XFX GeForce8800GTS 320MB XXX: اداؤه عند تشغيل لعبة Battlefield 2 (1024 by 768):80.75 صورة في الثانية. اداؤه عند تشغيل لعبة Half-Life 2 (1600 by 1200) :124.7 صورة في الثانية.منفذ التوصيل بالكمبيوتر: PCI Express.الشريحة: nVidia GeForce 8800 GTSحجم الذاكرة الملحقة (بالميغابايت): 320سرعة الذكرة (بالميغاهيرتز): 1800سرعة المعالج (بالميغاهيرتز): 580المنافذ الخارجية: Two DVI-out، S-Video-Out، Composite-Video-Out، Component Videoملحقات أخرى: 2 DVI-to-VGA adapters، component adapter، S-Video cable/ لعبة Lost Planetالسعر عند اعداد التقرير: 309 دولارات.'

# toknizing text
tokenizer = RegexpTokenizer(r'\w+')
tokenized_text = [token for token in tokenizer.tokenize(text)]
# make a part of speech tagging
tags = pos_tag(tokenized_text)

# a function to do stemming just for but not for specific names of people, places, or organizations
def stemming(tags):
    stemed_tokens = []
    for token,tag in tags:
        if tag == 'NNP':
            stemed_tokens.append(token)
        else:
            stem = st.stem(token)
            stemed_tokens.append(stem)
    return stemed_tokens
# stop words removal
arabic_stopwords = set(stopwords.words('arabic'))
filtred_text = [token for token in stemming(tags) if token not in arabic_stopwords]

# bind the tokens toghether
new_text = ' '.join(filtred_text)
print(new_text)
#print(filtred_text)


