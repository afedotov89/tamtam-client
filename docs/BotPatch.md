# BotPatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Visible name of bot | [optional] 
**username** | **str** | Bot unique identifier. It can be any string 4-64 characters long containing any digit, letter or special symbols: \&quot;-\&quot; or \&quot;_\&quot;. It **must** starts with a letter | [optional] 
**description** | **str** | Bot description up to 16k characters long | [optional] 
**commands** | [**list[BotCommand]**](BotCommand.md) | Commands supported by bot. Pass empty list if you want to remove commands | [optional] 
**photo** | [**Object**](.md) | Request to set bot photo | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

