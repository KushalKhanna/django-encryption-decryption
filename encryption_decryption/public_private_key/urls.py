from django.conf.urls import url
from public_private_key import views

urlpatterns = [
    url("home/", views.home, name="home"),
    url("get-public-key", views.get_public_key, name="get_public_key"),
    url("encrypted", views.encrypted_text, name="encryption"),
    url("generate-keys", views.generate_keys, name="generateKeys"),
    url("decrypted", views.decrypted_text, name="decryption"),
]
