package com.example.golee;

import android.app.DownloadManager;
import android.content.Intent;
import android.graphics.Color;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;
import org.w3c.dom.Text;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {

    // Oncreate
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Intent intent = new Intent(this, SplashActivity.class);
        restfulRequest();
        startActivity(intent);


    }
    //RestfulRequest ( get 요청 함 )
    public void restfulRequest(){
        final RequestQueue queue = Volley.newRequestQueue(this);
        //TODO 서버 주소 및 URL 경로는 유동적으로 변경해야함
        String url ="http://13.125.164.239/get/www.woongin.com";
        Log.d("Log point1 ","log point1"+queue.toString());
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {

                    @Override
                    public void onResponse(String response) {
                        Log.d("Response is: ", response);
                    };
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.d("That didn't work!",error.toString());
            }

        });

        Log.d("Log point2" , "Log point2"+stringRequest.toString());
        queue.add(stringRequest);
        Log.d("Log point3" ,"Log point3"+queue.add(stringRequest).toString());


    }



}