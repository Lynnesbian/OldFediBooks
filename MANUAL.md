# Introduction
This is the manual for FediBooks. The latest version can always be accessed online [here](https://github.com/Lynnesbian/FediBooks/tree/master/MANUAL.md).

FediBooks is free software, both gratis (free of charge, as in "free car") and libre (free to run, modify and distrubute, as in "freedom"). It is licensed under the GNU Affero Public License version 3.0. For more information, check the license section later in this manual, or read the provided license file ("LICENSE" in the root directory of this repository).

# Donations
While FediBooks is provided free of charge, it is still possible to donate to the project. Provided below are various donation methods.
- [Patreon](https://patreon.com/lynnesbian)
- [LiberaPay](https://liberapay.com/lynnesbian/)
- [PayPal](https://paypal.me/Lynnesbian)
- [Ko-fi](https://ko-fi/Lynnesbian)

# Reporting Bugs and Making Feature Requests
If you'd like to report a bug with FediBooks, request a feature, or submit some other form of feedback, click [here](https://github.com/Lynnesbian/FediBooks/issues/) and use the search bar to see if anyone else has opened a similar issue yet. If not, click the green "[New Issue](https://github.com/Lynnesbian/FediBooks/issues/new/choose)" button.

# Supported Instance Types
Note: No instances are currently supported by FediBooks, as FediBooks itself doesn't work yet. The first working version of FediBooks will probably support these instance types:

| Instance type | Mastodon | Pleroma | Misskey | Diaspora* | Hubzilla | Osada | GangGo | GNU Social |
|---------------|----------|---------|---------|-----------|----------|-------|--------|------------|
|      Sourcing | ✔️        | ✔️       | ✔️       | ❌        | ❌       | ❌    | ❌     | ❌         |
|       Posting | ✔️        | ✔️       | ✔️       | ✔️         | ❌       | ❌    | ❌     | ❌         |
|      Replying | ✔️        | ✔️       | ✔️       | ❌        | ❌       | ❌    | ❌     | ❌         |

These instances are in descending order of priority -- for example, if Pleroma and Misskey support are both broken, I will focus on Pleroma first. I've ordered them in terms of relevance, userbase, and ease of support.

# Using FediBooks

## Caveats
 - FediBooks is currently incompatible with non-HTTPS instances. While it wouldn't be much work to support them, I doubt that there are many non-HTTPS instances out there, and some instance types (e.g. Mastodon) will outright refuse to federate with non-HTTPS instances.
 - As FediBooks is not finished yet, much of this documentation does not actually apply. This manual gives you an idea of how you can expect FediBooks to work, but it is subject to massive changes, and almost nothing listed here is implemented.
 - The bots can only post if the computer FediBooks is running on is online. If you put the computer FediBooks is running on into sleep mode, it will stop posting until the computer is woken up. FediBooks will not reply when mentioned while the computer is asleep, and it will not reply to the mentions it missed after the computer wakes up.
 - [mstdn-ebooks](https://github.com/Lynnesbian/mstdn-ebooks), the previous bot software I wrote, determined sources by seeing what accounts the bot was following. For example, if @bot was following @jack and @jill, it would download posts from their accounts and use them to learn. FediBooks does not work this way, and you will instead need to add sources via the user interface. Support for this method of specifying sources is planned.

## Permissions
This section aims to explain why FediBooks requests the account permissions it does.
### Mastodon and Pleroma
 - read:accounts - Get account info, such as accounts followed, user ID, etc.
 - read:follows - Relationship info between the bot account and another account -- check if they're blocked, followed, etc.
 - read:notifications - Monitor notifications for mentions
 - read:statuses - Read replies
 - write:follows - Follow accounts from the bot
 - write:media - Upload media (Eventually, the bots will (probably) be able to post images/videos)
 - write:statuses - Create posts
### Misskey
 - account-read - Get account info
 - account/read - I don't know what the difference between this and the above one is, and there's no documentation, so I'm adding this one to be safe
 - drive-write - Upload media
 - following-read - Check if we're following a user
 - following-write - Follow accounts from the bot
 - note-read - Read replies
 - note-write - Create posts
 - notification-read - Monitor notifications for mentions
<!--
### Osada and Hubzilla
-->
### Diaspora*
FediBooks uses your account credentials to log in to Diaspora* (this is currently the only way to authenticate with Diaspora*.). As no special "app tokens" are requested, it is impossible for FediBooks to only request certain permissions. FediBooks therefore operates with full access to your account.

## The User Interface (UI)
FediBooks provides a robust, intuitive graphical user interface (GUI) to aid the user in creating and maintaining their bot(s). No knowledge of the command line is required to use FediBooks, although there are some optional features that make use of it. This section of the manual will explain the UI in greater detail.

### Bot Creation Wizard
The Bot Creation Wizard guides you through the process of creating a new bot.

#### Choose an Instance
The first step (after the welcome page) is choosing an instance for the bot to run on. This doesn't need to be the same instance as your account(s)! Any instance should be fine. I recommend [botsin.space](https://botsin.space/about), a Mastodon instance dedicated to running bots. There are no benefits gained from having the bot on the same instance as you, aside from having access to the same emojo set.

#### Create an Account
This page allows you to create an account on the chosen instance. If you already have an account you'd like the bot to post from, you can continue without doing anything here. Note that you must confirm the email before continuing.

#### Registering App
FediBooks needs to create an app profile with your instance so that it can post properly. There's nothing for you to do here but sit back and watch the animated progressbar!

#### Authorise FediBooks
FediBooks needs access to your bot's account in order to post, reply, and so on. Click the "request access" button, complete the authorisation process in your browser, and paste the provided code into the text box provided. Every time you click the "request access" button, the previous request will be invalidated, so make sure you only click it again if the first time fails for some reason, or if you accidentally deny access.

For more information on the permissions requested by FediBooks, click [here](#permissions).

#### Select Sources
You must now provide at least one source for your bot to learn from. This can be a fediverse account (an account on Mastodon, Pleroma, Misskey...) or a text file on your computer. You can add as many sources as you like.

#### Configure your Bot
There are various options to choose from here. You can leave the defaults if you'd like. 
 - Learn from CW'd posts: If enabled, your bot will learn from posts with content warnings. This can lead to your bot posting unsavoury things, so it's disabled by default.
 - Check for new posts every [60 mins]: How frequently your bot should download and learn from new posts from the provided account(s).
 - Create a new post every [30 mins]: How frequently your bot should post.
 - Reply service: If enabled, your bot will reply when mentioned. 
 - CW for created posts: You can provide a content warning here, for example "Bot post" or "Markov post".  If you don't want a content warning, leave the box blank.

#### Attribution (Important)
Under the terms of the GNU Affero General Public License version 3.0, you are required to provide attribution. The simplest way to do this is to link to [FediBooks' GitHub repository](https://github.com/Lynnesbian/FediBooks), but you can do anything you'd like as long as you provide the following:
 1. A copy of, or a link to, the source code
 2. Acknowledgement of the author (Lynnesbian), with a link to somewhere I can be realistically contacted (such as my email address, fediverse handle, GitHub account...)

