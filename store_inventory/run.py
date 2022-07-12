"""
A simple flask web application to work with Android's WebView.
"""

"""
Executes our Store Inventory app.
"""

from storeinventory import app

if __name__ == "__main__":
    app.run(debug=True, port=7676)