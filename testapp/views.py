from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request, 'testapp/index.html')

def movies_view(request):
    head_msg = 'Movies Info'
    sub_msg1 = 'Saripoda Sanivaram is a good movie.'
    sub_msg2 = 'Planning for Aashiqui-3 with Mahesh sir'
    sub_msg3 = "Don't go for movies. Practice Django instead."
    type = 'movies'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3, 'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_view(request):
    head_msg = 'Sports Info'
    sub_msg1 = 'Australia won the match against England.'
    sub_msg2 = 'Next World Cup is for India.'
    sub_msg3 = "Who is upcoming coach of team India?"
    type = 'sports'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3, 'type':type}
    return render(request,'testapp/news.html',my_dict) 

def politics_view(request):
    head_msg = 'Politics Info'
    sub_msg1 = 'Indian prime minister is Narendra Modi.'
    sub_msg2 = 'Chief Minister of Odisha is Mohan Charan Majhi'
    sub_msg3 = "BJP won the 2024 general election."
    type = 'politics'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3, 'type':type}
    return render(request,'testapp/news.html',my_dict)