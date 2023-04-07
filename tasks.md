# Tasks

## Registration Number Validation

1. Check whether registration number is valid.
2. Check whether registration number is present in the list of TAG members.

### Registration Model

1. Name
2. Registration Number
3. Team
4. Leader (Bool)

### Team Model

1. Name
2. Game (Enum)

## Request System

1. When someone joins a team, a reqeust should be sent to the team's leader
2. After the request has been accepted, the player should only be then made a part of the leader's team

## User system 

1. To avoid spam, create a user system so that people have to sign up before registering for tournament
2. Allow only one team registration per user (automatically will become team leader)
3. Allow either the user to enter a team or create a new one.

## Create superuser view

1. So the Tag Core members can see all the registrations, we need a seperate viewing page for them

### Bracket System (Optional)

1. Make a bracket maker using API calls to challonge.com
2. Update whenever a new team is created
