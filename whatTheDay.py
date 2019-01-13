from mastodon import Mastodon
import schedule
import cred
import time
import logging

def log_in():
    '''
    Logges in to mastodon and returns the mastodon class.
    '''
    mastodon = Mastodon(
        api_base_url = 'https://botsin.space/',
        access_token = cred.accessToken
    )

    try:
        mastodon.log_in(
            cred.email,
            cred.password,
        )

        logging.info('Logged in Sucessfull!')

    except Exception as error:
        logging.error(repr(error))
        exit()
    
    return(mastodon)


def post():
    '''
    Gets the week day, date and time and toots it.
    '''
    mastodon = log_in()

    weekday = time.strftime('%A')
    dateDMY =time.strftime('%d/%m/%Y')
    clock = time.strftime("%X")

    try:
        # mastodon.status_post(f'Today is {weekday}, the {dateDMY} and it is {clock} o\'clock!', visibility='unlisted')
        mastodon.status_post('Today is {}, the {} and it is {} o\'clock!'.format(weekday, dateDMY, clock), visibility='unlisted')
        # print(f'Today is {weekday}, the {dateDMY} and it is {clock} o\'clock!')

        logging.info('Post Sucessfull!')
        
    except Exception as error:
        logging.error(repr(error))
        pass

def main():
    '''
    Runs the schedule for the toots at 8 o'clock and 20 o'clock.
    '''
    logging.basicConfig(filename='whattheday.log',level=logging.DEBUG)

    schedule.every().day.at('08:00').do(post)
    schedule.every().day.at('20:00').do(post)

    # schedule.every(2).seconds.do(post)
    
    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__ == "__main__":
    main()