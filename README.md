# Push Notification
This is my Push Notification portion for final project in ECE 4574 at Virginia Tech

### What is this repository for? ###

* Provides an Android studio project that can be used to create a virtual android phone/tablet
* Provides the tests for the push_notifications.

## Prerequisites to Run ##
* Android Studio
* Your device is connected to the internet (to clone the repository and download required libraries)

## Firebase Cloud Messaging Automated Testing Outputs ##
[Nexus 5](https://00e9e64bac42cda73b8f8b312788b5cd765795073a8aa76fcd-apidata.googleusercontent.com/download/storage/v1/b/test-lab-b44s4yat051uz-hckq2t4i7yd2m/o/web-build_2017-04-18T00:17:45.727Z_EIqR%2FNexus5X-25-en_US-portrait%2Fbugreport.txt?qk=AD5uMEuaJA-G0TptZ2TNWYHpnwwpkB2IAPM-ORTwhjBQn3G_1fwdpazVhFRamYuOGWU786HUT_yigqte1GLU68FDXpKYoBtldXJw6F_NSTtFkec8wiy97J4CcFBbcZikyKDQoS96oNQuUZUSfTOgExMG4bPEC9jPCQWpdvZpnvh2rBiK6Og2DdyUhOCZ7wZRtVU60VWD2VBoKtmukR0Zkc3Ki55rl0Ry7JHTaAUYudQs_O0iOC-bPypiWcbLLCkn2JQKhox98Ifz4LUVSAPvjWqjPGDlYDoQxWLQXf6jzPy4D4h-AHAN-iUmyrsnWvnK4F4gBa9HmkyorvX4gFNfFqWCE27iwa3647kTn3_Wl8BOBVP511SGtiwQWmd3jKELsRlj2KWsMINVVf4BR3Kd4OB9kKPalWb5CGuql0NhYJ4ls20sT8e61ErRopcjyS-8SqBcPXFNk8aF-8We7d_RWEw0Qf9KhQiyUwhuiqcaoVBrsw9zqQi8kd5P4OXVWhb5ss5-F_ccpDeE-bYwerltal9uR8Fi8zpYAIVLISrL2NRTyw33CdBTigD7CeGyTybwd7CIDLSJYuvTkhKBMIctFmVNV_LMM3TRaN9T35HFi6GLU_otyurvT2LrXx4PhZeCEafiQmuvBhyzPoWFONeMFgrX5hnDhRMzLqsnbXQGzBMHxieFD1fnoOI8owPIHL-phaHT70-PxXc7LLAWye12wDBx6YhykQiq6Pq7UDYel8GnDBdXtGLlknJUhQb7mR79DnvErcWVfgzmVI3PKEFrcwpQEpob2C3yZHo0RZvSgfNBlRhbLy0IvigYXJB8Mz4rVk5b3X97b-dHQLySZMaaNuf3gi-1kcbHynIkxN5xGZQjoJZQia2ksIoJw3FrZDRcz06de_plNAQm)

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


### Edits ###
1. Improved testing capability to more than one phone - therefore the image is out of date

### Authors ###

* Joshua Chung
