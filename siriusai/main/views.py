from django.shortcuts import render
from .models import question
from .forms import questionForm
import pandas as pd

def about(request):
    quest = question.objects.all()
    return render(request, 'main/about.html', {'quest' : quest})

def func(request,model):
    if request.method == "POST":
        form = questionForm(request.POST)
        file_open = open('text_file.txt','w')
        arr = []
        for i in form:
            arr.append(str(i.value()))
            file_open.write(str(i.value())+'\n')

        arr1 = ['без ремонта',
                'designer',
                'косметический',
                'евро'
        ]
        dict1 = {
            'без ремонта':'Without renovation',
            'дизайнерский':'Designer',
            'косметический':'Cosmetic',
            'евро':'European-style renovation'
        }
        dict = {"Metro station": [arr[0]],
                "Minutes to metro": [int(arr[1])],
                "Number of rooms": [int(arr[2])],
                "Area": [int(float(arr[3]))],
                "Living area": [int(float(arr[4]))],
                "Kitchen area": [int(float(arr[5]))],
                "Floor": [int(arr[6])],
                "Number of floors": [int(arr[7])]
        }
        if arr[8] in arr1:
            dict['Renovation'] = dict1[arr[8].lower()]
        else:
            dict['Renovation'] = 'Without renovation'


        answer_ = str(int(model.predict(pd.DataFrame(dict))[0]) // 10000 * 10000)
        data = {
            'form': form,
            'answer': answer_
        }
        return render(request, 'main/titlepage.html', data)

    form = questionForm()

    data = {
        'form' : form,
        'answer' : ''
    }
    return render(request, 'main/titlepage.html', data)