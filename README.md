Giant Multiplayer Robot for Linux
=========

Giant Multiplayer Robot is a service which makes it easy to play Sid Meier's Civilization V online, by distributing hotseat players who take turns to play in their own time. Civilization V was recently released for Linux, leaving me without a Giant Multiplayer Robot client for Linux. This Python project is an attempt at creating a (simple) client for the service on Linux.

Requirements
------------

 * Python 2.7
 * Python requests
 * Python ConfigParser
 * Civilization V is highly recommended

Installation
------------

I've aimed to make the installation of this client as simple and portable as possible. To install it, copy the directory anywhere (I would recommend `/opt/gmr-client` or `~/bin/gmr`, but it's up to you). Then, you might want to create a .desktop file or symbolic link as a shortcut to the `gmr-client` script which starts things.

Turn Notifications
------------
Since the GMR-API doesn't support push notifications, I suggest that you use email notifications from the GMR website.
