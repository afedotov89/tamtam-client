# swagger_client.MessagesApi

All URIs are relative to *https://botapi.tamtam.chat*

Method | HTTP request | Description
------------- | ------------- | -------------
[**answer_on_callback**](MessagesApi.md#answer_on_callback) | **POST** /answers | Answer on callback
[**delete_message**](MessagesApi.md#delete_message) | **DELETE** /messages | Delete message
[**edit_message**](MessagesApi.md#edit_message) | **PUT** /messages | Edit message
[**get_messages**](MessagesApi.md#get_messages) | **GET** /messages | Get messages
[**send_message**](MessagesApi.md#send_message) | **POST** /messages | Send message

# **answer_on_callback**
> SimpleQueryResult answer_on_callback(body, callback_id)

Answer on callback

This method should be called to send an answer after a user has clicked the button. The answer may be an updated message or/and a one-time user notification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CallbackAnswer() # CallbackAnswer | 
callback_id = 'callback_id_example' # str | Identifies a button clicked by user. Bot receives this identifier after user pressed button as part of `MessageCallbackUpdate`

try:
    # Answer on callback
    api_response = api_instance.answer_on_callback(body, callback_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->answer_on_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CallbackAnswer**](CallbackAnswer.md)|  | 
 **callback_id** | **str**| Identifies a button clicked by user. Bot receives this identifier after user pressed button as part of &#x60;MessageCallbackUpdate&#x60; | 

### Return type

[**SimpleQueryResult**](SimpleQueryResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message**
> SimpleQueryResult delete_message(message_id)

Delete message

Deletes message in a dialog or in a chat if bot has permission to delete messages.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
message_id = 'message_id_example' # str | Deleting message identifier

try:
    # Delete message
    api_response = api_instance.delete_message(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->delete_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**| Deleting message identifier | 

### Return type

[**SimpleQueryResult**](SimpleQueryResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_message**
> SimpleQueryResult edit_message(body, message_id)

Edit message

Updated message should be sent as `NewMessageBody` in a request body. In case `attachments` field is `null`, the current message attachments won’t be changed. In case of sending an empty list in this field, all attachments will be deleted.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewMessageBody() # NewMessageBody | 
message_id = 'message_id_example' # str | Editing message identifier

try:
    # Edit message
    api_response = api_instance.edit_message(body, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->edit_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewMessageBody**](NewMessageBody.md)|  | 
 **message_id** | **str**| Editing message identifier | 

### Return type

[**SimpleQueryResult**](SimpleQueryResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> MessageList get_messages(chat_id=chat_id, message_ids=message_ids, _from=_from, to=to, count=count)

Get messages

Returns messages in chat: result page and marker referencing to the next page. Messages traversed in reverse direction so the latest message in chat will be first in result array. Therefore if you use `from` and `to` parameters, `to` must be **less than** `from`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
chat_id = swagger_client.Bigint() # Bigint | Chat identifier to get messages in chat (optional)
message_ids = ['message_ids_example'] # list[str] | Messages ids you want to get (optional)
_from = swagger_client.Bigint() # Bigint | Start time for requested messages (optional)
to = swagger_client.Bigint() # Bigint | End time for requested messages (optional)
count = 56 # int | Maximum amount of messages in response (optional)

try:
    # Get messages
    api_response = api_instance.get_messages(chat_id=chat_id, message_ids=message_ids, _from=_from, to=to, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | [**Bigint**](.md)| Chat identifier to get messages in chat | [optional] 
 **message_ids** | [**list[str]**](str.md)| Messages ids you want to get | [optional] 
 **_from** | [**Bigint**](.md)| Start time for requested messages | [optional] 
 **to** | [**Bigint**](.md)| End time for requested messages | [optional] 
 **count** | **int**| Maximum amount of messages in response | [optional] 

### Return type

[**MessageList**](MessageList.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> SendMessageResult send_message(body, user_id=user_id, chat_id=chat_id)

Send message

Sends a message to a chat. As a result for this method new message identifier returns. ### Attaching media Attaching media to messages is a three-step process.  At first step, you should [obtain a URL to upload](#operation/getUploadUrl) your media files.  At the second, you should upload binary of appropriate format to URL you obtained at the previous step. See [upload](https://dev.tamtam.chat/#operation/getUploadUrl) section for details.  Finally, if the upload process was successful, you will receive JSON-object in a response body.  Use this object to create attachment. Construct an object with two properties: - `type` with the value set to appropriate media type - and `payload` filled with the JSON you've got.  For example, you can attach a video to message this way:  1. Get URL to upload. Execute following: ```shell curl -X POST 'https://botapi.tamtam.chat/uploads?access_token=%access_token%&type=video' ``` As the result it will return URL for the next step. ```json {     \"url\": \"http://vu.mycdn.me/upload.do…\" } ```  2. Use this url to upload your binary: ```shell curl -i -X POST   -H \"Content-Type: multipart/form-data\"   -F \"data=@movie.mp4\" \"http://vu.mycdn.me/upload.do…\" ``` As the result it will return JSON you can attach to message: ```json   {     \"token\": \"_3Rarhcf1PtlMXy8jpgie8Ai_KARnVFYNQTtmIRWNh4\"   } ``` 3. Send message with attach: ```json {     \"text\": \"Message with video\",     \"attachments\": [         {             \"type\": \"video\",             \"payload\": {                 \"token\": \"_3Rarhcf1PtlMXy8jpgie8Ai_KARnVFYNQTtmIRWNh4\"             }         }     ] } ```  **Important notice**:  It may take time for the server to process your file (audio/video or any binary). While a file is not processed you can't attach it. It means the last step will fail with `400` error. Try to send a message again until you'll get a successful result.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = swagger_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NewMessageBody() # NewMessageBody | 
user_id = 789 # int | Fill this parameter if you want to send message to user (optional)
chat_id = 789 # int | Fill this if you send message to chat (optional)

try:
    # Send message
    api_response = api_instance.send_message(body, user_id=user_id, chat_id=chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewMessageBody**](NewMessageBody.md)|  | 
 **user_id** | **int**| Fill this parameter if you want to send message to user | [optional] 
 **chat_id** | **int**| Fill this if you send message to chat | [optional] 

### Return type

[**SendMessageResult**](SendMessageResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

