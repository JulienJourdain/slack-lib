#!/usr/bin/env python3
import modules.kaptenSlack as kaptenSlack

def main():
    
    # Args parser
    args = kaptenSlack.argsInit()

    # Slack webhook
    slack_webhook_url = kaptenSlack.webhookInit()
    
    # Generate a payload
    myPayload = kaptenSlack.createPayload(args.message, args.channel)

    # Send slack message
    kaptenSlack.send(slack_webhook_url, myPayload)
    

if __name__ == "__main__":
    main()