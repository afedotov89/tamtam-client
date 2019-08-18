# swagger_client.SubscriptionsApi

All URIs are relative to *https://botapi.tamtam.chat*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscriptions**](SubscriptionsApi.md#get_subscriptions) | **GET** /subscriptions | Get subscriptions
[**get_updates**](SubscriptionsApi.md#get_updates) | **GET** /updates | Get updates
[**subscribe**](SubscriptionsApi.md#subscribe) | **POST** /subscriptions | Subscribe
[**unsubscribe**](SubscriptionsApi.md#unsubscribe) | **DELETE** /subscriptions | Unsubscribe

# **get_subscriptions**
> GetSubscriptionsResult get_subscriptions()

Get subscriptions

In case your bot gets data via WebHook, the method returns list of all subscriptions

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))

try:
    # Get subscriptions
    api_response = api_instance.get_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSubscriptionsResult**](GetSubscriptionsResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_updates**
> UpdateList get_updates(limit=limit, timeout=timeout, marker=marker, types=types)

Get updates

You can use this method for getting updates in case your bot is not subscribed to WebHook. The method is based on long polling.  Every update has its own sequence number. `marker` property in response points to the next upcoming update.  All previous updates are considered as *committed* after passing `marker` parameter. If `marker` parameter is **not passed**, your bot will get all updates happened before the last commitment.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Maximum number of updates to be retrieved (optional)
timeout = 56 # int | Timeout in seconds for long polling (optional)
marker = 789 # int | Pass `null` to get updates you didn't get yet (optional)
types = ['types_example'] # list[str] | Comma separated list of update types your bot want to receive (optional)

try:
    # Get updates
    api_response = api_instance.get_updates(limit=limit, timeout=timeout, marker=marker, types=types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_updates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of updates to be retrieved | [optional] 
 **timeout** | **int**| Timeout in seconds for long polling | [optional] 
 **marker** | **int**| Pass &#x60;null&#x60; to get updates you didn&#x27;t get yet | [optional] 
 **types** | [**list[str]**](str.md)| Comma separated list of update types your bot want to receive | [optional] 

### Return type

[**UpdateList**](UpdateList.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe**
> SimpleQueryResult subscribe(body)

Subscribe

Subscribes bot to receive updates via WebHook. After calling this method, the bot will receive notifications about new events in chat rooms at the specified URL.  Your server **must** be listening on one of the following ports: **80, 8080, 443, 8443, 16384-32383**

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SubscriptionRequestBody() # SubscriptionRequestBody | 

try:
    # Subscribe
    api_response = api_instance.subscribe(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionRequestBody**](SubscriptionRequestBody.md)|  | 

### Return type

[**SimpleQueryResult**](SimpleQueryResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe**
> SimpleQueryResult unsubscribe(url)

Unsubscribe

Unsubscribes bot from receiving updates via WebHook. After calling the method, the bot stops receiving notifications about new events. Notification via the long-poll API becomes available for the bot

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
url = 'url_example' # str | URL to remove from WebHook subscriptions

try:
    # Unsubscribe
    api_response = api_instance.unsubscribe(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->unsubscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL to remove from WebHook subscriptions | 

### Return type

[**SimpleQueryResult**](SimpleQueryResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

