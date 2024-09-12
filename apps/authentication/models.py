# -*- encoding: utf-8 -*-
import logging

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(
        unique=True, max_length=255, blank=True, null=True)
    first_name = models.CharField(
        max_length=255, blank=False, verbose_name="Primeiro Nome")
    last_name = models.CharField(
        max_length=255, blank=False, verbose_name="Ultimo Nome")

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "username"]

    def save(self, *args, **kwargs):
        password = self._password
        if not self.username:
            self.username = self.email

        super().save(*args, **kwargs)

        if self.email and password:

            assunto = 'Cadastro realizado com sucesso!'
            mensagem = render_to_string('registration/password/password_reset_email.html', {
                'password': password,
                'username': self.username,
                'first_name': self.first_name
            })

            remetente = 'comunidadecrp@gmail.com'
            destinatarios = [self.email]

            try:
                logging.info('Enviando Email...')
                send_mail(assunto, '', remetente,
                          destinatarios, html_message=mensagem)
                logging.info('Email Enviado com sucesso!')
            except Exception as e:
                logging.error('Erro ao enviar o email: %s', str(e))

    def __str__(self):
        return self.first_name


