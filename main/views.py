from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2506561542 ',
        'name': 'Fanny Demarin',
        'class': 'KKI'
    }

    return render(request, "main.html", context)