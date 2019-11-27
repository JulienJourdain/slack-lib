#!/usr/bin/env python3
import modules.kaptenSlack as kaptenSlack

def main():
    
    # Args parser
    args = kaptenSlack.argsInit()
    
    # Generate a payload
    myPayload = kaptenSlack.createPayload(args.message, args.channel)

    # Send slack message
    kaptenSlack.send(myPayload, webhook=slack_webhook_url)

if __name__ == "__main__":
    main()