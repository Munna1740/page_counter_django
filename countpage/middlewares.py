from django.shortcuts import render

class UnderCon:
    def __init__(self,get_response):
        self.get_response= get_response

    def __call__(self,request):
        print("call from middleware befor view")
        response = render(request, 'countpage/uc.html')
        print("call from middleware after view")
        return response