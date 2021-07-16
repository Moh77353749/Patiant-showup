import pandas as pd
import matplotlib.pyplot as plt

data = 'data.csv'


def load_data(data):
    '''
    load the data set and make organize it.
    :return: the dataFrame df ready for the analyses.
    '''
    global df
    df = pd.read_csv(data)  # read the data set
    df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])  # convert the column to a date time format
    df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
    df['month'] = df['AppointmentDay'].dt.month  # extract the months from the column
    df['day of appointment'] = df['AppointmentDay'].dt.day_name()  # extract the days from the column
    return df


def show_trends(df):
    '''
    takes the DataFrame and show the graphs that illustrates some relations.
    :param df:the DataFrame.
    :return: graphs between ( Gender, Day) and the No-show, the Gender &Day of appointment and some other relations
    '''
    df['day of appointment'] = df['AppointmentDay'].dt.day  # extract the days from the column

    df['No-show'] = df['No-show'].map({'Yes': 1, 'No': 0})
    df = df.rename(columns={'No-show': 'Miss-appointment'})
    df['Gender'] = df['Gender'].map({'M': 1, 'F': 0})  # this is to build the correlation matrix
    print(df.corr())  # illustrate the Relationships between the variables.


    ((df['Miss-appointment'] + ' ' + df['Gender']).value_counts()).plot(kind='bar')
    plt.show()
    ((df['Miss-appointment'] + ' ' + df['day of appointment']).value_counts()).plot(kind='bar')
    plt.show()
    df['Miss-appointment'].value_counts().plot(kind='bar')
    plt.show()
    df['Neighbourhood'].value_counts().plot(kind='pie')
    plt.show()
    ((df['Gender'] + ' ' + df['day of appointment']).value_counts()).plot(kind='bar')
    plt.show()
   # df['Gender'] = df['Gender'].map({1: 'Male', 0: 'Female'})# the lables have edited to bee more clear.

    print('How the Neighbourhood affects attending the appointment?', '\n', (df['No-show'] + '  ' + df['Neighbourhood'])
          .value_counts())
    print('the most common month used for appointments', df['month'].mode(), '\n', 'the most common day used for '
                                                                                   'appointments',
          df['day of appointment'].mode())


def main():
    load_data(data)
    show_trends(df)


if __name__ == "__main__":
    main()
