from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def main(request):

    template=loader.get_template('main/main.html')
    list_of_states = ['Alabama','Alaska','Arizona' ,'Arkansas',
                        'California', 'Colorado' , 'Connecticut', 'Delaware', 'Florida', 'Georgia' ,
                        'Hawaii' , 'Idaho' , 'Illinois' , 'Indiana' , 'Iowa' ,'Kansas' ,
                        'Kentucky', 'Louisiana' , 'Maine' , 'Maryland' ,
                        'Massachusetts', 'Michigan', 'Minnesota' , 'Mississippi' , 'Missouri',
                        'Montana','Nebraska','Nevada','New Hampshire','New Jersey',
                        'New Mexico','New York''North Carolina', 'North Dakota','Ohio','Oklahoma',
                        'Oregon','Pennsylvania','Rhode Island','South Carolina',
                        'South Dakota','Tennessee','Texas','Utah','Vermont','Virginia',
                        'Washington','West Virginia','Wisconsin','Wyoming']

    degree_type = ['Bachelors','Masters','Associate','Certificate']
    school_type=['Public','Private - Non Profit' , 'Private - For Profit']
    location = [1, 2, 3, 4 , 5 , 6, 7 , 8 , 9, 10 ,11, 12]



    context = {
        'list_of_states':list_of_states,
        'degree_type':degree_type,
        'school_type':school_type,
        'location':location


    }
    return HttpResponse(template.render(context,request))



