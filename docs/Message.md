# Message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | [**Object**](.md) | User that sent this message. Can be &#x60;null&#x60; if message has been posted on behalf of a channel | [optional] 
**recipient** | [**Object**](.md) | Message recipient. Could be user or chat | 
**timestamp** | **int** | Unix-time when message was created | 
**link** | [**Object**](.md) | Forwarder or replied message | [optional] 
**body** | [**Object**](.md) | Body of created message. Text + attachments. Could be null if message contains only forwarded message | 
**stat** | [**Object**](.md) | Message statistics. Available only for channels in [GET:/messages](#operation/getMessages) context | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

