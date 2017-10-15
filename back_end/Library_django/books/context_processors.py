from . import models

def categoryList(request):
    try:
        categoryList = models.Category.objects.all()
    except:
        categoryList = None
    
    return {'categoryList': categoryList, }