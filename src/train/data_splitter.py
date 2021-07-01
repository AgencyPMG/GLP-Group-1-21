import random
from shutil import copyfile

def split_data(base, training, testing, split_size=0.9):
    categories = ['adults>women>shirts',
                    'adults>women>shoes',
                    'adults>men>outwear>sweatshirts',
                    'adults>men>pants>jeans',
                    'adults>women>outwear>sweaters']
    def sort_categories(data):
        cat1 = []
        cat2 = []
        cat3 = []
        cat4 = []
        cat5 = []
        for datum in data:
            if categories[0] in datum:
                cat1.append(datum)
            if categories[1] in datum:
                cat2.append(datum)
            if categories[2] in datum:
                cat3.append(datum)
            if categories[3] in datum:
                cat4.append(datum)
            if categories[4] in datum:
                cat5.append(datum)
                
        return cat1, cat2, cat3, cat4, cat5
    
    def fill_directories(data, training, testing, split_size):
        train = random.sample(data, round(split_size * len(data)))
        test = list(set(data) - set(train))
        
        for x in train:
             copyfile(base + x, training + x)
                
        for x in test:
             copyfile(base + x, testing + x)
                
            
    # Get all files into array and get rid of files that are empty
    data = [x for x in os.listdir(base) if os.path.getsize(base + x) > 0]
    
    # Split data into categories
    cats = sort_cats_dogs(data)
    
    # Fill directories
    for i in range(len(cats)):
        fill_directories(cats[i], training+categories[i], testing+categories[i], split_size)

if __name__ =='__main__':
    training = 'src/train/data/training'
    testing = 'src/train/data/testing'
    source = 'src/train/data'

    split_data(source, training, testing)