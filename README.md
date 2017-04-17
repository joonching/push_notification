# Push Notification
This is my Push Notification portion for final project in ECE 4574 at Virginia Tech

### What is this repository for? ###

* Provides an Android studio project that can be used to create a virtual android phone/tablet
* Provides the tests for the push_notifications.

## Prerequisites to Run ##
* Android Studio
* Your device is connected to the internet (to clone the repository and download required libraries)

## How to run the test ##
1. go ahead and gitclone this repo
`git clone https://github.com/joonching/push_notification.git`
2. Run the python script *send.py*
`Python3 send.py {api_key} {registration_id}`

## Image of Test + Virtual Phone ##
<img src='http://i.imgur.com/DVQKv4Q.png' title='test image' width='' alt='test image' />


## Notes ##
The {api_key} and {registration_id} is provided with a word documented.
The {registration_id} is currently the id for my virtual android device. 
When the application gets fully implemented then the registration_id will start to change or get added to.

If you want to see the actual application on a phone then you would have to run the Android Studio project and run the virtual phone
As of now the test is getting run to my current Firebase cloud messaging server that reroutes the messages to my virtual phone. 

### Authors ###

* Joshua Chung
