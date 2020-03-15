from selenium import webdriver
import time


def fill_results(url, filename):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(0.5)
    input_field = driver.find_element_by_class_name('form-control')
    input_field.send_keys('Kazakhstan')

    ths = ['Country', 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases',
          'Serious / Critical', 'Total Cases / 1M population']

    tds = driver.find_elements_by_tag_name('td')[:9]

    file = open(filename, 'w+')
    for th, td in zip(ths, tds):
        td_text = td.text
        if td_text == '':
            td_text = 'no data'
        file.write("%-30s %s\n" %(th+':', td_text))
    file.close()


def main():
    url = 'https://www.worldometers.info/coronavirus/'
    filename = 'results.txt'
    fill_results(url, filename)





if __name__ == '__main__':
    main()
