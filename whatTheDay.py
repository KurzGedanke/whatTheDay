from mastodon import Mastodon
import schedule
import cred
import time



def post():
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

def main():
    schedule.every(2).seconds.do(post)
    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__ == "__main__":
    main()