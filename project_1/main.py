import requests
from bs4 import BeautifulSoup
import cv2
import matplotlib.pyplot as plt
import json


# url_news = 'https://www.fcbarcelona.com/en/football/first-team/news'
# url_team = 'https://www.fcbarcelona.com/en/football/first-team/players'


# FCB latest News
def get_news():
    url_news = url_news = 'https://www.fcbarcelona.com/en/football/first-team/news'
    bs_news = BeautifulSoup(requests.get(url_news).content, "html.parser")
    news = bs_news.find(name='div', attrs={"class": 'feed__items js-feed-items'})
    news_list = []
    for news_title in news.find_all(attrs={'class': 'thumbnail__title'}):
        news_list.append(news_title.string)
    return news_list


# FCB team buildup
def get_team():
    url_team = 'https://www.fcbarcelona.com/en/football/first-team/players'
    bs_team = BeautifulSoup(requests.get(url_team).content, 'html.parser')
    team = bs_team.find(name='div', attrs={"class": 'team-list js-team-list'})
    team_name = []
    image_dic = {}
    for team_title in team.find_all(attrs={'class': 'team-list__section'})[0:-1]:
        team_name.append('\n'+team_title.div.string+':')
        for player in team_title.find_all(attrs={'class': 'team-list__person-container js-team-list-player'}):
            player_name = player.find(attrs={'class': 'team-person__last-name js-team-list-player-last-name'})
            player_image = player.img['data-image-src']
            team_name.append(player_name.string)
            image_dic[player_name.string] = player_image
    return team_name, image_dic


# download player's image
def download_image(name):
    team_n, image_d = get_team()
    response = requests.get(image_d[name])
    file = open(name+".jpg", "wb")
    file.write(response.content)
    file.close()


# itunes Api
def itunes(name):
    parameters = {'term': name, 'entity': 'song'}
    url = requests.get('https://itunes.apple.com/search', params=parameters)
    hjson = json.loads(url.text)
    song_name = []
    for item in hjson['results']:
        song_name.append(item['trackName'])
    return song_name
