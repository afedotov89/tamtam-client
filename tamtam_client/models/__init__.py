# coding: utf-8

# flake8: noqa
"""
    TamTam Bot API

    # About Bot API allows bots to interact with TamTam. Methods are called by sending HTTPS requests to [botapi.tamtam.chat](https://botapi.tamtam.chat) domain. Bots are third-party applications that use TamTam features. A bot can legitimately take part in a conversation. It can be achieved through HTTP requests to the TamTam Bot API.  ## Features TamTam bots of the current version are able to: - Communicate with users and respond to requests - Recommend users complete actions via programmed buttons - Request personal data from users (name, short reference, phone number) We'll keep working on expanding bot capabilities in the future.  ## Examples Bots can be used for the following purposes: - Providing support, answering frequently asked questions - Sending typical information - Voting - Likes/dislikes - Following external links - Forwarding a user to a chat/channel  ## @PrimeBot [PrimeBot](https://tt.me/primebot) is the main bot in TamTam, all bots creator. Use PrimeBot to create and edit your bots. Feel free to contact us for any questions, [@support](https://tt.me/support) or [team@tamtam.chat](mailto:team@tamtam.chat).  #### [PrimeBot](https://tt.me/primebot) commands: `/start` &mdash; start a dialog with a bot  `/create` &mdash; create a bot, assign the unique short name to it (from 4 to 64 characters)  `/set_name [name]` &mdash; assign a short or full name to the bot (up to 200 characters)  `/set_description [description]` &mdash; enter the description for the bot profile (up to 400 characters)  `/set_picture [URL]` &mdash; enter the URL of bot's picture  `/delete [username]` &mdash; delete the bot  `/list` &mdash; show the list of all bots  `/get_token` &mdash; obtain a token for a bot  `/revoke` &mdash; request a new token  `/help` &mdash; help  ## HTTP verbs `GET` &mdash; getting resources, parameters are transmitted via URL  `POST` &mdash; creation of resources (for example, sending new messages)  `PUT` &mdash; editing resources  `DELETE` &mdash; deleting resources  `PATCH` &mdash; patching resources  ## HTTP response codes `200` &mdash; successful operation  `400` &mdash; invalid request  `401` &mdash; authentication error  `404` &mdash; resource not found  `405` &mdash; method is not allowed  `429` &mdash; the number of requests is exceeded  `503` &mdash; service unavailable  ## Resources format For content requests (PUT and POST) and responses, the API uses the JSON format. All strings are UTF-8 encoded. Date/time fields are represented as the number of milliseconds that have elapsed since 00:00 January 1, 1970 in the long format. To get it, you can simply multiply the UNIX timestamp by 1000. All date/time fields have a UTC timezone. ## Error responses In case of an error, the API returns a response with the corresponding HTTP code and JSON with the following fields:  `code` - the string with the error key   `message` - a string describing the error </br>  For example: ```bash > http https://botapi.tamtam.chat/chats?access_token={EXAMPLE_TOKEN} HTTP / 1.1 403 Forbidden Cache-Control: no-cache Connection: Keep-Alive Content-Length: 57 Content-Type: application / json; charset = utf-8 Set-Cookie: web_ui_lang = ru; Path = /; Domain = .tamtam.chat; Expires = 2019-03-24T11: 45: 36.500Z {    \"code\": \"verify.token\",    \"message\": \"Invalid access_token\" } ``` ## Receiving Notifications TamTam Bot API supports 2 options of receiving notifications on new dialog events for bots: - Push notifications via WebHook. To receive data via WebHook, you'll have to [add subscription](https://dev.tamtam.chat/#operation/subscribe); - Notifications upon request via [long polling](#operation/getUpdates) API. All data can be received via long polling **by default** after creating the bot,  Both methods **cannot** be used simultaneously. Refer to the response schema of [/updates](https://dev.tamtam.chat/#operation/getUpdates) method to check all available types of updates.  ## Message buttons You can program buttons for users answering a bot. TamTam supports the following types of buttons:   `callback` &mdash; sends a notification to a bot (via WebHook or long polling)  `link` &mdash; makes a user to follow a link  `request_contact` &mdash; requests the user permission to access contact information (phone number, short link, email)  You may also send a message with an [InlineKeyboard]() type attachment to start creating buttons. When the user presses a button, the bot receives the answer with filled callback field. It is recommended to edit that message so the user can receive updated buttons.  # Versioning API models and interface may change over time. To make sure your bot will get the right info, we strongly recommend adding API version number to each request. You can add it as `v` parameter to each HTTP-request. For instance, `v=0.1.2`. To specify the data model version you are getting through WebHook subscription, use the `version` property in the request body of the [subscribe](https://dev.tamtam.chat/#operation/subscribe) request.  # Libraries We have created [Java library](https://github.com/tamtam-chat/tamtam-bot-api) to make using API easier.  # Changelog ##### Version 0.1.8 - Added `code`, `width`, `height` to [StickerAttachment](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1580) - `token` is now only one required property for video/audio/file attachments - `sender` and `chat_id` of [LinkedMessage](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1401) are now optional - Added clarifying `message` to [SimpleQueryResult](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1938)  ##### Version 0.1.7 - It is now **required** to pass `marker` parameter in [/updates](#operation/getUpdates) requests, except initial  - Added full `User` object to update types: bot_started, bot_added, bot_removed, user_added, user_removed, chat_title_changed - Added `size` and `filename` to [`FileAttachment`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1503) - Added [`token`](https://github.com/tamtam-chat/tamtam-bot-api-schema/blob/master/schema.yaml#L1525) property to video/audio/file attachments allows you to reuse attachments uploaded by another user  ##### Version 0.1.6 - Added method to [edit bot info](#operation/editMyInfo) - Added statistics for messages in channel - `Message.sender` and `UserWithPhoto.avatar_url/full_avatar_url` removed from required properties  ##### Version 0.1.5 - Added `id` property to media attachments (`VideoAttachment`, `AudioAttachment`) so you can reuse attachment from one message in another - Added ability to create *linked* message: replied or forwarded. See `link` in `NewMessageBody` - `intent` property marked as required only for `CallbackButton`  ##### Version 0.1.4 - Added `user_ids` parameter to [get members](#operation/getMembers) in chat by id - `attachment` property of [send message](#operation/sendMessage) request body marked as deprecated  ##### Version 0.1.3 - Added method to [delete](https://dev.tamtam.chat/#operation/deleteMessages) messages - Added ability to [get](https://dev.tamtam.chat/#operation/getMessages) particular messages by ID - Added `is_admin` flag to `ChatMember` - Added `message` property to `MessageCallbackUpdate` - Renamed property `message` to `body` for `Message` schema - Added reusable `token` to `PhotoAttachment`. It allows to attach the same photo more than once.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    OpenAPI spec version: 0.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.action_request_body import ActionRequestBody
from swagger_client.models.attachment import Attachment
from swagger_client.models.attachment_payload import AttachmentPayload
from swagger_client.models.attachment_request import AttachmentRequest
from swagger_client.models.audio_attachment import AudioAttachment
from swagger_client.models.audio_attachment_request import AudioAttachmentRequest
from swagger_client.models.bigint import Bigint
from swagger_client.models.bot_added_to_chat_update import BotAddedToChatUpdate
from swagger_client.models.bot_command import BotCommand
from swagger_client.models.bot_info import BotInfo
from swagger_client.models.bot_patch import BotPatch
from swagger_client.models.bot_removed_from_chat_update import BotRemovedFromChatUpdate
from swagger_client.models.bot_started_update import BotStartedUpdate
from swagger_client.models.button import Button
from swagger_client.models.callback import Callback
from swagger_client.models.callback_answer import CallbackAnswer
from swagger_client.models.callback_button import CallbackButton
from swagger_client.models.chat import Chat
from swagger_client.models.chat_admin_permission import ChatAdminPermission
from swagger_client.models.chat_list import ChatList
from swagger_client.models.chat_member import ChatMember
from swagger_client.models.chat_members_list import ChatMembersList
from swagger_client.models.chat_patch import ChatPatch
from swagger_client.models.chat_status import ChatStatus
from swagger_client.models.chat_title_changed_update import ChatTitleChangedUpdate
from swagger_client.models.chat_type import ChatType
from swagger_client.models.contact_attachment import ContactAttachment
from swagger_client.models.contact_attachment_payload import ContactAttachmentPayload
from swagger_client.models.contact_attachment_request import ContactAttachmentRequest
from swagger_client.models.contact_attachment_request_payload import ContactAttachmentRequestPayload
from swagger_client.models.error import Error
from swagger_client.models.file_attachment import FileAttachment
from swagger_client.models.file_attachment_payload import FileAttachmentPayload
from swagger_client.models.file_attachment_request import FileAttachmentRequest
from swagger_client.models.get_subscriptions_result import GetSubscriptionsResult
from swagger_client.models.image import Image
from swagger_client.models.inline_keyboard_attachment import InlineKeyboardAttachment
from swagger_client.models.inline_keyboard_attachment_request import InlineKeyboardAttachmentRequest
from swagger_client.models.inline_keyboard_attachment_request_payload import InlineKeyboardAttachmentRequestPayload
from swagger_client.models.intent import Intent
from swagger_client.models.keyboard import Keyboard
from swagger_client.models.link_button import LinkButton
from swagger_client.models.linked_message import LinkedMessage
from swagger_client.models.location_attachment import LocationAttachment
from swagger_client.models.location_attachment_request import LocationAttachmentRequest
from swagger_client.models.media_attachment_payload import MediaAttachmentPayload
from swagger_client.models.message import Message
from swagger_client.models.message_body import MessageBody
from swagger_client.models.message_callback_update import MessageCallbackUpdate
from swagger_client.models.message_created_update import MessageCreatedUpdate
from swagger_client.models.message_edited_update import MessageEditedUpdate
from swagger_client.models.message_link_type import MessageLinkType
from swagger_client.models.message_list import MessageList
from swagger_client.models.message_removed_update import MessageRemovedUpdate
from swagger_client.models.message_stat import MessageStat
from swagger_client.models.new_message_body import NewMessageBody
from swagger_client.models.new_message_link import NewMessageLink
from swagger_client.models.photo_attachment import PhotoAttachment
from swagger_client.models.photo_attachment_payload import PhotoAttachmentPayload
from swagger_client.models.photo_attachment_request import PhotoAttachmentRequest
from swagger_client.models.photo_attachment_request_payload import PhotoAttachmentRequestPayload
from swagger_client.models.photo_token import PhotoToken
from swagger_client.models.photo_tokens import PhotoTokens
from swagger_client.models.recipient import Recipient
from swagger_client.models.request_contact_button import RequestContactButton
from swagger_client.models.request_geo_location_button import RequestGeoLocationButton
from swagger_client.models.send_message_result import SendMessageResult
from swagger_client.models.sender_action import SenderAction
from swagger_client.models.share_attachment import ShareAttachment
from swagger_client.models.simple_query_result import SimpleQueryResult
from swagger_client.models.sticker_attachment import StickerAttachment
from swagger_client.models.sticker_attachment_payload import StickerAttachmentPayload
from swagger_client.models.sticker_attachment_request import StickerAttachmentRequest
from swagger_client.models.sticker_attachment_request_payload import StickerAttachmentRequestPayload
from swagger_client.models.subscription import Subscription
from swagger_client.models.subscription_request_body import SubscriptionRequestBody
from swagger_client.models.update import Update
from swagger_client.models.update_list import UpdateList
from swagger_client.models.upload_endpoint import UploadEndpoint
from swagger_client.models.upload_type import UploadType
from swagger_client.models.uploaded_info import UploadedInfo
from swagger_client.models.user import User
from swagger_client.models.user_added_to_chat_update import UserAddedToChatUpdate
from swagger_client.models.user_ids_list import UserIdsList
from swagger_client.models.user_removed_from_chat_update import UserRemovedFromChatUpdate
from swagger_client.models.user_with_photo import UserWithPhoto
from swagger_client.models.video_attachment import VideoAttachment
from swagger_client.models.video_attachment_request import VideoAttachmentRequest
