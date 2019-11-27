#!/usr/bin/env python3
import json
import requests
import argparse
import os
import sys

def argsInit():
    # Args parsing
    parser = argparse.ArgumentParser()
    
    # Required arguments
    parser.add_argument("message",
                        help="Slack message body")
    parser.add_argument("channel",
                        help="Slack channel")

    # Optional arguments
    parser.add_argument("--webhook",
                        help="Slack webhook URL")
    parser.add_argument("--token",
                        help="Slack application's token")
    parser.add_argument("--username",
                        help="Override username")
    parser.add_argument("--attachment_title",
                        help="Attachment's title")
    parser.add_argument("--attachment_pretext",
                        help="Optional text that appears above the attachment block")
    parser.add_argument("--attachment_message",
                        help="Optional text that appears within the attachment")              
    parser.add_argument("--attachment_fields",
                        help="Attachment - fields in format [{'title': 'field1', 'value': 'content'}, {'title': 'field2', 'value': 'content'}]")
    parser.add_argument("--attachment_color",
                        help="Attachment's color in hexadecimal format (ex: #FFF)")
    parser.add_argument("--attachment_author",
                        help="Attachment's author name")
    parser.add_argument("--attachment_fallback",
                        help="Required plain-text summary of the attachment")

    return(parser.parse_args())

def createPayload(message, channel, username=None, attachmentTitle=None, attachmentPretext=None, attachmentMessage=None, attachmentFields=None, attachmentColor=None, attachmentAuthor=None, attachmentFallback=None):
    payload = {}
    attachmentData = {}

    payload.update({ "text": str(message).replace("\\n", "\n") })

    if username:
        payload.update({ "username": username })

    if attachmentTitle:
        attachmentData.update({ "title": attachmentTitle })
    if attachmentPretext:
        attachmentData.update({ "pretext": attachmentPretext })
    if attachmentMessage:
        attachmentData.update({ "text": attachmentMessage })
    if attachmentFields:
        attachmentData.update({ "fields": attachmentFields })
    if attachmentColor:
        attachmentData.update({ "color": attachmentColor })
    if attachmentAuthor:
        attachmentData.update({ "author": attachmentAuthor })
    if attachmentFallback:
        attachmentData.update({ "fallback": attachmentFallback })

    if len(attachmentData) > 0:
        payload.update({ "attachments": [attachmentData] })
    
    payload.update({ "channel": channel })

    return(payload)

def send(payload, token=None, webhook=None):
    # Dynamic headers
    headers = {}
    headers.update({ "Content-Type": "application/json" })

    if token:
        slack_url = "https://slack.com/api/chat.postMessage"
        headers.update({ "Authorization": "Bearer {}".format(token) })
    elif webhook:
        slack_url = webhook
    else:
        print("ERROR! In order to send a message, you must provide at least an application token or a webhook URL.")
        sys.exit(1)

    requests.post(slack_url, data=json.dumps(payload), headers=headers)

def main():
    # Args parser
    args = argsInit()
    
    # Generate a payload
    myPayload = createPayload(
        message=args.message,
        channel=args.channel,
        username=args.username,
        attachmentTitle=args.attachment_title,
        attachmentPretext=args.attachment_pretext,
        attachmentMessage=args.attachment_message,
        attachmentFields=args.attachment_fields,
        attachmentColor=args.attachment_color,
        attachmentAuthor=args.attachment_author,
        attachmentFallback=args.attachment_fallback
    )

    # Send slack message
    if args.token is not None:
        send(myPayload, token=args.token)
    elif args.webhook is not None:
        send(myPayload, webhook=args.webhook)
    else:
        print("ERROR! In order to send a message, you must provide at least an application token or a webhook URL.")
        sys.exit(1)

if __name__ == "__main__":
    main()
