from django.conf.urls import url
from use_encryption_decryption import views

urlpatterns = [
    url('generate-secret-key/', views.generate_secret_key, name="generate_secret_key"),
    url('encrypting-file/', views.encrypting_file, name="encrypting_file"),
    url('decrypting-file/', views.decrypting_file, name="decrypting_file"),
]
