package com.example.kmsproject;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.messaging.FirebaseMessaging;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //추가한 라인
        FirebaseMessaging.getInstance().subscribeToTopic("news");
        FirebaseInstanceId.getInstance().getToken();
        Log.d("token::", FirebaseInstanceId.getInstance().getToken());
        WebView WebView01 = (WebView) findViewById(R.id.webView01);
        WebView01.setWebViewClient(new WebViewClient());
        WebSettings webSettings = WebView01.getSettings();
        webSettings.setJavaScriptEnabled(true);
        WebView01.getSettings().setLayoutAlgorithm(WebSettings.LayoutAlgorithm.SINGLE_COLUMN);
        WebView01.loadUrl("http://121.169.9.44/kms");


    }

}
