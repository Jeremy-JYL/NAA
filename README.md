# About

Heavily inspired by ChatterBot ( https://github.com/gunthercox/ChatterBot )

## Name

N - Not

A - An

A - AI

## Try it out

Just run the main.py!

Default it will run with default `data.yaml` use `main.py {yaml or json File}` to run alternative Yaml or Json File!

## How it is work?

Basicly NAA work like a big if and else statement but use a yaml or json file like a AI Model inside there Triggers and Responds

## Files Format

The Json file have three part: 

1. Tag name - Like comment if not there the python code will rasie a error
2. Triggers - Use for the if statement
3. Responds - If statement responds

Note:
Triggers must be lower case!

For example:

    {
        "Tag Name": {
            "Triggers": [
                "triggers"
            ],
            "Responds": [
                "Responds"
            ]
        }
    }

Or:

    Tag Name:
      Triggers:
        - triggers
      Responds:
       - Responds

Special code:
1. time - will return the time for the datelibary
2. link ( Start with "http" or "https" ) - with open the link

## Why I create this

Answer is:

    I'm lazy to learn pytorch!
