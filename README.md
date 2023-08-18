<p align="center">
     <img src="https://i.imgur.com/j4ffLKS.png" width="280px" height="100px"/>
   
</p>


#ppt

https://www.canva.com/design/DAEsgW0gjvw/GICjGuS7YgZYH7kTmsGPMg/edit


# Intro video:

https://user-images.githubusercontent.com/65186501/137447170-cd5e8175-0424-45d4-b0d1-83bf48cce888.mp4



    


# EventDesk

EventDesk is a platform for effectively organizing and Hosting events with just a few clicks.
We can hold multiple events simultaneously, with proper Privacy and Security.
The User Interface makes it easy for both the organizers and participants to properly access the website and hence the events are held smoothly. 


To make things better, there is a section for Winner Declaration, where the host can send personalized emails and goodies (if required) to the winners. 
The website also acts as a reminder for upcoming events through its eye catching posters & banners, speaking of which we have developed our own notification system, subscribing to which, the participants will get notified about upcoming events via the email address provided by them. Our support system is fast and reliable, our team will assist you with utmost priority.
It is the simplest gateway to connect Organizers and Participants.






<!-- to know more visit website: http://event-desk.herokuapp.com/ -->
## Features

#### Host POV

- Make an account, login
- Host events
- Set timing, specifications
- Generate dynamic forms
- Get responses
- Declare winner
- Send notifications


#### Partcipant POV
- Participate in events
- Fill form
- Win events
- Get ranked in leaderboard
- Get all the notifications through newsletter





## API Reference

#### For the API access you need to have auth token which is only generated for admin users . You have to signup to the website and contact our team for the admin access , after that you can generate valid auth token for API requests 


#### Get Authorization Token

```http
  POST /api/auth-token
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. your username |
| `password` | `string` | **Required**. Your password|



#### Get all events

```http
  GET /api/events-list
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `auth token` | `string` | **Required**. Your Auth token in header |

#### Get event groups

```http
  GET /api/group-list
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `auth token`      | `string` | **Required**. Your auth token in header|



  




  
## Run Locally

- Clone the project

```bash
  git clone https://github.com/GrowerLabs/EventDesk.git
```


- Make virtualenv

```bash
  python -m virtualenv [env name]
```
- Activate virtualenv

```bash
  . [env name]/Scripts/activate
```
- Locate to core directory
```bash
  cd core
```

- Install dependencies

```bash
  pip install -r requirements.txt
```


- Runserver

```bash
  python manage.py runserver
```




  
## Tech Stack


**Frontend** Bootstrap, CSS, Javascript

**Backend:** django, Python, Javascript


  
## Feedback

If you have any feedback, please reach out to us at growerlabs@gmail.com

  
## From :


![Logo](https://i.imgur.com/tb24D9K.jpg)
  
