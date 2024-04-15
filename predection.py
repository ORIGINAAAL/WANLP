import joblib

my_model= joblib.load('press_articles_classifier.pkl')
count_vectorizer= joblib.load('count_vctorizer.pkl')

def categories_category(category):
    if category == 1:
        return 'Sports'
    elif category == 2:
        return 'Politics'
    elif category == 3:
        return 'Culture'

def predect_new_category(article):
    article_count_vctorizer = count_vectorizer.transform(article)
    category = categories_category(my_model.predict(article_count_vctorizer)[0])
    return category

article3 = [
    'اختارت جامعة الجزائر "2" بالتنسيق مع التنظيمات الطلابية الناشطة في الجامعة، الاحتفال بيوم العلم بتحضير برنامج ثري جمع بين الأنشطة العلمية، ممثلة في عدد من المحاضرات التي تمحورت في مضمونها حول تمجيد يوم العلم المصادف لـ16 أفريل، وكذا أنشطة ثقافية ممثلة في أبيات شعرية وأخرى فنية رياضية تفاعل معها الطلبة الذين توافدوا على قاعة المحاضرات الكبرى للمشاركة في الاحتفالية. بدأت الاحتفالية بكلمة ترحيبية لرئيس الجامعة عبد الحميد خميسي، الذي تطرق من خلالها إلى أهمية العلم في بناء الأمم، وكيف يمكن له أن يكون سلاح ذو حديين فقد يكون وسيلة لإنقاذ البشرية وتحديدا في مجال معالجة الأمراض الخطيرة، كما يمكن له أن يتحول إلى وسيلة لتحطيم الإنسان وتدمير الشعوب، ودعا في الإطار الطلبة إلى الاهتمام بتعلم مختلف العلوم والانفتاح على العالم الخارجي.'
]
print(predect_new_category(article3))