package com.eroldme.android.store_inventory


import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Base64
import android.view.KeyEvent
import android.webkit.WebView
import android.webkit.WebViewClient
class MainActivity : AppCompatActivity() {

    private lateinit var webView: WebView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        webView = findViewById(R.id.web_view)
        webView.webViewClient = StoreInventoryWebViewClient()
        webView.settings.builtInZoomControls = true
        webView.settings.javaScriptEnabled = true

        val unEncodedHtml = StringBuilder()
            .append("<html>")
            .append("  <body>")
            .append("      <h1 style='color:red;'>This is test content.</h1>")
            .append("  </body>")
            .append("</html>")
            .toString()

        val encodedHtml = Base64.encodeToString(unEncodedHtml.toByteArray(), Base64.NO_PADDING)
        webView.loadData(encodedHtml, "text/html", "base64")

    }

    override fun onKeyDown(keyCode: Int, event: KeyEvent?): Boolean {

        if (keyCode == KeyEvent.KEYCODE_BACK && webView.canGoBack()) {
            webView.goBack()
            return true
        }

        return super.onKeyDown(keyCode, event)
    }


    private class StoreInventoryWebViewClient : WebViewClient() {

        override fun shouldOverrideUrlLoading(view: WebView?, url: String): Boolean {
            return false
        }
    }
}