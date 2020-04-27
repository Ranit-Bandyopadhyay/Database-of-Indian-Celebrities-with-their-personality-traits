from bs4 import BeautifulSoup
import pandas as pd
import simple as s
'----------------------------------------------------------------------------------------------------------------------------------------'
class mbit():

    def name_1(self):
        trait = []

        n = []
        with open('traits_1.html') as html_file:
            soup2 = BeautifulSoup(html_file, 'lxml')

        for name in soup2.findAll('div', class_='postContainer copycontent'):
            trait.append(name.text)

        z = trait[0].split('-')
        for i in range(1,len(z)-2):
            if (i == 0):
                n.append(z[i].split('.')[-1])
            else:
                if (z[i][:5].isupper() == True):

                    #b.append(z[i][:5])
                    n.append(z[i][5:])
                else:
                    #b.append(z[i][10:15])
                    n.append(z[i][14:])

        return n

    def traits_1(self):
        trait = []
        b = []
        with open('traits_1.html') as html_file:
            soup2 = BeautifulSoup(html_file, 'lxml')

        for name in soup2.findAll('div', class_='postContainer copycontent'):
            trait.append(name.text)

        z = trait[0].split('-')
        for i in range(1,len(z)-1):
            if (z[i][:5].isupper() == True):

                b.append(z[i][:5])
                #n.append(z[i][5:])
            else:
                b.append(z[i][10:15])
                #n.append(z[i][15:])
        return b


    def name_2(self):
        trait = []
        n = []
        with open('traits_2.html') as html_file:
            soup3 = BeautifulSoup(html_file, 'lxml')

        for name in soup3.findAll('div', class_='postContainer copycontent'):
            trait.append(name.text)
        z = trait[0].split('-')
        for i in range(len(z) - 2):
            if (i == 0):
                n.append(z[i][-11:])
            else:
                n.append(z[i][5:])
        return n

    def traits_2(self):
        trait = []
        b = []
        with open('traits_2.html') as html_file:
            soup3 = BeautifulSoup(html_file, 'lxml')

        for name in soup3.findAll('div', class_='postContainer copycontent'):
            trait.append(name.text)
        z = trait[0].split('-')
        for i in range(1,len(z) - 2):
            b.append(z[i][:5])
        return b

    '''def imgs_1(self):
        images = []
        names = []
        with open('simple.html') as html_file:                                      
            soup4 = BeautifulSoup(html_file, 'lxml')

        for name in soup4.findAll('a'):
            names.append(name.get('title'))

        for name in soup4.findAll('img'):
            images.append(name.get('src'))

        return images[3:-3]'''


    '''def name_of_imgs_1(self):
        images = []
        names = []
        with open('simple.html') as html_file:                      
            soup4 = BeautifulSoup(html_file, 'lxml')

        for name in soup4.findAll('a'):
            names.append(name.get('title'))

        for name in soup4.findAll('img'):
            images.append(name.get('src'))

        return names[39:63]'''

    def traits_3(self):
        z = []
        tr = []
        with open('traits.html') as html_file:
            soup1 = BeautifulSoup(html_file, 'lxml')

        for name in soup1.findAll('p', class_='ui_qtext_para u-ltr u-text-align--start'):
            z.append(name.text.split('-'))
        for i in range(len(z)):
            tr.append(z[i][-1])
        return tr

    def name_3(self):
        z = []
        nam = []
        with open('traits.html') as html_file:
            soup1 = BeautifulSoup(html_file, 'lxml')

        for name in soup1.findAll('p', class_='ui_qtext_para u-ltr u-text-align--start'):
            z.append(name.text.split('-'))
        for i in range(len(z)):
            nam.append(z[i][0])
        return (nam)

    '''def imgs_2(self):
        images = []
        names = []
        with open('simple_1.html') as html_file:                                      
            soup4 = BeautifulSoup(html_file, 'lxml')

        for name in soup4.findAll('a'):
            names.append(name.get('title'))

        for name in soup4.findAll('img'):
            images.append(name.get('src'))

        return images[3:-3]'''

    '''def name_of_imgs_2(self):
        images = []
        names = []
        with open('simple_1.html') as html_file:                      
            soup4 = BeautifulSoup(html_file, 'lxml')

        for name in soup4.findAll('a'):
            names.append(name.get('title'))

        for name in soup4.findAll('img'):
            images.append(name.get('src'))

        return names[39:63]'''


'--------------------------------------------------------------------------------------------------------------------------------------'
c=mbit()                                                   #OBJECT

v=c.traits_1()
x=c.traits_2()
n=c.traits_3()
joined_1=v+x+n
#print(joined_1)

w=c.name_1()
y=c.name_2()
l=c.name_3()
joined_2=w+y+l
#print(joined_2)
print('CREATING DATABASE....')
'---------------------------------------------------------------------------------------------------------------------------------------'
                                                           #REMOVE DUBLICATES
d=dict(zip(joined_2,joined_1))
joined=list(set(joined_2))
v=[]                                                #  joined_2--->joined      ,         joined_1--->v
for i in range(len(joined)):
    v.append(d[joined[i]])


#print(d)                                             #straight to the csv file
'----------------------------------------------------------------------------------------------------------------------------------------'
                                                        #  MANIPULATING THE JOINED LIST
for i in range(len(joined)):
    if(joined[i][-1]==' '):
        joined[i]=joined[i][0:-1]
'---------------------------------------------------------------------------------------------------------------------------------------'
                                                        #   RETRIEVE THE IMAGES

a=s.imgs_1()                                                               #image_link
b=s.imgs_2()
y=s.imgs_3()
op=s.imgs_4()
vp=s.imgs_5()
vn=s.imgs_6()
join_imgs=a+b+y+op+vp+vn

r=s.name_of_imgs_1()                                                       #names
p=s.name_of_imgs_2()
t=s.name_of_imgs_3()
cv=s.name_of_imgs_4()
bp=s.name_of_imgs_5()
bn=s.name_of_imgs_6()
join_name=r+p+t+cv+bp+bn

#print(joined)
#print(v)
#print(join_name)
#print(len(joined))
'---------------------------------------------------------------------------------------------------------------------------------------'
                                               #ALIGNING THE NAMES WITH THEIR IMAGE URL'S
dictionary=dict(zip(joined,v))

for i in range(len(join_name)):
    for j in range(len(joined)):
        if(join_name[i]==joined[j]):
            joined.append(join_name[i])
v.clear()
for i in range(len(joined)):
    v.append(dictionary[joined[i]])

joined=joined[56:]
v=v[56:]


#print(joined)                                        STRAIGHT TO CSV AS NAMES
#print(v)                                             STRAIGHT TO CSV AS TRAITS
'----------------------------------------------------------------------------------------------------------------------------------------'
                                                    # IMAGE URL'S
url=[]

di=dict(zip(join_name,join_imgs))
for i in range(len(join_name)):
    for j in range(len(joined)):
        if(join_name[i]==joined[j]):
            #print(di[join_name[i]])
            url.append('https:'+di[join_name[i]])
        else:
            continue
'---------------------------------------------------------------------------------------------------------------------------------------'
joined.append('Varun Dhavan')
joined.append('Disha Patani')
joined.append('Parineeti Chopra')
joined.append('Vicky Kaushal')
joined.append('Dino Morea')
joined.append('Irfan Khan')
joined.append('Priyanshu Chatterjee')
joined.append('Suniel Grover')
joined.append('Kapil Sharma')

v.append('ESFP')
v.append('ISFP')
v.append('ESTJ')
v.append('ISFJ')
v.append('ISTJ')
v.append('ESFP')
v.append('ENTJ')
v.append('ENFP')
v.append('ENTP')

url.append('https://img.indiaforums.com/person/320x240/10672-varun-dhawan.jpg')
url.append('https://img.indiaforums.com/person/320x240/12908-disha-patani.jpg')
url.append('https://img.indiaforums.com/person/320x240/10359-parineeti-chopra.jpg')
url.append('https://img.indiaforums.com/person/320x240/12561-vicky-kaushal.jpg')
url.append('https://img.indiaforums.com/person/320x240/0104-dino-morea.jpg')
url.append('https://img.indiaforums.com/person/320x240/7536-irrfan-khan.jpg')
url.append('https://img.indiaforums.com/person/320x240/0713-priyanshu-chatterjee.jpg')
url.append('http://nationnext.in/wp-content/uploads/2017/03/Sunil-Grover.jpg')
url.append('https://www.masala.com/sites/default/files/images/2019/11/25/Kapil-Sharma.jpg')


#print(url)                                        # STRAIGHT TO CSV AS IMAGE URL
'----------------------------------------------------------------------------------------------------------------------------------------'
                                                       #  CONVERTING TO DATAFRAME
ppp=pd.Series(joined,index=None,name="NAME")
yyy=pd.Series(v,index=None,name="TRAIT")
aaa=pd.Series(url,index=None,name="IMAGE URL")
final_1=pd.concat([ppp,yyy],axis=1)
final=pd.concat([final_1,aaa],axis=1)
final.to_csv('C:\\Users\\user\\Desktop\\n.csv')
'--------------------------------------------------------------------------------------------------------------------------------------'

print('FINISHED!')