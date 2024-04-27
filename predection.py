import joblib

my_model= joblib.load('new_press_articles_classifier.pkl')
count_vectorizer= joblib.load('count_vctorizer.pkl')

def categories_category(category):
    if category == 1:
        return 'Sports'
    elif category == 2:
        return 'Politics'
    elif category == 3:
        return 'Culture'
    elif category == 4:
        return 'Finance'
    elif category == 5:
        return 'Medical'
    elif category == 6:
        return 'Religion'
    elif category == 7:
        return 'Tech'
    elif category == 8:
        return 'Cars'
    elif category == 9:
        return 'Economy'
    elif category == 10:
        return 'Health'
    elif category == 11:
        return 'Tourism'
categories = []
def predect_new_category(article):
    
    article_count_vctorizer = count_vectorizer.transform(article)
    category = categories_category(my_model.predict(article_count_vctorizer)[0])
    return category

article3 = [
    'شهدت الأعوام الأربعة الأولى من تولّي السيد رئيس الجمهورية شؤون الحكم، حيوية بارزة للاقتصاد الجزائري الذي كان على موعد بين عامي 2019 و2023 مع تحولات كبرى وإنماء نوعي تستعرضهما "ملتيميديا الإذاعة الجزائرية" في التقرير التالي. حدّد رئيس الجمهورية في العام الأول من عهدته، الإطار المرجعي للنموذج الاقتصادي الجديد، راسماً معالم خطة الانتعاش الاقتصادي، انطلاقاً من "إتاحة الفرص للجميع" و"تعزيز سمو القانون وتكافؤ الفرص، والتشاركية في رسم السياسات، وتحقيق الاستدامة الـمالية وتقوية الـمؤسسات، ورفع مستوى وكفاءة التعليم". وقام النموذج الاقتصادي الجديد على تنويع النمو واقتصاد المعرفة، ووضع سياسة تصنيع جديدة موجّهة نحو الصناعات المصغّرة والمتوسطة والناشئة، وتعطي الأولوية في مجال التركيب الصناعي للمنتجات الضامنة لأعلى نسبة من الإدماج الوطني". وجرى ضبط الرهان الأكبر في تفعيل مليون مؤسسة مصغّرة، بغرض تطوير النسيج الاقتصادي وجلب القيمة المضافة، مع تطوير المؤسسات المصغّرة الناشطة في القطاعين الزراعي والصناعي، وابتعاث مؤسسات ناشئة لتطوير برامج ومنصات لرقمنة المجتمع وأخرى لترقية الحلول المدمجة وتحسين الأنشطة والتمويل، وما يتصلّ بالذكاء الصناعي، وتشجيع حاملي المشروعات الابتكارية لبناء أرضية خصبة للمقاولاتية ونقل المعرفة ورفع جودة ونوعية المنتوج المحلي وتعزيز قدرته التنافسية. وجرى إقرار تسهيل منح القروض ودعم المؤسسات الناشئة للاستثمار في إفريقيا، وجرد كل الثروات الوطنية الطبيعية غير المستغلة "رفعاً لطاقات التصدير، وتعويضاً عن أي نقص من عائدات المحروقات، وحفاظاً على حق الأجيال الصاعدة في هذه الثروة". وركّز النموذج ذاته على بناء صناعة وطنية حقيقية ضمن اقتصاد وطني حقيقي ومنتج، محدّداً آجالاً واضحة الأهداف من خلال مراجعة الإطار التشريعي المتعلق بترقية الاستثمار وإعادة تنظيم القطاع الاقتصادي العمومي التابع لها، قصد إعادة بعثه وفصله تمامًا عن الخزينة العمومية كمموّل أساسي. واهتمّ النموذج الاقتصادي لرئيس الجمهورية بترقية ودعم الأنشطة الاقتصادية القائمة على المعرفة، ذات القيمة التكنولوجية العالية، ودعم المؤسسات الصغيرة، وتشجيع المؤسسات الناشئة التي يقودها أصحاب الشهادات من الشباب ودعم وترقية دور قطاع البناء والأشغال العمومية لما له من دور محوري في دعم النمو الاقتصادي وامتصاص البطالة. وإضافة إلى ما تقدّم، جرى تحسين مناخ الأعمال من خلال تبسيط إجراءات إنشاء المؤسسات، وتوفير العقار والاستفادة من القروض والخدمات العمومية ذات الجودة، وإصلاح وعصرنة النظام البنكي والإدارة ومكافحة السلوك البيروقراطي.'
]

print(predect_new_category(article3))