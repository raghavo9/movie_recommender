def img_scrapper(value):
    from bs4 import BeautifulSoup
    import requests
    #value = 'quantum of solace'
    base_url = "https://www.cinematerial.com/"
    page_url = base_url + 'search?q=' + value

    source = requests.get(page_url).text
    soup = BeautifulSoup(source, 'lxml')

    link_value = " ".join(value.split("+"))

    value1 = soup.findAll("a")
    #value1 = soup.findAll("img",src=True)

    '''
    try:

        m_needed=[]
        for i in value1:
            temp=i['src']
            if temp[0:5]=="https" :
                m_needed.append(i['src'])
        return(m_needed[1])


    except:
        pass

    '''


    
    #print(value1)
    my_image=None
    try:

        for i in value1:
            if (i.text).lower() == link_value.lower():
                needed = i
                value2 = needed['href']
                complete_url = base_url + value2
                source1 = requests.get(complete_url).text
                soup1 = BeautifulSoup(source1, 'lxml')
                img_list = soup1.findAll("img", src=True)
                needed_image = img_list[1]
                my_image = needed_image['data-src']
                return my_image
    except:
        value1 = soup.findAll("img", src=True)
        m_needed = []
        for i in value1:
            temp = i['src']
            if temp[0:5] == "https":
                m_needed.append(i['src'])
        return (m_needed[1])



    # print(complete_url)












#print(img_scrapper("Terminator+2:+Judgment+Day"))



#print(img_scrapper("Titanic"))




#https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/300px-No_image_available.svg.png