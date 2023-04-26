from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
from rapidfuzz import process, fuzz

import time
import pandas as pd

website = "https://www.audible.com/search"
path = "/Users/hveer/Downloads/chromedrive"

driver = webdriver.Chrome(options=options, service=Service(path))
driver.get(website)

time.sleep(3)

try:
    menu = driver.find_element(By.XPATH, '//span[contains(@class,"bc-button-text-inner")][contains(text(), "Go back to Audible.com")]')
    menu.click()
except:
    pass

try:
    popup = driver.find_element(By.XPATH, '//a[@class="at-popup-content"]/div')
    popup.click()
except:
    pass

time.sleep(3)
try:
    menu = driver.find_element(By.XPATH, '//span[contains(@class,"bc-button-text-inner")][contains(text(), "Go back to Audible.com")]')
    menu.click()
except:
    pass


title = []
subtitle = []
author = []
narrator = []
series = []
length =[]
release_date = []
language = []
ratings = []

category_mapping = {
    'Arts & Entertainment': 1,
    'Biographies & Memoirs': 2,
    'Business & Careers': 3,
    "Children's Audiobooks": 4,
    'Comedy & Humor': 5,
    'Education & Learning': 6,
    'Computers & Technology': 7,
    'Erotica': 8,
    'Health & Wellness': 9,
    'History': 10,
    'Home & Garden': 11,
    'LGBTQ+': 12,
    'Literature & Fiction': 13,
    'Money & Finance': 14,
    'Mystery, Thriller & Suspense': 15,
    'Politics & Social Sciences': 16,
    'Relationships, Parenting & Personal Development': 17,
    'Religion & Spirituality': 18,
    'Romance': 19,
    'Science & Engineering': 20,
    'Science Fiction & Fantasy': 21,
    'Sports & Outdoors': 22,
    'Teen & Young Adult': 23,
    'Travel & Tourism': 24,
}

fil_1_map = {
    'Plus Catalog': 1,
    'Free Titles': 2
}

fil_2_map = {
    'Coming Soon': 3,
    'Last 30 Days': 4,
    'Last 90 Days': 5
}

fil_3_map = {
    'Up to 1 hour': 6,
    '1 to 3 hours': 7,
    '3 to 6 hours': 8,
    '6 to 10 hours': 9,
    '10 to 20 hours': 10,
    '20 hours & above': 11
}

fil_4_map = {
    'English': 12,
    'Spanish': 13,
    'German': 14,
    'French': 15,
    'Portuguese': 16,
    'Italian': 17,
    'Japanese': 18,
    'Afrikaans': 19,
    'Danish': 20,
    'Russian': 21,
    'Czech': 22,
    'Mandarin Chinese': 23
}

fil_5_map = {
    'Abridged': 25,
    'Unabridged': 26
}

fil_6_map = {
    'Whispersync for Voice': 27
}

do_input = True

while True:
    books = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
    try:
        if do_input == True:
            ans = str((input('Would you like to select books by category? (Y/N) ')))
            if ans.lower() == 'y' or ans.lower() == 'yes':
                cat = str((input('Which category would you like to select? ')))
                cat = process.extractOne(cat, category_mapping.keys(), scorer=fuzz.token_set_ratio, score_cutoff=50)
                if cat:
                    cat = category_mapping[cat[0]]
                    category_link = driver.find_element(By.XPATH, f'//div[contains(@class, "categories")]//ul/li[{cat}]/a')
                    category_link.click()
                    books = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
                fil_1 = str((input('Would you like to filter by Access? ')))
                fil_1 = process.extractOne(fil_1, fil_1_map.keys(), scorer=fuzz.token_set_ratio, score_cutoff=50)
                if fil_1:
                    fil_1 = fil_1_map[fil_1[0]]
                    filter_1_link = driver.find_element(By.XPATH, f'//section[@class="otherFilters"]/.//./li[contains(@class, "bc-list-item")][{fil_1}]/a')
                    books = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
                else:
                    print('Defaulting to no Access filter...')
                fil_2 = str((input('Would you like to filter by New Releases? ')))
                fil_2 = process.extractOne(fil_2, fil_2_map.keys(),scorer=fuzz.token_set_ratio, score_cutoff=50)
                if fil_2:
                    fil_2 = fil_2_map[fil_2[0]]
                    filter_2_link = driver.find_element(By.XPATH, f'//section[@class="otherFilters"]/.//./li[contains(@class, "bc-list-item")][{fil_2}]/a')
                    books = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
                else:
                    print('Defaulting to no New Releases filter...')
                fil_3 = str((input('Would you like to filter by Duration? ')))
                fil_3 = process.extractOne(fil_3, fil_3_map.keys(), scorer=fuzz.token_set_ratio, score_cutoff=50)
                if fil_3 in fil_3_map:
                    fil_3 = fil_3_map[fil_3[0]]
                    filter_3_link = driver.find_element(By.XPATH, f'//section[@class="otherFilters"]/.//./li[contains(@class, "bc-list-item")][{fil_3}]/a')
                    books = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
                else:
                    print('Defaulting to no Duration filter...')
                fil_4 = str((input('Would you like to filter by Language? ')))
                fil_4 = process.extractOne(fil_4, fil_4_map.keys(), scorer=fuzz.token_set_ratio, score_cutoff=50)
                if fil_4:
                    fil_4 = fil_4_map[fil_4[0]]
                    filter_4_link = driver.find_element(By.XPATH, f'//section[@class="otherFilters"]/.//./li[contains(@class, "bc-list-item")][{fil_4}]/a')
                    books = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
                else:
                    print('Defaulting to no Language filter...')
                fil_5 = str((input('Would you like to filter by Abridgement? ')))
                fil_5 = process.extractOne(fil_5, fil_5_map.keys(), scorer=fuzz.token_set_ratio, score_cutoff=50)
                if fil_5:
                    fil_5 = fil_5_map[fil_5[0]]
                    filter_5_link = driver.find_element(By.XPATH, f'//section[@class="otherFilters"]/.//./li[contains(@class, "bc-list-item")][{fil_5}]/a')
                    books = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
                else:
                    print('Defaulting to no Abridgement filter...')
                fil_6 = str((input('Would you like to filter by Whipsersync? ')))
                fil_6 = process.extractOne(fil_6, fil_6_map.keys(), scorer=fuzz.token_set_ratio, score_cutoff=50)
                if fil_6:
                    fil_6 = fil_6_map[fil_6[0]]
                    filter_6_link = driver.find_element(By.XPATH, f'//section[@class="otherFilters"]/.//./li[contains(@class, "bc-list-item")][{fil_6}]/a')
                    books = driver.find_elements(By.XPATH, '//li[contains(@class,"productListItem")]')
                    do_input = False
                else:
                    print('Defaulting to no Whispersync filter...')
                    do_input = False
            else:
                print('Defaulting to all...')
    except ValueError:
        continue
    for book in books:
        try:
            title.append(book.find_element(By.XPATH, './/h3/a').text)
        except:
            title.append(None)
        try:
            subtitle.append(book.find_element(By.XPATH, './/li[contains(@class, "subtitle")]').text)
        except:
            subtitle.append(None)
        try:
            author.append(book.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        except:
            author.append(None)
        try:
            narrator.append(book.find_element(By.XPATH, './/li[contains(@class, "narratorLabel")]').text)
        except:
            narrator.append(None)
        try:
            series.append(book.find_element(By.XPATH, './/li[contains(@class, "seriesLabel")]').text)
        except:
            series.append(None)
        try:
            length.append(book.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)
        except:
            length.append(None)
        try:
            release_date.append(book.find_element(By.XPATH, './/li[contains(@class, "releaseDateLabel")]').text)
        except:
            release_date.append(None)
        try:
            language.append(book.find_element(By.XPATH, './/li[contains(@class, "languageLabel")]').text)
        except:
            language.append(None)
        try:
            ratings.append(book.find_element(By.XPATH, './/li[contains(@class, "ratingsLabel")]').text)
        except:
            ratings.append(None)
    try:
        next = driver.find_element(By.XPATH, '//li[contains(@class,"bc-list-item")]//span[contains(@class, "nextButton")]/a')
        next.click()
        time.sleep(3)
    except:
        break

category = driver.find_element(By.XPATH, '//div[contains(@class, "linkListWrapper")]//li/span[contains(@class, "bold")]')
category = category.text
df = pd.DataFrame({'Title': title, 'Subtitle': subtitle, 'Narrated By': narrator, 'Series': series, 'Length': length, 'Release Date': release_date, 'Language': language, 'Ratings': ratings})
df.to_csv(f"AudibleBooksData_{category}.csv", index=False)