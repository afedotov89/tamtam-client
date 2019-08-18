# Chat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **int** | Chats identifier | 
**type** | [**Object**](.md) | Type of chat. One of: dialog, chat, channel | 
**status** | [**Object**](.md) | Chat status. One of:  - active: bot is active member of chat  - removed: bot was kicked  - left: bot intentionally left chat  - closed: chat was closed | 
**title** | **str** | Visible title of chat. Can be null for dialogs | 
**icon** | [**Object**](.md) | Icon of chat | 
**last_event_time** | **int** | Time of last event occurred in chat | 
**participants_count** | **int** | Number of people in chat. Always 2 for &#x60;dialog&#x60; chat type | 
**owner_id** | **int** | Identifier of chat owner. Visible only for chat admins | [optional] 
**participants** | **dict(str, int)** | Participants in chat with time of last activity. Can be *null* when you request list of chats. Visible for chat admins only | [optional] 
**is_public** | **bool** | Is current chat publicly available. Always &#x60;false&#x60; for dialogs | 
**link** | **str** | Link on chat if it is public | [optional] 
**description** | [**Object**](Object.md) | Chat description | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

