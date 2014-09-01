package com.comp3617.frankzhufinalproject;

import com.example.frankzhufinalproject.R;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	
	//swtich to the city select activity
	public void onStart(View v)
	{
		Intent intentAddCity = new Intent(this, CitySelectActivity.class);
		
	    //*************************************************************************
			intentAddCity.putExtra("Msg", "Hello from Main Activity!");
			
			startActivity(intentAddCity);
	}

}
