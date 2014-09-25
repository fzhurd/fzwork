
package com.comp3617.weather;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;


public class DailyForecastPageAdapter extends FragmentPagerAdapter {

	private int numDays;
	private FragmentManager fm;
	private WeatherForecast forecast;
	private final static SimpleDateFormat sdf = new SimpleDateFormat("E, dd-MM");
	
	public DailyForecastPageAdapter(int numDays, FragmentManager fm, WeatherForecast forecast) {
		super(fm);
		this.numDays = numDays;
		this.fm = fm;
		this.forecast = forecast;
		
	}
	
	
	// Page title
	@Override
	public CharSequence getPageTitle(int position) {
		// We calculate the next days adding position to the current date
		Date d = new Date();
		Calendar gc =  new GregorianCalendar();
		gc.setTime(d);
		gc.add(GregorianCalendar.DAY_OF_MONTH, position);
		
		return sdf.format(gc.getTime());
		
		
	}



	@Override
	public Fragment getItem(int num) {
		DayForecast dayForecast = (DayForecast) forecast.getForecast(num);
		DayForecastFragment f = new DayForecastFragment();
		f.setForecast(dayForecast);
		return f;
	}

	/* 
	 * Number of the days we have the forecast
	 */
	@Override
	public int getCount() {
		
		return numDays;
	}

}
