# table-service

Have you seen [Flatware](https://github.com/jsoma/flatware) for [Tabletop.js](https://github.com/jsoma/tabletop)? (cf. [mhkeller's gdoc-to-s3](https://github.com/mhkeller/gdoc-to-s3)) Table-service is like that, except on-demand. Table-service comes in two parts:

## The server-side python script ...

Table-service is a **lightweight installation** -- if you've already got wsgi for python, just copy over two files, and your service is ready. You can point any number of Google Spreadsheets to this script, and it will cache all their sheets on Amazon S3.

## ... plus a script for your Spreadsheets.

You'll also need to [**add a script**](https://github.com/martinburch/table-service/wiki/Spreadsheet-installation) to your Google Spreadsheets, but if you want, you'll never have to touch it again. Google can notify the script automatically when cells change, and the script will keep things up-to-date. Or you can set up a menu item to invoke the script instead, so you don't show visitors your half-finished changes.
