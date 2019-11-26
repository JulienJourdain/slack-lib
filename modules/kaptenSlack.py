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
    parser.add_argument("--attachment-title",
                        help="Attachment's title")
    parser.add_argument("--attachment-pretext",
                        help="Optional text that appears above the attachment block")
    parser.add_argument("--attachment-message",
                        help="Optional text that appears within the attachment")              
    parser.add_argument("--attachment-fields",
                        help="Attachment - fields in format [{'title': 'field1', 'value': 'content'}, {'title': 'field2', 'value': 'content'}]")
    parser.add_argument("--attachment-color",
                        help="Attachment's color in hexadecimal format (ex: #FFF)")
    parser.add_argument("--attachment-author",
                        help="Attachment's author name")
    parser.add_argument("--attachment-fallback",
                        help="Required plain-text summary of the attachment")

    return(parser.parse_args())

def webhookInit():
    if not os.environ.get('SLACK_WEBHOOK'):
        print("Environnement variable 'SLACK_WEBHOOK' does not exists")
        sys.exit(1)
    else:
        return(os.environ.get('SLACK_WEBHOOK'))

def createPayload(message, channel, attachmentTitle=None, attachmentPretext=None, attachmentMessage=None, attachmentFields=None, attachmentColor=None, attachmentAuthor=None, attachmentFallback=None):
    payload = {}
    attachmentData = {}

    if attachmentTitle:
        data.update({ "title": attachmentTitle })
    if attachmentPretext:
        data.update({ "pretext": attachmentPretext })
    if attachmentMessage:
        data.update({ "text": attachmentMessage })
    if attachmentFields:
        data.update({ "fields": attachmentFields })
    if attachmentColor:
        data.update({ "color": attachmentColor })
    if attachmentAuthor:
        data.update({ "author": attachmentAuthor })
    if attachmentFallback:
        data.update({ "author": attachmentFallback })

    payload.update({ "text": message })

    if len(attachmentData) > 0:
        payload.update({ "attachments": [attachmentData] })
    
    payload.update({ "channel": channel })

    return(payload)

def send(webhook, payload):
    requests.post(webhook, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

if __name__ == "__main__":
    main()