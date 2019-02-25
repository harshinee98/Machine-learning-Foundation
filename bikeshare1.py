import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    print("\nWould you like to see data for Chicago , New York or Washington ?")
    city=input()

    # TO DO: get user input for month (all, january, february, ... , june)
    print("\nWhich month? all,janauary,february,march,april,may,june")
    month=input()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("\nWhich day ? all,monday,tuesday,wednesday,thursday,friday,saturday,sunday")
    day=input() 
        
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
    df =pd.read_csv(CITY_DATA[city]) 
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['month'] =  df['Start Time'].dt.month
    df['hour'] =  df['Start Time'].dt.hour
    df['day_of_week'] =  df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =  months.index(month)+1
        df =df[df['month']==month] 
    if day != 'all':
        df =df[df['day_of_week']==day.title()] 
        
       
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print ("\nThe most common month is : ",df['month'].mode()[0])


    # TO DO: display the most common day of week
    print ("\nThe most common day is : ",df['day_of_week'].mode()[0])       


    # TO DO: display the most common start hour
    print ("\nThe most common start hour is : ",df['hour'].mode()[0])       


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ("\nThe most commonly used start station is : ",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print ("\nThe most commonly used end station is : ",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print ("\nThe most frequent combination of start station and end station is",df.groupby(['Start Station','End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is : ",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The total travel time is : ",df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)



    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print(gender_types)
      
    


    # TO DO: Display earliest, most recent, and most common year of birth
    print ("\nThe most common year of birth is : ",df['Birth Year'].mode()[0])
    print("\nThe earliest year of birth is : ",df['Birth Year'].min())
    print("\nThe most recent year of birth is : ",df['Birth Year'].maxs())
           

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
