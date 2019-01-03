from mastodon import Mastodon
import schedule
import cred
import time



def post():
    '''
    Login for Mastdon and tooting a toot with the current weekday, date and time.
    '''
    weekday = time.strftime('%A')
    dateDMY =time.strftime('%d/%m/%Y')
    clock = time.strftime("%X")

    mastodon = Mastodon(
        api_base_url = 'https://botsin.space/',
        access_token = cred.accessToken
    )
    mastodon.log_in(
        cred.email,
        cred.password,
    )
    mastodon.status_post(f'Today is {weekday}, the {dateDMY} and it is {clock} o\'clock!', visibility='unlisted')
    # print(f'Today is {weekday}, the {dateDMY} and it is {clock} o\'clock!')

def main():
    '''
    Runs the schedule for the toots at 8 o'clock and 20 o'clock.
    '''
    schedule.every().day.at('08:00').do(post)
    schedule.every().day.at('20:00').do(post)
    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__ == "__main__":
    main()