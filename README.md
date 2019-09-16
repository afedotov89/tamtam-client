# swagger-client
## About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API.  
## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future.  
## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel  
## @PrimeBot [PrimeBot](https://tt.me/primebot) is the main bot in TamTam, all bots creator. Use PrimeBot to create and edit your bots. Feel free to contact us for any questions, [@support](https://tt.me/support) or [team@tamtam.chat](mailto:team@tamtam.chat).  
#### [PrimeBot](https://tt.me/primebot) commands: `/start` &mdash; start a dialog with a bot  `/create` &mdash; create a bot, assign the unique short name to it (from 4 to 64 characters)  `/set_name [name]` &mdash; assign a short or full name to the bot (up to 200 characters)  `/set_description [description]` &mdash; enter the description for the bot profile (up to 400 characters)  `/set_picture [URL]` &mdash; enter the URL of bot's picture  `/delete [username]` &mdash; delete the bot  `/list` &mdash; show the list of all bots  `/get_token` &mdash; obtain a token for a bot  `/revoke` &mdash; request a new token  `/help` &mdash; help  
## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources  ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method is not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  
## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. 
## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:  `code` - the string with the error key   `message` - a string describing the error </br>  For example: 
```bash 
> http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} 
HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json;
charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; 
Domain = .tamtam.chat; 
Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } 
``` 
## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates.  
## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:   `callback` &mdash; sends a notification to a bot (via WebHook or long polling)  `link` &mdash; makes a user to follow a link  `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)  You may also send a message with an [InlineKeyboard]() type attachment to start creating buttons. When the user presses a button, the bot receives the answer with filled callback field. It is recommended to edit that message so the user can receive updated buttons.  
# Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request.  
# Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier.  
# Changelog 
##### Version 0.1.8 - Added `code`, `width`, `height` to [StickerAttachment](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1580) - `token` is now only one required property for video/audio/file attachments - `sender` and `chat_id` of [LinkedMessage](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1401) are now optional - Added clarifying `message` to [SimpleQueryResult](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1938)  
##### Version 0.1.7 - It is now **required** to pass `marker` parameter in [/updates](#operation/getUpdates) requests, except initial  - Added full `User` object to update types: bot_started, bot_added, bot_removed, user_added, user_removed, chat_title_changed - Added `size` and `filename` to [`FileAttachment`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1503) - Added [`token`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1525) property to video/audio/file attachments allows you to reuse attachments uploaded by another user  
##### Version 0.1.6 - Added method to [edit bot info](#operation/editMyInfo) - Added statistics for messages in channel - `Message.sender` and `UserWithPhoto.avatar_url/full_avatar_url` removed from required properties  
##### Version 0.1.5 - Added `id` property to media attachments (`VideoAttachment`, `AudioAttachment`) so you can reuse attachment from one message in another - Added ability to create *linked* message: replied or forwarded. See `link` in `NewMessageBody` - `intent` property marked as required only for `CallbackButton`  
##### Version 0.1.4 - Added `user_ids` parameter to [get members](#operation/getMembers) in chat by id - `attachment` property of [send message](#operation/sendMessage) request body marked as deprecated  
##### Version 0.1.3 - Added method to [delete](https://dev.tamtam.chat/#operation/deleteMessages) messages - Added ability to [get](https://dev.tamtam.chat/#operation/getMessages) particular messages by ID - Added `is_admin` flag to `ChatMember` - Added `message` property to `MessageCallbackUpdate` - Renamed property `message` to `body` for `Message` schema - Added reusable `token` to `PhotoAttachment`. It allows to attach the same photo more than once.  
# Authentication  <!-- ReDoc-Inject: <security-definitions> -->

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.8
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import tamtam_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tamtam_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = tamtam_client.BotsApi(tamtam_client.ApiClient(configuration))
body = tamtam_client.BotPatch() # BotPatch | 

try:
    # Edit current bot info
    api_response = api_instance.edit_my_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->edit_my_info: %s\n" % e)

# Configure API key authorization: access_token
configuration = tamtam_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'

# create an instance of the API class
api_instance = tamtam_client.BotsApi(tamtam_client.ApiClient(configuration))

try:
    # Get current bot info
    api_response = api_instance.get_my_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BotsApi->get_my_info: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://botapi.tamtam.chat*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BotsApi* | [**edit_my_info**](docs/BotsApi.md#edit_my_info) | **PATCH** /me | Edit current bot info
*BotsApi* | [**get_my_info**](docs/BotsApi.md#get_my_info) | **GET** /me | Get current bot info
*ChatsApi* | [**add_members**](docs/ChatsApi.md#add_members) | **POST** /chats/{chatId}/members | Add members
*ChatsApi* | [**edit_chat**](docs/ChatsApi.md#edit_chat) | **PATCH** /chats/{chatId} | Edit chat info
*ChatsApi* | [**get_chat**](docs/ChatsApi.md#get_chat) | **GET** /chats/{chatId} | Get chat
*ChatsApi* | [**get_chats**](docs/ChatsApi.md#get_chats) | **GET** /chats | Get all chats
*ChatsApi* | [**get_members**](docs/ChatsApi.md#get_members) | **GET** /chats/{chatId}/members | Get members
*ChatsApi* | [**get_membership**](docs/ChatsApi.md#get_membership) | **GET** /chats/{chatId}/members/me | Get chat membership
*ChatsApi* | [**leave_chat**](docs/ChatsApi.md#leave_chat) | **DELETE** /chats/{chatId}/members/me | Leave chat
*ChatsApi* | [**remove_member**](docs/ChatsApi.md#remove_member) | **DELETE** /chats/{chatId}/members | Remove member
*ChatsApi* | [**send_action**](docs/ChatsApi.md#send_action) | **POST** /chats/{chatId}/actions | Send action
*MessagesApi* | [**answer_on_callback**](docs/MessagesApi.md#answer_on_callback) | **POST** /answers | Answer on callback
*MessagesApi* | [**delete_message**](docs/MessagesApi.md#delete_message) | **DELETE** /messages | Delete message
*MessagesApi* | [**edit_message**](docs/MessagesApi.md#edit_message) | **PUT** /messages | Edit message
*MessagesApi* | [**get_messages**](docs/MessagesApi.md#get_messages) | **GET** /messages | Get messages
*MessagesApi* | [**send_message**](docs/MessagesApi.md#send_message) | **POST** /messages | Send message
*SubscriptionsApi* | [**get_subscriptions**](docs/SubscriptionsApi.md#get_subscriptions) | **GET** /subscriptions | Get subscriptions
*SubscriptionsApi* | [**get_updates**](docs/SubscriptionsApi.md#get_updates) | **GET** /updates | Get updates
*SubscriptionsApi* | [**subscribe**](docs/SubscriptionsApi.md#subscribe) | **POST** /subscriptions | Subscribe
*SubscriptionsApi* | [**unsubscribe**](docs/SubscriptionsApi.md#unsubscribe) | **DELETE** /subscriptions | Unsubscribe
*UploadApi* | [**get_upload_url**](docs/UploadApi.md#get_upload_url) | **POST** /uploads | Get upload URL

## Documentation For Models

 - [ActionRequestBody](docs/ActionRequestBody.md)
 - [Attachment](docs/Attachment.md)
 - [AttachmentPayload](docs/AttachmentPayload.md)
 - [AttachmentRequest](docs/AttachmentRequest.md)
 - [AudioAttachment](docs/AudioAttachment.md)
 - [AudioAttachmentRequest](docs/AudioAttachmentRequest.md)
 - [Bigint](docs/Bigint.md)
 - [BotAddedToChatUpdate](docs/BotAddedToChatUpdate.md)
 - [BotCommand](docs/BotCommand.md)
 - [BotInfo](docs/BotInfo.md)
 - [BotPatch](docs/BotPatch.md)
 - [BotRemovedFromChatUpdate](docs/BotRemovedFromChatUpdate.md)
 - [BotStartedUpdate](docs/BotStartedUpdate.md)
 - [Button](docs/Button.md)
 - [Callback](docs/Callback.md)
 - [CallbackAnswer](docs/CallbackAnswer.md)
 - [CallbackButton](docs/CallbackButton.md)
 - [Chat](docs/Chat.md)
 - [ChatAdminPermission](docs/ChatAdminPermission.md)
 - [ChatList](docs/ChatList.md)
 - [ChatMember](docs/ChatMember.md)
 - [ChatMembersList](docs/ChatMembersList.md)
 - [ChatPatch](docs/ChatPatch.md)
 - [ChatStatus](docs/ChatStatus.md)
 - [ChatTitleChangedUpdate](docs/ChatTitleChangedUpdate.md)
 - [ChatType](docs/ChatType.md)
 - [ContactAttachment](docs/ContactAttachment.md)
 - [ContactAttachmentPayload](docs/ContactAttachmentPayload.md)
 - [ContactAttachmentRequest](docs/ContactAttachmentRequest.md)
 - [ContactAttachmentRequestPayload](docs/ContactAttachmentRequestPayload.md)
 - [Error](docs/Error.md)
 - [FileAttachment](docs/FileAttachment.md)
 - [FileAttachmentPayload](docs/FileAttachmentPayload.md)
 - [FileAttachmentRequest](docs/FileAttachmentRequest.md)
 - [GetSubscriptionsResult](docs/GetSubscriptionsResult.md)
 - [Image](docs/Image.md)
 - [InlineKeyboardAttachment](docs/InlineKeyboardAttachment.md)
 - [InlineKeyboardAttachmentRequest](docs/InlineKeyboardAttachmentRequest.md)
 - [InlineKeyboardAttachmentRequestPayload](docs/InlineKeyboardAttachmentRequestPayload.md)
 - [Intent](docs/Intent.md)
 - [Keyboard](docs/Keyboard.md)
 - [LinkButton](docs/LinkButton.md)
 - [LinkedMessage](docs/LinkedMessage.md)
 - [LocationAttachment](docs/LocationAttachment.md)
 - [LocationAttachmentRequest](docs/LocationAttachmentRequest.md)
 - [MediaAttachmentPayload](docs/MediaAttachmentPayload.md)
 - [Message](docs/Message.md)
 - [MessageBody](docs/MessageBody.md)
 - [MessageCallbackUpdate](docs/MessageCallbackUpdate.md)
 - [MessageCreatedUpdate](docs/MessageCreatedUpdate.md)
 - [MessageEditedUpdate](docs/MessageEditedUpdate.md)
 - [MessageLinkType](docs/MessageLinkType.md)
 - [MessageList](docs/MessageList.md)
 - [MessageRemovedUpdate](docs/MessageRemovedUpdate.md)
 - [MessageStat](docs/MessageStat.md)
 - [NewMessageBody](docs/NewMessageBody.md)
 - [NewMessageLink](docs/NewMessageLink.md)
 - [PhotoAttachment](docs/PhotoAttachment.md)
 - [PhotoAttachmentPayload](docs/PhotoAttachmentPayload.md)
 - [PhotoAttachmentRequest](docs/PhotoAttachmentRequest.md)
 - [PhotoAttachmentRequestPayload](docs/PhotoAttachmentRequestPayload.md)
 - [PhotoToken](docs/PhotoToken.md)
 - [PhotoTokens](docs/PhotoTokens.md)
 - [Recipient](docs/Recipient.md)
 - [RequestContactButton](docs/RequestContactButton.md)
 - [RequestGeoLocationButton](docs/RequestGeoLocationButton.md)
 - [SendMessageResult](docs/SendMessageResult.md)
 - [SenderAction](docs/SenderAction.md)
 - [ShareAttachment](docs/ShareAttachment.md)
 - [SimpleQueryResult](docs/SimpleQueryResult.md)
 - [StickerAttachment](docs/StickerAttachment.md)
 - [StickerAttachmentPayload](docs/StickerAttachmentPayload.md)
 - [StickerAttachmentRequest](docs/StickerAttachmentRequest.md)
 - [StickerAttachmentRequestPayload](docs/StickerAttachmentRequestPayload.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionRequestBody](docs/SubscriptionRequestBody.md)
 - [Update](docs/Update.md)
 - [UpdateList](docs/UpdateList.md)
 - [UploadEndpoint](docs/UploadEndpoint.md)
 - [UploadType](docs/UploadType.md)
 - [UploadedInfo](docs/UploadedInfo.md)
 - [User](docs/User.md)
 - [UserAddedToChatUpdate](docs/UserAddedToChatUpdate.md)
 - [UserIdsList](docs/UserIdsList.md)
 - [UserRemovedFromChatUpdate](docs/UserRemovedFromChatUpdate.md)
 - [UserWithPhoto](docs/UserWithPhoto.md)
 - [VideoAttachment](docs/VideoAttachment.md)
 - [VideoAttachmentRequest](docs/VideoAttachmentRequest.md)

## Documentation For Authorization


## access_token

- **Type**: API key
- **API key parameter name**: access_token
- **Location**: URL query string


## Author


