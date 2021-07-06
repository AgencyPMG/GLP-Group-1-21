import os
import sys
import random
from shutil import copyfile

def split_data(base, training, testing, split_size=0.9):
    categories_full = ['adults _ women _ shirts',
                    'adults _ women _ shoes',
                    'adults _ men _ outwear _ sweatshirts',
                    'adults _ men _ pants _ jeans',
                    'adults _ women _ outwear _ sweaters']
    categories = ['shirts',
                    'shoes',
                    'sweatshirts',
                    'jeans',
                    'sweaters']
    def sort_categories(data):
        cat1 = []
        cat2 = []
        cat3 = []
        cat4 = []
        cat5 = []
        for datum in data:
            #sys.stdout.write(str(datum))
            #name_cat = datum.split('_')
            
            if categories[0] in datum:
                cat1.append(datum)
            elif categories[1] in datum:
                cat2.append(datum)
            elif categories[2] in datum:
                cat3.append(datum)
            elif categories[3] in datum:
                cat4.append(datum)
            elif categories[4] in datum:
                cat5.append(datum)
            else:
                sys.stdout.write('NOT FOUND ')
                
        return cat1, cat2, cat3, cat4, cat5
    
    def fill_directories(data, training, testing, split_size=0.9):
        train = random.sample(data, round(split_size * len(data)))
        test = list(set(data) - set(train))

        for x in train:
             # sys.stdout.write(' ! ')
             # sys.stdout.write(str(x))
             # sys.stdout.write(' ! ')
             # sys.stdout.write(str(base + x))
             # sys.stdout.write(' ! ')
             # sys.stdout.write(str(training + x))
             # sys.stdout.write(' ! ')
             copyfile(base + x, training + x)
                
        for x in test:
             copyfile(base + x, testing + x)
                
            
    # Get all files into array and get rid of files that are empty
    data = [x for x in os.listdir(base)]# if os.path.getsize(base + x) > 0]
    
    # Split data into categories
    cats = sort_categories(data)
    # Fill directories
    for i in range(len(cats)):
        fill_directories(cats[i], training, testing, split_size)

if __name__ =='__main__':
    training = 'src/train/data/training/'
    testing = 'src/train/data/testing/'
    source = 'src/train/data/images/'

    split_data(source, training, testing)