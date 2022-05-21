from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse


def home_page(request):
    if request.method == 'POST':
        text = request.POST.get('myText')
        start = request.POST.get('start')
        end = request.POST.get('end')
        context = {'text': text, 'start': start, 'end': end}

        # check if all empty
        if not text or not start or not end:
            messages.add_message(request, messages.ERROR, 'All fields are required')
        # try to convert the start and end values to int
        try:
            start = int(start)
            end = int(end)

            # start num can't be bigger than end num
            if start > end:
                messages.add_message(
                    request, messages.ERROR,
                    'Start number can not be bigger than the end number'
                )
            # end num can't be bigger than the text length
            elif end > len(text):
                messages.add_message(
                    request, messages.ERROR,
                    'End number can not be bigger than the text length'
                )
            else:
                colored_text = text[0:start] + "<span style='color:red'>" + text[start:end] + "</span>" + text[end:]
                context['colored_text'] = colored_text

        except ValueError:
            messages.add_message(request, messages.ERROR,
                                 'Please enter valid integer values in start and end field')

        return render(request, 'myapp/home_page.html', context)

    return render(request, 'myapp/home_page.html')
