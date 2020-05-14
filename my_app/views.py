from django.shortcuts import render

import scrapper
import better

import threading

def home(request):
    return render(request,'my_app/home.html')

def mov_res(request):
    val = request.POST['title']

    ml = better.improved_movie_recom(val)

    il = [None] * 10

    def func(j):
        xy = ml[j]
        n = xy.split(" ")
        sum_string = "+".join(n)
        image_link = scrapper.img_scrapper(sum_string)
        if image_link == None:
            image_link = "data:image/jpeg;base64,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"
        il[j] = image_link

    threads = []
    for i in range(10):
        t = threading.Thread(target=func, args=(i,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    return render(request, 'my_app/result.html',{'movie': val, 'ai': ml[0], 'bi': ml[1], 'ci': ml[2], 'di': ml[3], 'ei': ml[4], 'fi': ml[5],'gi': ml[6], 'hi': ml[7], 'ii': ml[8], 'ji': ml[9], 'a': il[0], 'b': il[1], 'c': il[2], 'd': il[3],'e': il[4], 'f': il[5], 'g': il[6], 'h': il[7], 'i': il[8], 'j': il[9]})



