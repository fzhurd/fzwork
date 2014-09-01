package com.comp3617.frankzhufinalproject;


import com.comp3617.weather.WeatherMainActivity;
import com.example.frankzhufinalproject.R;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;
import android.widget.AdapterView.OnItemSelectedListener;

public class CitySelectActivity extends Activity {
	
	// private Spinner  spinner1;
	// private Button submit;
	
	private static  String[] countriesArr;
	private Spinner spCountry;
	private String cityName;
	private String countryName;
	private EditText etextCityName;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_city_select);
		spCountry = (Spinner) findViewById(R.id.spinner1);
		etextCityName = (EditText)findViewById(R.id.editText1);
		
		countriesArr = getResources().getStringArray(R.array.country_array);
		
		
		spCountry.setAdapter(new ArrayAdapter<String> (this, android.R.layout.simple_spinner_item, countriesArr));
		
		
		spCountry.setOnItemSelectedListener(new OnItemSelectedListener() {

			@Override
			public void onItemSelected(AdapterView<?> arg0, View arg1,
					int pos, long id) {
				
				Toast.makeText(CitySelectActivity.this, "The selected country is " + countriesArr[pos], Toast.LENGTH_SHORT).show();
				countryName = countriesArr[pos];
				//task.setStatus(thisStatus);
				
			}

			@Override
			public void onNothingSelected(AdapterView<?> arg0) {
				// TODO Auto-generated method stub
				
			}
			
			
		});
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.city_select, menu);
		return true;
	}
	
	//go to the weather activity
	public void onSubmit(View v)
	{
		    String cityName =  etextCityName.getText().toString();	
			Intent intentCheckWeather = new Intent(this, WeatherMainActivity.class);
		
	    //*************************************************************************
			intentCheckWeather.putExtra("cityName", cityName);
			intentCheckWeather.putExtra("countryName", countryName);
			
			
			startActivity(intentCheckWeather);
	}

}



//*******************************************************************************************


/*package com.comp3617.frankzhufinalproject;


import com.comp3617.weather.WeatherMainActivity;
import com.example.frankzhufinalproject.R;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;
import android.widget.AdapterView.OnItemSelectedListener;

public class CitySelectActivity extends Activity {
	
	// private Spinner  spinner1;
	// private Button submit;
	
	private static  String[] countriesArr;
	private Spinner spCountry;
	private String cityName;
	private String countryName;
	private EditText etextCityName;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_city_select);
		spCountry = (Spinner) findViewById(R.id.spinner1);
		etextCityName = (EditText)findViewById(R.id.editText1);
		
		countriesArr = getResources().getStringArray(R.array.country_array);
		
		
		spCountry.setAdapter(new ArrayAdapter<String> (this, android.R.layout.simple_spinner_item, countriesArr));
		
		
		spCountry.setOnItemSelectedListener(new OnItemSelectedListener() {

			@Override
			public void onItemSelected(AdapterView<?> arg0, View arg1,
					int pos, long id) {
				
				Toast.makeText(CitySelectActivity.this, "This task status is " + countriesArr[pos], Toast.LENGTH_SHORT).show();
				countryName = countriesArr[pos];
				//task.setStatus(thisStatus);
				
			}

			@Override
			public void onNothingSelected(AdapterView<?> arg0) {
				// TODO Auto-generated method stub
				
			}
			
			
		});
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.city_select, menu);
		return true;
	}
	
	public void onSubmit(View v)
	{
		    String cityName =  etextCityName.getText().toString();	
			Intent intentCheckWeather = new Intent(this, WeatherMainActivity.class);
		
	    //*************************************************************************
			intentCheckWeather.putExtra("cityName", cityName);
			intentCheckWeather.putExtra("countryName", countryName);
			
			
			startActivity(intentCheckWeather);
	}

}
*/