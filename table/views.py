from django.shortcuts import render

# Create your views here.

def table(request):
    result=[]
    if request.method=='POST':
        num1 = int(request.POST.get('number1'))
        num2 = int(request.POST.get('limit'))
        
        for i in range(1,(num2+1)):
            result.append(str(num1)+ ' * '+ str(i)+ ' = ' + str(num1*i))
            
        return render(request, 'table.html',{'result':result, 'num1':num1, 'num2':num2})
    else:
        return render(request, 'table.html')