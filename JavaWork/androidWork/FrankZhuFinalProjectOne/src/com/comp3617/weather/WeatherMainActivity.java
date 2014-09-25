package com.comp3617.weather;

import com.example.frankzhufinalproject.R;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;


import android.os.AsyncTask;
import android.os.Bundle;
import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.support.v4.app.FragmentActivity;
import android.support.v4.view.ViewPager;
import android.view.Menu;
import android.widget.ImageView;
import android.widget.TextView;

public class WeatherMainActivity extends FragmentActivity {
	
	String checkCityName;
	String checkCountryName;

	
	private TextView cityText;
	private TextView condDescr;
	private TextView temp;
	private TextView press;
	private TextView windSpeed;
	private TextView windDeg;
	private TextView unitTemp;
	
	private TextView hum;
	private ImageView imgView;
	
	private static String forecastDaysNum = "7";
	private ViewPager pager;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.weather_main_activity);
		
		
		checkCityName = getIntent().getStringExtra("cityName");
		checkCountryName = getIntent().getStringExtra("countryName");
		
		String city = checkCityName + ",   "+ checkCountryName;
		
		String lang = "en";
		
		cityText = (TextView) findViewById(R.id.cityText);
		temp = (TextView) findViewById(R.id.temp);
		unitTemp = (TextView) findViewById(R.id.unittemp);
		unitTemp.setText("°C");
		condDescr = (TextView) findViewById(R.id.skydesc);
		
		pager = (ViewPager) findViewById(R.id.pager);
		imgView = (ImageView) findViewById(R.id.condIcon);
	
		
		
		JSONWeatherTask task = new JSONWeatherTask();
		task.execute(new String[]{city,lang});
		
		JSONForecastWeatherTask task1 = new JSONForecastWeatherTask();
		task1.execute(new String[]{city,lang, forecastDaysNum});
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	
	private class JSONWeatherTask extends AsyncTask<String, Void, Weather> {
		
		@Override
		protected Weather doInBackground(String... params) {
			Weather weather = new Weather();
			String data = ( (new WeatherHttpClient()).getWeatherData(params[0], params[1]));

			try {
				weather = JSONWeatherParser.getWeather(data);
				System.out.println("Weather ["+weather+"]");
				
				// Let's retrieve the icon
				weather.iconData = ( (new WeatherHttpClient()).getImage(weather.currentCondition.getIcon()));
				
			} catch (JSONException e) {				
				e.printStackTrace();
			}
			return weather;
		
	}
		
	//city name and temperature
	@Override
	protected void onPostExecute(Weather weather) {			
			super.onPostExecute(weather);
			
			if (weather.iconData != null && weather.iconData.length > 0) {
				Bitmap img = BitmapFactory.decodeByteArray(weather.iconData, 0, weather.iconData.length); 
				imgView.setImageBitmap(img);
			}
			
			
			cityText.setText(weather.location.getCity() + ", " + weather.location.getCountry());
			temp.setText("" + Math.round((weather.temperature.getTemp() - 275.15)));
			condDescr.setText(weather.currentCondition.getCondition() + "(" + weather.currentCondition.getDescr() + ")");
			
			
			
		}



  }
	
	
	private class JSONForecastWeatherTask extends AsyncTask<String, Void, WeatherForecast> {
		
		@Override
		protected WeatherForecast doInBackground(String... params) {
			
			String data = ( (new WeatherHttpClient()).getForecastWeatherData(params[0], params[1], params[2]));
			WeatherForecast forecast = new WeatherForecast();
			try {
				forecast = JSONWeatherParser.getForecastWeather(data);
				System.out.println("Weather ["+forecast+"]");
				
				
			} catch (JSONException e) {				
				e.printStackTrace();
			}
			return forecast;
		
	}
		
		
		
		
	@Override
		protected void onPostExecute(WeatherForecast forecastWeather) {			
			super.onPostExecute(forecastWeather);
			
			DailyForecastPageAdapter adapter = new DailyForecastPageAdapter(Integer.parseInt(forecastDaysNum), getSupportFragmentManager(), forecastWeather);
			
			pager.setAdapter(adapter);
		}



  }
}

