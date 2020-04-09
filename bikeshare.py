import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ('january', 'february', 'march', 'april', 'may', 'june')

weekdays = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday')
def select(i, selections=()):

   #Return a valid input from the user 
    while True:
        select = input(i).lower().strip()
        if select in selections:
                break
                
        i = ( "please enter a valid option")
    return select

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
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        city = select("\nChoose A City, New York City, Chicago or Washington >>>", CITY_DATA.keys())

        month = select("\nFrom January to June, for what month(s) do you want do filter data?\n>",months)

        day = select("\nFor what weekday(s) do you want do filter bikeshare \n>", weekdays)

        break
        
    print('-'*40)
    return city, month, day





def load_data(city, month, day):

    """Load data for the specified filters of city(ies), month(s) and

       day(s) whenever applicable.



    Args:

        (str) city - name of the city(ies) to analyze

        (str) month - name of the month(s) to filter

        (str) day - name of the day(s) of week to filter

    Returns:

        df - Pandas DataFrame containing filtered data

    """



    print("\nThe program is loading the data for the filters of your choice.")

    start_time = time.time()



    # load data file into a dataframe


    df = pd.read_csv(CITY_DATA[city])

    

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Month'] = df['Start Time'].dt.month

    df['Weekday'] = df['Start Time'].dt.weekday_name

    df['Start Hour'] = df['Start Time'].dt.hour



    # filter the data according to month and weekday into two new DataFrames


    df = df[df['Month'] == (months.index(month)+1)]




    df = df[df['Weekday'] == day.title()]



    print("\nThis took {} seconds.".format((time.time() - start_time)))

    print('-'*40)



    return df
   


def time_stats(df):

    """Display statistics on the most frequent times of travel."""



    print('\nDisplaying the statistics on the most frequent times of '

          'travel...\n')

    start_time = time.time()

    # TO DO:display the most common month
    MCM = df['Month'].mode()[0] 
    # TO DO:display the most common day of week
    MCD = df['Weekday'].mode()[0]
    # TO DO:display the most common start hour
    MCH = df['Start Hour'].mode()[0]
    print("\nThis took {} seconds.".format((time.time() - start_time)))
    x=input ("Do You Want to display statistics on the most frequent times of travel ? Yes or No\n"  )
    if x=='yes':
    
        print('For the selected City, the month with the most travels is: ' + str(months[MCM-1]).title())
        print('For the selected City, the most common day of the week is: ' + str(MCD))
        print('For the selected City, the most common start hour is: ' + str(MCH))
        
   

    




   

print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = str(df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    most_common_end_station = str(df['End Station'].mode()[0]) 
    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combination'] = (df['Start Station'] + ' : ' + df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    y=input ("Do You Want to display The Most Popular Stations and Trip ? Yes or No\n"  )
    if y=='yes':   
        print("For the selected filters, the most common start station is: " +most_common_start_station)  
        print("For the selected filters, the most common start end is: " +most_common_end_station)
        print("For the selected filters, the most common start-end combination of stations is: " + most_common_start_end_combination)   

print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    total_travel_time = (str(int(total_travel_time//86400)) + 'd '+
                         str(int((total_travel_time % 86400)//3600)) + 'h '+
                         str(int(((total_travel_time % 86400) % 3600)//60)) +'m '+
                         str(int(((total_travel_time % 86400) % 3600) % 60)) +'s')

    

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')

    



    print("\nThis took {} seconds.".format((time.time() - start_time)))
    z=input ("Do You Want to display the total and average trip duration ? Yes or No\n"  )
    if z=='yes':
        print('For the selected filters, the total travel time is : ' + total_travel_time )
        print("For the selected filters, the mean travel time is : " + mean_travel_time)
 
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""
    k=input ("Do You Want to display User Stats ? Yes or No\n"  )
    if k=='yes':
        print('\nCalculating User Stats...\n')
        start_time = time.time()

    # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts().to_string()

        print("Distribution for user types:")

        print(user_types)

    # TO DO: Display counts of gender


        try:

            gender_distribution = df['Gender'].value_counts().to_string()

            print("\nDistribution for each gender:")

            print(gender_distribution)

        except KeyError:

            print(" There is no data of user genders for this city.")

 
    # TO DO: Display earliest, most recent, and most common year of birth

        try:

            earliest_birth_year = str(int(df['Birth Year'].min()))

            print("\nFor the selected filter, the oldest rider was born in: " + earliest_birth_year)

            most_recent_birth_year = str(int(df['Birth Year'].max()))

            print("For the selected filter, the youngest rider was born in: " + most_recent_birth_year)

            most_common_birth_year = str(int(df['Birth Year'].mode()[0]))

            print("For the selected filter, the most common birth year of riders is: " + most_common_birth_year)

        except:

            print(" There is no data of birth year for this city")

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
        
        r=input("do you wanna display row data?yes or No")
        if r=="yes":
            
            n=int(input("how many rows do you want to view ? please enter intiger number"))
             
                        
        print (df.head(n))
        n=0
           
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
