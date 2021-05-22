from django.http import JsonResponse

# Create your views here.

data = {
"Name" : "Dixie Sasu",
"Track" : "Backend (Python)",
"Course" : "Python",
"Message" : "Hi, mentors! Thank you for your assistance, your time is greatly appreciated!"
}


def infopage_index(request):
    return JsonResponse(data)