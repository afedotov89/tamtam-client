# tamtam_client.ChatsApi

All URIs are relative to *https://botapi.tamtam.chat*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members**](ChatsApi.md#add_members) | **POST** /chats/{chatId}/members | Add members
[**edit_chat**](ChatsApi.md#edit_chat) | **PATCH** /chats/{chatId} | Edit chat info
[**get_chat**](ChatsApi.md#get_chat) | **GET** /chats/{chatId} | Get chat
[**get_chats**](ChatsApi.md#get_chats) | **GET** /chats | Get all chats
[**get_members**](ChatsApi.md#get_members) | **GET** /chats/{chatId}/members | Get members
[**get_membership**](ChatsApi.md#get_membership) | **GET** /chats/{chatId}/members/me | Get chat membership
[**leave_chat**](ChatsApi.md#leave_chat) | **DELETE** /chats/{chatId}/members/me | Leave chat
[**remove_member**](ChatsApi.md#remove_member) | **DELETE** /chats/{chatId}/members | Remove member
[**send_action**](ChatsApi.md#send_action) | **POST** /chats/{chatId}/actions | Send action

# **add_members**
> SimpleQueryResult add_members(body, chat_id)

Add members

Adds members to chat. Additional permissions may require.

### Example
```python
from __future__ import print_function
import time
import tamtam_client
from tamtam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.ChatsApi(tamtam_client.ApiClient(configuration))
body = tamtam_client.UserIdsList() # UserIdsList | 
chat_id = 789 # int | Chat identifier

try:
    # Add members
    api_response = api_instance.add_members(body, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->add_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserIdsList**](UserIdsList.md)|  | 
 **chat_id** | **int**| Chat identifier | 

### Return type

[**SimpleQueryResult**](SimpleQueryResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_chat**
> Chat edit_chat(body, chat_id)

Edit chat info

Edits chat info: title, icon, etc…

### Example
```python
from __future__ import print_function
import time
import tamtam_client
from tamtam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.ChatsApi(tamtam_client.ApiClient(configuration))
body = tamtam_client.ChatPatch() # ChatPatch | 
chat_id = 789 # int | Chat identifier

try:
    # Edit chat info
    api_response = api_instance.edit_chat(body, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->edit_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChatPatch**](ChatPatch.md)|  | 
 **chat_id** | **int**| Chat identifier | 

### Return type

[**Chat**](Chat.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat**
> Chat get_chat(chat_id)

Get chat

Returns info about chat.

### Example
```python
from __future__ import print_function
import time
import tamtam_client
from tamtam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.ChatsApi(tamtam_client.ApiClient(configuration))
chat_id = 789 # int | Requested chat identifier

try:
    # Get chat
    api_response = api_instance.get_chat(chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->get_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **int**| Requested chat identifier | 

### Return type

[**Chat**](Chat.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chats**
> ChatList get_chats(count=count, marker=marker)

Get all chats

Returns information about chats that bot participated in: a result list and marker points to the next page

### Example
```python
from __future__ import print_function
import time
import tamtam_client
from tamtam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.ChatsApi(tamtam_client.ApiClient(configuration))
count = 56 # int | Number of chats requested (optional)
marker = tamtam_client.Bigint() # Bigint | Points to next data page. `null` for the first page (optional)

try:
    # Get all chats
    api_response = api_instance.get_chats(count=count, marker=marker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->get_chats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of chats requested | [optional] 
 **marker** | [**Bigint**](.md)| Points to next data page. &#x60;null&#x60; for the first page | [optional] 

### Return type

[**ChatList**](ChatList.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members**
> ChatMembersList get_members(chat_id, user_ids=user_ids, marker=marker, count=count)

Get members

Returns users participated in chat.

### Example
```python
from __future__ import print_function
import time
import tamtam_client
from tamtam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.ChatsApi(tamtam_client.ApiClient(configuration))
chat_id = 789 # int | Chat identifier
user_ids = [56] # list[int] | *Since* version [0.1.4](#section/About/Changelog).  Comma-separated list of users identifiers to get their membership. When this parameter is passed, both `count` and `marker` are ignored (optional)
marker = 789 # int | Marker (optional)
count = 56 # int | Count (optional)

try:
    # Get members
    api_response = api_instance.get_members(chat_id, user_ids=user_ids, marker=marker, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->get_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **int**| Chat identifier | 
 **user_ids** | [**list[int]**](int.md)| *Since* version [0.1.4](#section/About/Changelog).  Comma-separated list of users identifiers to get their membership. When this parameter is passed, both &#x60;count&#x60; and &#x60;marker&#x60; are ignored | [optional] 
 **marker** | **int**| Marker | [optional] 
 **count** | **int**| Count | [optional] 

### Return type

[**ChatMembersList**](ChatMembersList.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership**
> ChatMember get_membership(chat_id)

Get chat membership

Returns chat membership info for current bot

### Example
```python
from __future__ import print_function
import time
import tamtam_client
from tamtam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.ChatsApi(tamtam_client.ApiClient(configuration))
chat_id = 789 # int | Chat identifier

try:
    # Get chat membership
    api_response = api_instance.get_membership(chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->get_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **int**| Chat identifier | 

### Return type

[**ChatMember**](ChatMember.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_chat**
> SimpleQueryResult leave_chat(chat_id)

Leave chat

Removes bot from chat members.

### Example
```python
from __future__ import print_function
import time
import tamtam_client
from tamtam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.ChatsApi(tamtam_client.ApiClient(configuration))
chat_id = 789 # int | Chat identifier

try:
    # Leave chat
    api_response = api_instance.leave_chat(chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->leave_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **int**| Chat identifier | 

### Return type

[**SimpleQueryResult**](SimpleQueryResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member**
> SimpleQueryResult remove_member(chat_id, user_id)

Remove member

Removes member from chat. Additional permissions may require.

### Example
```python
from __future__ import print_function
import time
import tamtam_client
from tamtam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.ChatsApi(tamtam_client.ApiClient(configuration))
chat_id = 789 # int | Chat identifier
user_id = 789 # int | User id to remove from chat

try:
    # Remove member
    api_response = api_instance.remove_member(chat_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->remove_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **int**| Chat identifier | 
 **user_id** | **int**| User id to remove from chat | 

### Return type

[**SimpleQueryResult**](SimpleQueryResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_action**
> SimpleQueryResult send_action(body, chat_id)

Send action

Send bot action to chat

### Example
```python
from __future__ import print_function
import time
import tamtam_client
from tamtam_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.ChatsApi(tamtam_client.ApiClient(configuration))
body = tamtam_client.ActionRequestBody() # ActionRequestBody | 
chat_id = 789 # int | Chat identifier

try:
    # Send action
    api_response = api_instance.send_action(body, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatsApi->send_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActionRequestBody**](ActionRequestBody.md)|  | 
 **chat_id** | **int**| Chat identifier | 

### Return type

[**SimpleQueryResult**](SimpleQueryResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

