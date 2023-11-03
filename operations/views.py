from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

#ADDITION
class AdditionView(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response(data=res)
    
 #SUBSTRACTION   
class SubstractionView(APIView):
    def post(self ,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response(data=res)
    
#MULTIPLICATION    
class MultiplicationView(APIView):
    def post(self,request,*args,**kw):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1*n2
        return Response(data=res)
    
#FACTORIAL
class FactView(APIView):
    def post(self,request,*args,**kw):
        num=request.data.get("num")
        fact=1
        for i in range(1,(num+1)):
            fact=fact*i

        return Response(data=fact)

 #PRIMENUMBER 
class PrimeNumberView(APIView):
    def post(self,request,*args,**kw):
        num=request.data.get("num")
        is_prime=True
        for i in range(2,num):
            if(num%i==0):
                is_prime=False
                break
        return Response(data=is_prime)        