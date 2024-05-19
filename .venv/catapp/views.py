from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cat
from .forms import CatForm
from .get_cat import get_random_cat
# Create your views here.

def catapp(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def review(request):
    template = loader.get_template('review.html')
    return HttpResponse(template.render())

def game(request):
    template = loader.get_template('game.html')
    return HttpResponse(template.render())

def firstCat(request):
    random_cat = get_random_cat()
    # Pass the random cat to the template
    context = {
        'random_cat': random_cat,
    }

    template = loader.get_template('firstCat.html')
    return HttpResponse(template.render(context, request))

def secondCat(request):
    random_cat = get_random_cat()
    context = {
        'random_cat': random_cat,
    }
    template = loader.get_template('secondCat.html')
    return HttpResponse(template.render(context, request))

def thirdCat(request):
    random_cat = get_random_cat()
    context = {
        'random_cat': random_cat,
    }
    template = loader.get_template('thirdCat.html')
    return HttpResponse(template.render(context, request))
def addCat(request):
    if request.method == 'POST':
        form = CatForm(request.POST)

        if form.is_valid():
            obj = form.save()
            return redirect('cat', cId=obj.id)
    form = CatForm(None)
    return render(request, "addCat.html", {'form':form})

def updateCat(request, cId):
    obj = Cat.objects.get(id=cId)
    if request.method == 'POST':
       form = CatForm(request.POST, instance=obj)
       if form.is_valied():
            obj.save()
            return redirect('cat', cId=obj.id)
    form = CatForm(instance=obj)
    return render(request, "updateCat.html", {'form': form})


def filterCats(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isName = request.POST.get('option1')
        isRarity = request.POST.get('option2')

        selected = request.POST.get('selectedRarity')

        myCats = Cat.objects.filter(name__icontains='or')
        myCats2 = myCats.filter(rarity__lte=100).exclude(description__icontains='Saad')

        print(f"selected rarity = {selected}")
        # now filter
        cats = __getCats()
        newCats = []
        for item in cats:
            contained = False
            if isName and string in item['name'].lower():
                contained = True
            if not contained and isRarity and string in item['rarity'].lower():
                contained = True
            if contained:
                newCats.append(item)
        return render(request, 'catList.html', {'cats': newCats})
    return render(request, 'search.html', {})



