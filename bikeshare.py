import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago',' new york city', 'washington']
months =['january','february','march','april','may','june','all']
days =['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Search for the city you want?')
        if city in cities:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\n Search for the month you want? or all \n')
        if month in months:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\n Search for the day you want? or all \n')
        if day in days:
            break
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # Make columes to statistics
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    df['start_end'] = df['Start Station'].astype(str) + 'to' + df['End Station']
    
    #Month filter.
    if month !='all':
        month = months.index(month)+1
        #DataFrame for month
        df = df[df['month']== month]
    #Day filte.
    if day !='all':
        #DataFrame for Day
        df = df[df['week_day']==day.title()]

    return df


def time_stats(df):
                
     #"""Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month travels is:'+ str(months[most_common_month]).title()+'.')
               
    # TO DO: display the most common day of week
    most_common_day = df['week_day'].mode()[0]
    print('Most common day of week is:'+ str(most_common_day)+'.')

    # TO DO: display the most common start hour
    most_common_hour = df['start_hour'].mode()[0]
    print('Most common start hour is:'+ str(most_common_hour)+'.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['commonly_start'] = df['Start Station']
    common_start = df['commonly_start'].mode()[0]
    print('the most commonly used statrt station is:',common_start)
                
    # TO DO: display most commonly used end station
    df['commonly_end'] = df['End Station']
    common_end = df['commonly_end'].mode()[0]
    print('the most commonly used end station is:',common_end)

    # TO DO: display most frequent combination of start station and end station trip
    station_trip= df['commonly_start'] + 'to' + df['commonly_end']
    print('the most frequent combination of start station and end station trip:',station_trip.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    start_trip = pd.to_datetime(df['Start Time'])
    end_trip = pd.to_datetime(df['End Time'])
    df['total_trip'] = start_trip - end_trip
    total_travel_time = df['total_trip'].sum()
    print(' the total time for trip is:'+str(total_travel_time))
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The mean travel time of a trip is:'+str(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print("%s, what is your gender?")
    genderInput = input("Enter 'M' for Male or 'F' for Female\n")
    if genderInput == "M":
        gender = "Male"
    elif genderInput == "F":
        gender= "Female"

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("\nEarliest year of birth: ",df['Birth Year'].min())
        print("\nmost recent year of birth: ",df['Birth Year'].max())
        print("\nmost common of birth: ",df['Birth Year'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
