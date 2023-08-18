from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
# Create your models here.
TYPE_OF_EVENT =[
    ('GM','Gaming'),
    ('NR','Normal')
]

TYPE_OF_PROFILE=[
    ('HS', 'Host'),
    ('NR', 'Normal')
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100,default=" ")
    type_of = models.CharField(max_length=2, choices=TYPE_OF_PROFILE,default='NR')
    dp = models.ImageField(upload_to= 'dp', default = 'avatar_obrx70.png')
    phone = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    # forget_password_token = models.CharField(max_length=100, blank=True, null=True)
    # news_letter_subbed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)

# class Participant(models.Model):
#     prof = models.OneToOneField(Profile, on_delete = models.CASCADE)
#     def __str__(self):
#         return str(self.prof.user.username)
class EventGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ImageField(upload_to = 'group_posters', default ='groupbanner_hsmr6h.png')
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    restricted = models.BooleanField(default =False)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=400)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    description = models.TextField(blank=True, null= True)
    poster = models.ImageField(upload_to= 'posters',default = 'poster_h9wa8t.png')
    rules = models.TextField(blank=True, null=True)
    type_of = models.CharField(max_length=2, choices=TYPE_OF_EVENT,default='NR')
    host = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(EventGroup, on_delete=models.CASCADE, null=True, blank=True)
    no_of_participants  = models.IntegerField(default=0, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(Profile, related_name="participants")
    status = models.BooleanField(default=True)
    restricted = models.BooleanField(default=False)
    result_out = models.BooleanField(default=False)
    def __str__(self):
        return str(self.title) + ' from ' + str(self.host)



class Tag(models.Model):
    name = models.CharField(max_length=20)
    event = models.ManyToManyField(Event)
    def __str__(self):
        return str(self.name) 


class WinningPosition(models.Model):
    position_name = models.CharField(max_length=100)
    event_of = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    prof = models.ManyToManyField(Profile)
    def __str__(self):
        return str(self.prof) + ' won ' + str(self.position_name)



# form design


class FormParent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_obj = models.OneToOneField(Event, on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    accept_responses = models.BooleanField(default=True)
    banner_img = models.ImageField(upload_to = 'banners', default='banner_iwdwal.png', blank=True, null=True)

    def __str__(self):
        return self.title


class FormDesign(models.Model):
    label= models.TextField()
    form_parent = models.ForeignKey(FormParent, on_delete=models.CASCADE)
    character_field = models.BooleanField(default = False)
    big_text_field = models.BooleanField(default = False)
    integer_field = models.BooleanField(default = False)
    file_field = models.BooleanField(default = False)
    mcq_field = models.BooleanField(default = False)
    def __str__(self):
        return self.form_parent.title





class FormObject(models.Model):
    form_parent = models.ForeignKey(FormParent, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.form_parent.title 

    
class FormCharacterField(models.Model):
    label_name = models.TextField(blank=True)
    field_data = models.CharField(max_length=400)
    form_object = models.ForeignKey(FormObject, on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    type_of = models.CharField(max_length=30, default="char")

    def __str__(self):
        return self.form_object.form_parent.title

class FormBigTextField(models.Model):
    label_name = models.TextField(blank=True)
    field_data = models.TextField()
    form_object = models.ForeignKey(FormObject, on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    type_of = models.CharField(max_length=30, default="txt")
    def __str__(self):
        return self.form_object.form_parent.title


class FormIntegerField(models.Model):
    label_name = models.TextField(blank=True)
    field_data = models.BigIntegerField()
    form_object = models.ForeignKey(FormObject, on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    type_of = models.CharField(max_length=30, default="int")
    def __str__(self):
        return self.form_object.form_parent.title

class FormFileField(models.Model):
    label_name = models.TextField( blank=True)
    field_data = models.FileField(upload_to='fileData')
    form_object = models.ForeignKey(FormObject, on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    type_of = models.CharField(max_length=30, default="file")
    def __str__(self):
        return self.form_object.form_parent.title





class MCQField(models.Model):
    label_name = models.TextField(blank=True)
    field_data = models.IntegerField()
    form_object = models.ForeignKey(FormObject, on_delete= models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    type_of = models.CharField(max_length=30, default="Single")
    form_design = models.ForeignKey(FormDesign, on_delete=models.CASCADE)
    def __str__(self):
        return self.form_object.form_parent.title

class Choice(models.Model):
    name = models.CharField(max_length=100)
    mcq_parent = models.ForeignKey(FormDesign, on_delete= models.CASCADE)
    def __str__(self):
        return self.name



class NewsLetter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return str(self.email)



# chat system
class ChatRoom(models.Model):
    event = models.OneToOneField(Event,on_delete= models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event.title


class Chat(models.Model):
    author = models.ForeignKey(Profile, on_delete= models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    chat_room = models.ForeignKey(ChatRoom, on_delete= models.CASCADE)

    def __str__(self):
        return self.body + " from " + str(self.author.user.username)




class Feedback(models.Model):
    prof = models.ForeignKey(Profile, on_delete= models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete= models.CASCADE)

    def __str__(self):
        return "Feedback from " + str(self.prof.user.username) + " of " + str(self.event.title)
