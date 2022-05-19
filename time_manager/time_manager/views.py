from django.shortcuts import render, redirect

def main_redirect(request):
    return redirect('main/')