from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("this is home page")
    friends = ["brajesh","nitesh","kunal","rahul"]
    return JsonResponse(friends,safe=False)