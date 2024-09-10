from django.shortcuts import render
from .models import Income

def calculate_tax(request):
    context = {}
    if request.method == "POST":
        income = float(request.POST.get("income", 0))
        tax = calculate_income_tax(income)
        context = {
            "income": income,
            "tax": tax
        }
    return render(request, "tax_app/calculate_tax.html", context)

def calculate_income_tax(income):
    # 税率計算の仮定例
    if income <= 1950000:
        return income * 0.05
    elif income <= 3300000:
        return income * 0.1-97500
    elif income <= 6950000:
        return income * 0.2-427500
    elif income <= 9000000:
        return income * 0.23-636000
    elif income <= 18000000:
        return income * 0.33-1536000
    elif income <= 40000000:
        return income * 0.4-2796000
    else:
        return income * 0.45-4796000
