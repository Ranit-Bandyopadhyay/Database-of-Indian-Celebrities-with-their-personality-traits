from bs4 import BeautifulSoup

def imgs_1():
    images = []
    names = []
    with open('simple.html') as html_file:  # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return images[3:-3]

def name_of_imgs_1():
    images = []
    names = []
    with open('simple.html') as html_file:                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return names[39:63]

def imgs_2():
    images = []
    names = []
    with open('simple_1.html') as html_file:                                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return images[3:-3]

def name_of_imgs_2():
    images = []
    names = []
    with open('simple_1.html') as html_file:                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return names[39:63]

def imgs_3():
    images = []
    names = []
    with open('simple_2.html') as html_file:                                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return images[3:-3]

def name_of_imgs_3():
    images = []
    names = []
    with open('simple_2.html') as html_file:                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return names[39:63]

def imgs_4():
    images = []
    names = []
    with open('simple_3.html') as html_file:                                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return images[3:-3]

def name_of_imgs_4():
    images = []
    names = []
    with open('simple_3.html') as html_file:                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return names[39:63]

def imgs_5():
    images = []
    names = []
    with open('simple_4.html') as html_file:                                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return images[3:-3]

def name_of_imgs_5():
    images = []
    names = []
    with open('simple_4.html') as html_file:                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return names[39:63]

def imgs_6():
    images = []
    names = []
    with open('simple_5.html') as html_file:                                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return images[3:-3]

def name_of_imgs_6():
    images = []
    names = []
    with open('simple_5.html') as html_file:                      # 431th line
        soup4 = BeautifulSoup(html_file, 'lxml')

    for name in soup4.findAll('a'):
        names.append(name.get('title'))

    for name in soup4.findAll('img'):
        images.append(name.get('src'))

    return names[39:63]
