# Android Flask App

A simple flask web application to work with Android's WebView.

#### Individual applications

The following is the list of individual applications that make up this application(*Hopefully*).

- Store Inventory - A Flask application for basic store inventory.
- AFA API - An API used by the Flask application to get, add, update, and delete data from a database.
- Store Inventory WebView - An android application that uses WebView to render the Flask application on an android device(Hopefully).

***The Idea is to run both the api and flask app on services like ngrok and edit [MainActivity.kt](https://github.com/mr-erold/Android-Flask-App/blob/8c743b67a3943282f9e48fe6f61ce6d00b5cc907/StoreInventoryWV/app/src/main/java/com/eroldme/android/store_inventory/MainActivity.kt#L31) to use `loadUrl()` instead and pass in the ngrok url.***

Well happy hacking...
