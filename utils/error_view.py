from django.http import JsonResponse
 
def handler404(request,exception):
    message = ('Path not found ')
    response =JsonResponse(data ={'error':message})
    response.status_code=404
    return response
def handler500(request):
    message = ('Sorry , something wrong in Server ')
    response =JsonResponse(data ={'error':message})
    response.status_code=505
    return response