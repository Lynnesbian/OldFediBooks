# Introduction
This is the manual for FediBooks. The latest version can always be accessed online [here](https://github.com/Lynnesbian/FediBooks/tree/master/MANUAL.md).

FediBooks is free software, both gratis (free of charge, as in "free car") and libre (free to run, modify and distrubute, as in "freedom"). It is licensed under the GNU Affero Public License version 3.0. For more information, check the license section later in this manual, or read the provided license file ("LICENSE" in the root directory of this repository).

#Donations
While FediBooks is provided free of charge, it is still possible to donate to the project. Provided below are various donation methods.
- [LiberaPay](https://liberapay.com/lynnesbian/)
- [PayPal](https://paypal.me/Lynnesbian)
- [Ko-fi](https://ko-fi/Lynnesbian)

# Using FediBooks

## Caveats
 - The bots can only post if the computer FediBooks is running on is online. If you put the computer FediBooks is running on into sleep mode, it will stop posting until the computer is woken up. FediBooks will not reply when mentioned while the computer is asleep, and it will not reply to those mentions after the computer wakes up.

## The User Interface (UI)
FediBooks provides a robust, intuitive graphical user interface (GUI) to aid the user in creating and maintaining their bot(s). No knowledge of the command line is required to use FediBooks, although there are some optional features that make use of it. This section of the manual will explain the UI in greater detail.

### Bot Creation Wizard
The Bot Creation Wizard guides you through the process of creating a new bot.

#### Choose an Instance
The first step (after the welcome page) is choosing an instance for the bot to run on. This doesn't need to be the same instance as your account(s)! Any instance should be fine. I reccomend [botsin.space](https://botsin.space/about), a Mastodon instance dedicated to running bots. There are no benefits gained from having the bot on the same instance as you, aside from having access to the same emojo set.

#### Create an Account
This page allows you to create an account on the chosen instance. If you already have an account you'd like the bot to post from, you can continue without doing anything here. Note that you must confirm the email before continuing.

#### Authorise FediBooks
FediBooks needs access to your bot's account in order to post, reply, and so on. Click the "request access" button, complete the authorisation process in your browser, and paste the provided code into the text box provided. Every time you click the "request access" button, the previous request will be invalidated, so make sure you only click it again if the first time fails for some reason, or if you accidentally deny access.

#### Select Sources
You must now provide at least one source for your bot to learn from. This can be a fediverse account (an account on Mastodon, Pleroma, Misskey...) or a text file on your computer. You can add as many sources as you like.

#### Configure your Bot
There are various options to choose from here. You can leave the defaults if you'd like. 
 - Learn from CW'd posts: If enabled, your bot will learn from posts with content warnings. This can lead to your bot posting unsavoury things, so it's disabled by default.
 - Check for new posts every [60 mins]: How frequently your bot should download and learn from new posts from the provided account(s).
 - Create a new post every [30 mins]: How frequently your bot should post.
 - Reply service: If enabled, your bot will reply when mentioned. 
 - CW for created posts: You can provide a content warning here, for example "Bot post" or "Markov post". 

#### Attribution (Important)
Under the terms of the GNU Affero General Public License version 3.0, you are required to provide attribution. The simplest way to do this is to link to [FediBooks' GitHub repository](https://github.com/Lynnesbian/FediBooks), but you can do anything you'd like as long as you provide 
 1. A copy of, or a link to, the source code
 2. Acknowledgement of the author (Lynnesbian)

