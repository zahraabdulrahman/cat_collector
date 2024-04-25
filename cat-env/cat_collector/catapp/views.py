from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cat
# Create your views here.

def catapp(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def review(request):
    template = loader.get_template('review.html')
    return HttpResponse(template.render())


def addCat(request):
    if request.method == 'POST':
        nameval = request.POST.get('name')
        imageval = request.FILES.get('image')
        rarityval = request.POST.get('rarity')
        descriptionval = request.POST.get('description')
        obj = Cat(name=nameval, image=imageval, rarity=rarityval, description=descriptionval)
        obj.save()
        return redirect('cat', cId=obj.id)
    return render(request, "addCat.html", {})

def updateCat(request, cId):
    obj = Cat.objects.get(id=cId)
    if request.method == 'POST':
        nameval = request.POST.get('name')
        imageval = request.FILES.get('image')
        rarityval = request.POST.get('rarity')
        descriptionval = request.POST.get('description')
        obj.name = nameval
        obj.image = imageval
        obj.rarity = rarityval
        obj.description = descriptionval
        obj.save()
        return redirect('cat', cId=obj.id)
    return render(request, "updateCat.html", {'obj': obj})


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



