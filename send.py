'''
import urllib.request
import json
import sys
#MY_API_KEY="AIzaSyBM1ZW9JwSxiJ2SWIznWuCM2yYVQ8zXJNM"
MY_API_KEY="AIzaSyDfdSI8jk-Bsv2GIIA_YRG0ZcQjjAhvq9o"
messageTitle = sys.argv[1]
messageBody = sys.argv[2]
data={
    "to" : "/topics/my_little_topic",
    "notification" : {
        "body" : messageBody,
        "title" : messageTitle,
        "icon" : "ic_face_black_48dp"
    }
}

dataAsJSON = json.dumps(data)
ret = urllib.request.Request(
    "https://gcm-http.googleapis.com/gcm/send",
    dataAsJSON.encode("utf-8"),
    { "Authorization" : "key="+MY_API_KEY,
      "Content-type" : "application/json"
    }
)
#urllib.request.urlopen(ret)
print(urllib.request.urlopen(ret).read())
'''
import sys
from pyfcm import FCMNotification
import datetime
api_key = sys.argv[1]
registration_id = sys.argv[2]
reg_id = sys.argv[3]
reg_ids = [sys.argv[2], sys.argv[3]]
push_service = FCMNotification(api_key=api_key)

# OR initialize with proxies

proxy_dict = {
          "http"  : "http://127.0.0.1",
          "https" : "http://127.0.0.1",
        }
push_service = FCMNotification(api_key=api_key)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

message_title = "Hello"
message_body = "World"
message_title_n = 654321
message_body_n = 123456
passed_test = 0
failed_test = 0
total_test_time = 0
special_chars = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
total_push = 0
errors = []
#result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

print()
print("**TEST START**")
print()

print("Single text Title and Body to Single Phone")

a = datetime.datetime.now()
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
try: 
	assert result['success'] == 1
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	total_push = total_push + 1
	passed_test = passed_test + 1;
except AssertionError:
	failed_test = failed_test + 1
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
print()

print("Single text Title and Body to Multiple Phones")

a = datetime.datetime.now()
result = push_service.notify_multiple_devices(registration_ids=reg_ids, message_title=message_title, message_body=message_body)
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
try: 
	assert result[0]['success'] == 2
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	total_push = total_push + 1
	passed_test = passed_test + 1;
except AssertionError:
	failed_test = failed_test + 1
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
print()

print("Null text Title and Body to Single Phone")

a = datetime.datetime.now()
result = push_service.notify_single_device(registration_id=registration_id, message_title="\0", message_body="\0")
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
try: 
	assert result['success'] == 1
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	total_push = total_push + 1
	passed_test = passed_test + 1;
except AssertionError:
	failed_test = failed_test + 1
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
print()

print("Null text Title and Body to Multiple Phones")

a = datetime.datetime.now()
result = push_service.notify_multiple_devices(registration_ids=reg_ids, message_title="\0", message_body="\0")
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
try: 
	assert result[0]['success'] == 2
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	total_push = total_push + 1
	passed_test = passed_test + 1;
except AssertionError:
	failed_test = failed_test + 1
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
print()


print("Multiple text Title and Body to Single Phone")

a = datetime.datetime.now()
failure_bool = 0
for num in range(0,20):
	result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
	try: 
		assert result['success'] == 1
		total_push = total_push + 1
	except AssertionError:
		failure_bool = 1
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
if failure_bool == 1:
	failed_test = failed_test + 1;
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
else:
	passed_test = passed_test + 1;
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	print()


print("Multiple text Title and Body to Multiple Phones")

a = datetime.datetime.now()
failure_bool = 0
for num in range(0,20):
	result = push_service.notify_multiple_devices(registration_ids=reg_ids, message_title=message_title, message_body=message_body)
	try: 
		assert result[0]['success'] == 2
		total_push = total_push + 1
	except AssertionError:
		failure_bool = 1
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
if failure_bool == 1:
	failed_test = failed_test + 1;
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
else:
	passed_test = passed_test + 1;
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	print()


print("Single number Title and Body")

a = datetime.datetime.now()
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title_n, message_body=message_body_n)
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
try: 
	assert result['success'] == 1
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	total_push = total_push + 1
	passed_test = passed_test + 1;
except AssertionError:
	failed_test = failed_test + 1
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
print()


print("Multiple number Title and Body")

a = datetime.datetime.now()
failure_bool = 0
for num in range(0,20):
	result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title_n, message_body=message_body_n)
	try: 
		assert result['success'] == 1
		total_push = total_push + 1
	except AssertionError:
		failure_bool = 1
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
if failure_bool == 1:
	failed_test = failed_test + 1;
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
else:
	passed_test = passed_test + 1;
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	print()


print("Send Long random string")

long_title = "gYnwCQ0lK7Hv1EDEe1jWhl0RD7lcpEx6MEzP4QAMdYkiXUBSwgFmtO0PuHR5gDo4takBickz5RjaEFn1aGLOXsewQoEoTQvXQp3QKFbKp6Yw43e7LM2frJgJl5ejp6IHMHGDd3ABBtipIl6ZlNooUH3WA5Z69q0B6JYsHyniuZMFX7MziNMrn7iVTUV5qTO5romOIamDzMxT2ynDzqfAdlObgcU8R92Y6RaumlY6tH24jfl2reGnpIYKpOtFkXJh65r3Rg4wmPQlTR3JfppBciq5nxQC0rXFhKStdYNBxpfkcXkpOzr9vpuhBklJafOUEdrbneIiLppVWwIzqTTczR9yXdcyV5vLqwQ97nyfaSydYmDKodOHNymxP1okpoSaFE4hllhuQxkhb8npsHSpFmltkR8rnSNtoCkage3LXj29yjDxIwoC4aKnSmSHoxbWPVMDNkisV6AvsURnsWZWW2tIsMhdz8neVBuqzybSpfRAaPQ9RKwb"
long_message = "abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
a = datetime.datetime.now()
result = push_service.notify_single_device(registration_id=registration_id, message_title=long_title, message_body=long_message)
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
try: 
	assert result['success'] == 1
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	total_push = total_push + 1
	passed_test = passed_test + 1;
except AssertionError:
	failed_test = failed_test + 1
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
print()


print("Send Special Characters to Single Phone")

a = datetime.datetime.now()
failure_bool = 0
for num in range(len(special_chars)):
	result = push_service.notify_single_device(registration_id=registration_id, message_title=special_chars[num], message_body=special_chars[num])
	try: 
		assert result['success'] == 1
		total_push = total_push + 1
	except AssertionError:
		failure_bool = 1
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
if failure_bool == 1:
	failed_test = failed_test + 1;
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
else:
	passed_test = passed_test + 1;
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	print()

print("Send Special Characters to Multiple Phones")

a = datetime.datetime.now()
failure_bool = 0
for num in range(len(special_chars)):
	result = push_service.notify_multiple_devices(registration_ids=reg_ids, message_title=special_chars[num], message_body=special_chars[num])
	try: 
		assert result[0]['success'] == 2
		total_push = total_push + 1
	except AssertionError:
		failure_bool = 1
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
if failure_bool == 1:
	failed_test = failed_test + 1;
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
else:
	passed_test = passed_test + 1;
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	print()

print("No Registration ID - Failure Case")

a = datetime.datetime.now()
result = push_service.notify_single_device(registration_id="x", message_title=message_title_n, message_body=message_body_n)
b = datetime.datetime.now()
c = b - a
total_test_time = c.total_seconds() + total_test_time;
try: 
	assert result['success'] == 1
	print("Success, Performance Time: " + str(c.total_seconds()) + "s")
	total_push = total_push + 1
	passed_test = passed_test + 1;
except AssertionError:
	failed_test = failed_test + 1
	print("Failure, Performance Time: " + str(c.total_seconds()) + "s")
	print("**Error: " + result['results'][0]['error'] + "**")
print()



print("Total Test Time: " + str(total_test_time))
print("Total Tests Ran: 12")
print("Total Successful Push notifications sent: " + str(total_push))
print("Total Tests Passed: " + str(passed_test))
print("Total Tests Failed: " + str(failed_test))