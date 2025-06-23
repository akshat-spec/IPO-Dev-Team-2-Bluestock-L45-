from django.shortcuts import render

# def ipo_page(request):
#     return render(request, 'ipo-page.html')


from .models import IPO

## fetching all ipos from database and returning it and rendering the ipo-page.html
def ipo_page(request):
    ipos = IPO.objects.all()
    return render(request, 'ipo-page.html', {'ipos': ipos})
