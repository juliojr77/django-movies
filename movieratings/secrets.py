# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@r&!m56@=__$s%46c-og6^c2=0dmqk!5amz!8pc#6+schq%_f!'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movies',
        'USER': 'Pipita',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
