'''
step1 : create django project
step2:  install mysqlclient
            ->  pip install mysqlclient
step3:   go to setting.py
            ->  DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.mysql',
                        'NAME': 'pythonDB',
                        'USER': 'root',
                        'PASSWORD': 'root',
                        'HOST': 'localhost',
                        'PORT': '3306',
                }
            }
step4:  migrate the database using the following commands
            ->  python manage.py migrate
step5:   install django-widget-tweaks in our virtual environment
            ->   pip install django-widget-tweaks
step6:  open the settings.py file and add the application to the installed apps
            ->  INSTALLED_APPS = [
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'widget_tweaks'
                ]
step7:  we'll create an admin user that will allow us to access the admin interface of our app
            ->  python manage.py createsuperuser
            ->  Provide the desired username, email and password when prompted:
            ->  Username (leave blank to use 'ahmed'): shital
                    Email address: shital@gmail.com
                    Password:
                    Password (again):
                    Superuser created successfully.
step8:  create a django application
            ->  python manage.py startapp crudapp
            ->  add it in the settings.py file
step9:  create the database model for storing empdata
            -> go to models.py of crudapp
step10: create migrations
            ->  python manage.py makemigrations
step11: migrate your database
            ->  python manage.py migrate
step12: create a form for creating a empdata
            ->  in crudapp create a forms.py
step13: we'll create the views for performing the CRUD operations
            ->  in crudapp views.py add code
step14: Open the settings.py file and add os.path.join(BASE_DIR, 'templates') to the TEMPLATES array
            ->  TEMPLATES = [
                    {
                        'BACKEND': 'django.template.backends.django.DjangoTemplates',
                        'DIRS': [os.path.join(BASE_DIR, 'templates')],
                        'APP_DIRS': True,
                        'OPTIONS': {
                            'context_processors': [
                                'django.template.context_processors.debug',
                                'django.template.context_processors.request',
                                'django.contrib.auth.context_processors.auth',
                                'django.contrib.messages.context_processors.messages',
                            ],
                        },
                    },
            ]
step15: inside the crudapp folder create a templates folder
step16:  create the urls to access our CRUD view
            ->  Go to the urls.py file and update it
step17:  Running the Local Development Server
            ->  python manage.py runserver
'''