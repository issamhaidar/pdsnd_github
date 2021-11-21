import time
import pandas as pd
import numpy as np

"Based on the city chosen, the variable opens the right csv file"
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
    print('Hello! Let\'s explore some US bikeshare data in Chicago, New York City &  Washington!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cityname = ""
    citynames = ["chicago", "new york city", "washington"]
    while (cityname.lower() not in citynames):
        cityname = input('Enter a city name: "chicago, new york city, washington":\n').lower()
        if (cityname.lower() in citynames):
            break
        else:
            print("Incorrect City")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    months = ["january", "february", "march", "april", "may", "june", "all"]
    while(month.lower() not in months):
        month = input("Which month would you like to filter: 'january, february, march, april, may, june or all':\n" ).lower()
        if (month.lower() in months):
            break
        else:
            print("Incorrect month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    while((day.lower() not in days)):
        day = input("Which day of week would you like to filter: 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all':\n" ).lower()
        if (day.lower() in days):
            break
        else:
            print("Incorrect day")

    print('-'*40)
    return cityname, month, day


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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june", "all"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):
    """ Displays data for the specified city and filters by month and day if applicable. """
    i = 0
    raw = input("Display raw data? (Comment 'yes' or 'no'\n)").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)
    max_iter = 0
    while True:
        max_iter += 1
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[:5+i]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Display more raw data? (Comment 'yes' or 'no')\n").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        elif max_iter == 5:
            print("Max number of displays reached")
            break
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_dow = df['day_of_week'].mode()[0]
    print('Most common day of week:', popular_dow)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip:', df.groupby(['Start Station','End Station']).size().idxmax()[0],
           '-',df.groupby(['Start Station','End Station']).size().idxmax()[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: %d seconds.'% df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time: %.1f seconds.' % df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    """Displays statistics on bikeshare users."""
def user_stats(df):


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("User type count:", user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()

        print("Gender count:", gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print("Earliest user year of birth %d"% df["Birth Year"].min())
        print("Latest user year of birth %d"% df["Birth Year"].max())
        print("Most common user year of birth %d"% df["Birth Year"].mode()[0])
    except:
        print("")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"Main Function"
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        answer = 0
        while(answer == 0):
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'no':
                answer = "no"
                break
            elif restart.lower() == 'yes':
                print("Sure thing!")
                answer = 1
            else:
                print("Incorrect answer")
        if (answer == "no"):
            break


if __name__ == "__main__":
	main()
