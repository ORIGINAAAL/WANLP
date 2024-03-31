import os
import csv

def process_files(folderslist, csv_file):
    art_nbr = 0
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['article', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for foldername in folderslist:
            for filename in os.listdir(foldername):
                if filename.endswith('.txt'):                    
                    article_path = os.path.join(foldername, filename)
                    with open(article_path, 'r', encoding='utf-8') as article_file:
                        article_content = article_file.read()
                        writer.writerow({'article': article_content, 'category': foldername })
                        art_nbr += 1
                        print(f'\rnumber of articles = {art_nbr}',end='')
                        
        print('\nComplete !!')

folderslist = ['Sports', 'Politics', 'Culture']
process_files(folderslist, 'articles.csv')