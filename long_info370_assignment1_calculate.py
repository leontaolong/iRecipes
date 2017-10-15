import operator
import csv


# Takes data in cleanData_file_path and calculate the top 10 
# most frequently occurring ingredients in the ingredient list and output to calculated_file_path
def culculate(cleanData_file_path, calculated_file_path):
    with open(cleanData_file_path, "r") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        word_freq_dict = {} # for calculating overall counts
        word_prop_dict = {} # for calculating proportion
        recipes_num = 0
        recipe_set =[]
        for row in csvReader:
            recipe = row[1]
            # Calculate total number of recipes
            if recipe not in recipe_set:
                recipe_set.append(recipe) 
                recipes_num += 1

            words = row[2].split()
            words_list = [] # for looking for word duplicates in one row
            for word in words:
                # Update occurrences of the word in word_freq_dict
                if word not in word_freq_dict:
                    word_freq_dict[word] = 1
                else:
                    word_freq_dict[word] += 1
                
                # only count word once if there're duplicates in one row
                if word not in words_list:
                    if word not in word_prop_dict:
                        word_prop_dict[word] = 1
                    else:
                        word_prop_dict[word] += 1
                    words_list.append(word)

    # Sort word_prop_dict based on word occurrences    
    sorted_word_prop_dict = sorted(word_prop_dict.items(), key=operator.itemgetter(1))
    desc_sorted_word_prop_dict = tuple(reversed(sorted_word_prop_dict))

    f = open(calculated_file_path, 'w')
    writer = csv.writer(f, delimiter=',')

    for x in range(0,10): # top 10
        word = desc_sorted_word_prop_dict[x][0]
        prop = int((word_prop_dict[word])) / (recipes_num)
        count = word_freq_dict[word]
        writer.writerow([word, count, prop])

    f.close()