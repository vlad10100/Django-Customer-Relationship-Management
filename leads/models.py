from django.db import models

from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractUser


# Modifying the AbstractUser and adding BooleanFields
class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    
# UserProfile == User, just to make a separate and not to interchange
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Lead Model, can only have one agent, organization must be the same with agent.organization
class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey('Agent',null=True, blank=True, on_delete=models.SET_NULL)

    category = models.ForeignKey('Category', related_name='leads', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




# Agent Model, can only choose one organization, organization can have many agents.
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Another functionality that I don't fully understand. HAHA
class Category(models.Model): # Recently added, Contacted, Converted, Unconverted
    name = models.CharField(max_length=30)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.name






#SIGNALS - pre_init, post_init, pre_save, pre_post, etc,. 
# Whenever a user is created, automatically, a USERPROFILE will be created. 
def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created) 
    # instance = actual instance being saved
    # created = Boolean, if a new record is created

    if created:
        UserProfile.objects.create(user=instance)

# .connect() - connect to the database
post_save.connect(post_user_created_signal, sender=User)