![FreeHub](https://github.com/kaneru-soju/FreeHub/blob/main/FreeHubLogo.jpg)

# FreeHub
An app centralizes information about free products and provides it to everyone.

## Inspiration

Who doesn't love free stuff? We browse Reddit sometimes to try and find good deals on games, ebooks, and other things. However, it is so inconvenient. After all, we just cannot just browse Reddit all day, especially when a lot of these posts are not that helpful.

## What it does
This is where our bot comes in, it helps sort through the noise and provides a curated feed of posts from subreddits with useful information on freebies!  We filter posts from the subreddits r/Freebies, r/freegamefindings, r/freestickers, r/freeebooks.  We also have options to filter which subreddits one would like to get notifications to, since the bot can be configured to ping the role associated with these subreddits.  The message is send in a reader-friendly embed message that lists useful information like the upvote-ratio of the post (so users can know how popular this reddit post was, which can give more information about its reliability and usefulness) and the subreddit the post came from.  The embed also provides an image and the link to the reddit post so users have access to the information.  

## How we built it
We used the reddit api to filter posts from certain subreddits (r/Freebies, r/freegamefindings, r/freestickers, r/freeebooks) since these are the main reddits to get free products.  Then, we forward the post information to our discord bot which runs on the discord.py API.  

## Challenges we ran into
Some challenges we ran into were trying to make a full fledged discord bot in python for the first time.
We ran into a couple problems deciding between making a website and a discord bot. We also ran into issues when deciding how we would use PRAW (public reddit wrapper for the api). We weren't sure whether we should choose a constanst stream of submissions or a curated list at set time intervals.
  
## Accomplishments that we're proud of
We were able to successfully filter through the reddit posts and gather the recent data uploaded and present it in a readable format.  Furthermore, we were able to combine the practicality of our project with discord, which is a widely used platform.  

## What we learned
We learned how to use PRAW, the public reddit wrapper api to query subreddits and filter them by recency.  We also learned how to use discord.py to create a discord bot that synergizes with our subreddit information parser.  We learned how to configure the bot to use embeds and ping roles.  

## What's next for FreeHub
We want to make the bot more automated. The setup should be easier. The role assignment for pings should be automatic through a command in some channel.  Furthermore, we would like to expand our reach to more subreddits and other sources of information, not just confined to reddit.  However, this may increase our chances of posting duplicate information, so we will need to build some mechanism to detect duplicated information.  
