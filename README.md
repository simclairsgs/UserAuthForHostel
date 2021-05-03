> # UserAuthForHostel


>Biometric User Authentication System for Workplaces using Android and Django Rest API.
>This is the Django Backend repository, corresponding android application repository is given here.
><http://github.com/simclairsgs>
 
 
 
> # How to use ?
>
> - After the user account is created from django admin and the user can install the android app and login using the OTP provided by the admin.
> - Once logged in , the user cant logout(This is for security reasons), the application will get userdata and authentication status and display it in the app.
> - The system will not allow the user to authenticate, if the authentication slot isn't open(eg.9am-9.30am slot for workplaces, it can also be changed from backend), or the user is already authenticated,
> - The user can authenticate in the authentication time slot with th ebiometric prompt from the android device.
> - After the end of each day (12am- This can be modified - a report will be generated and stored as a csv file)
> - **Note: The user and server should be connected to the same authentication network**



> # How to install and run ?
> - Download or clone the repository
> - Install python3 from <https://python.org> with pip
> - Open terminal/command prompt, go to the repository location using cd commmand.
> - Execute the following commands
> - Create virtual environment and activate it.(optional)
> - `pip install -r requirements.txt`
> - `django-admin createsuper user`
> - `python manage.py makemigrations`
> - `python manage.py migrate`
> - `python manage.py runserver`
> 
>
>
> - Refer Django documentation for more info <https://docs.djangoproject.com/>
> - Make sure to open the required ports(default port:8000) to access it from the network.
> - Login to django-admin console from browser and create user accounts.
> - Set report generation time and authentication time slot from .
