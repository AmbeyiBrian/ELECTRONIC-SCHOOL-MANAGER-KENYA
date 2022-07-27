from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class accountsManager(BaseUserManager):
    def create_superuser(self, first_name, last_name, email_address, phone_number, national_id, gender,
                         user_class='Administrator', password=None):
        if not email_address:
            raise ValueError("User must have a valid email address")

        user = self.model(email_address=self.normalize_email(email_address), first_name=first_name, last_name=last_name,
                          phone_number=phone_number, national_id=national_id, gender=gender, user_class=user_class)
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(self._db)
        return user

    def create_user(self, first_name, last_name, email_address, phone_number, national_id, gender, user_class,
                    profile_photo):
        user = Users(first_name=first_name, last_name=last_name, email_address=email_address, phone_number=phone_number,
                     national_id=national_id, gender=gender, user_class=user_class, profile_photo=profile_photo)


class Users(AbstractBaseUser):
    first_name = models.CharField(max_length=50, verbose_name='FirstName')
    last_name = models.CharField(max_length=50, verbose_name='LastName')
    email_address = models.EmailField(max_length=50, unique=True, primary_key=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female')])
    user_class = models.CharField(max_length=50, choices=[('Principal', 'Principal'), ('Teacher', 'Teacher'),
                                                          ('Parent', 'Parent'), ('Sub staff', 'Sub staff')])
    profile_photo = models.FileField(upload_to='profile_photos', null=True)
    date_joined = models.DateTimeField(verbose_name='Date joined', auto_now=True)
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = accountsManager()

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'national_id', 'gender']

    def __str__(self):
        return self.email_address

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lebel):
        return True

    class Meta:
        verbose_name_plural = 'Users'
