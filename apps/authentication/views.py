# -*- encoding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from django.views.decorators.http import require_GET

from crp import settings
from .forms import LoginForm, UserUpdateData
from .models import CustomUser
from ..members.models import Membros


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.success(request, "Usuario e/ou senha invalidos")
        else:
            messages.error(request, "Ocorreu um erro ao validar o formulário")

    return render(request, "registration/login.html", {"form": form, "msg": msg})


@login_required
@require_GET
def show_user_profile(request):
    try:
        membro = Membros.objects.get(user=request.user)
    except Membros.DoesNotExist:
        messages.warning(request, "Este usuário não é um membro cadastrado. "
                                  "Associe o usuário a um membro para que possa ver os dados completo de perfil.")
        membro = None

    context = {'membro': membro}
    return render(request, 'registration/user_profile.html', context)


@login_required
def update_profile_data(request, pk):
    try:
        profile = Membros.objects.get(user=request.user)

    except Membros.DoesNotExist:
        messages.warning(request, "Não é possivel editar os dados. É necessario que este usuário seja um membro.")
        return redirect("user_profile")

    if request.method == "POST":
        form = UserUpdateData(request.POST, request.FILES, instance=profile, user=request.user)
        if not form.is_valid():
            profile.user = request.user
            profile.save()
            messages.success(request, "Seus dados foram atualizados com sucesso!")
            return redirect("user_profile".format(messages))
        else:
            messages.warning(request, "Ocorreu um erro ao tentar salvar o fomulário")
            context = {"form": form, }
    else:
        form = UserUpdateData(instance=profile, user=request.user)
        context = {
            "form": form,
        }
    return render(request, 'registration/user_update_profile.html', context)


@login_required
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = CustomUser.objects.filter(email=data)
            if not associated_users:
                messages.warning(request, "Email Invalido! Informe o seu email de cadastro")
            if associated_users.exists():
                for user in associated_users:
                    subject = "Solicitação de alteração de senha"
                    email_template = "registration/password/password_reset_email.txt"

                    context = {
                        "email": user.email,
                        'domain': 'comunidaderp.com.br',
                        'site_name': 'CRP',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user.first_name,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                    }
                    html_content = render_to_string(email_template, context=context)
                    text_content = strip_tags(html_content)

                    email = EmailMultiAlternatives(
                        subject,
                        text_content,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[user.email]
                    )
                    email.attach_alternative(html_content, 'text/html')

                    try:
                        send_mail(subject, text_content, 'Troca de senha', [user.email])
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("password_reset/done/")
    password_reset_form = PasswordResetForm()
    context = {"password_reset_form": password_reset_form}
    return render(request=request, template_name="registration/password/password_reset.html", context=context)


def forgot_password_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = CustomUser.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Solicitação de alteração de senha"
                    email_template = "registration/forgot_password/password_reset_email.txt"

                    context = {
                        "email": user.email,
                        'domain': 'comunidaderp.com.br',
                        'site_name': 'CRP',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user.first_name,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                    }
                    html_content = render_to_string(email_template, context=context)
                    text_content = strip_tags(html_content)

                    email = EmailMultiAlternatives(
                        subject,
                        text_content,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[user.email]
                    )
                    email.attach_alternative(html_content, 'text/html')

                    try:
                        send_mail(subject, text_content, 'Troca de senha', [user.email])
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/forgot_password_reset/done/")
    password_change_form = PasswordResetForm()
    context = {"password_change_form": password_change_form}
    return render(request=request, template_name="registration/forgot_password/password_change_form.html", context=context)
