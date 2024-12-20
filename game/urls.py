# game/urls.py
# app specific URLs for the mini_fb app

from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # main.html link. users will see this when they open my page
    path('', views.MainView.as_view(), name='main'),

    path(r'show_all_cards/', views.ShowAllCards.as_view(), name='show_all_cards'), # currently my main page
    path(r'hiders/', views.ShowAllHiders.as_view(), name='show_all_hiders'), # page for showing all hiders
    path(r'seekers/', views.ShowAllSeekers.as_view(), name='show_all_seekers'), # page for showing all seekers
    path(r'hiders/<int:pk>', views.ShowHiderView.as_view(), name='show_hider'), # page for showing a specific hider
    path(r'seekers/<int:pk>', views.ShowSeekerView.as_view(), name='show_seeker'), # page for showing a specific seeker
    path(r'create_game/', views.CreateGameView.as_view(), name='create_game'), # page for creating a game
    path(r'game/<int:pk>', views.GameView.as_view(), name='game'), # page for showing a specific game
    path(r'profile/<int:pk>', views.ShowProfileView.as_view(), name='show_profile'), # page for showing a specific profile
    path(r'create_profile/', views.CreateProfileView.as_view(), name='create_profile'), # page for creating a profile
    path(r'game_over/<int:pk>', views.GameOverView.as_view(), name='game_over'), # page for showing a specific game over
    path(r'leaderboard_by_games_won/', views.LeaderboardByGamesWonView.as_view(), name='leaderboard_by_games_won'), # page for showing the leaderboard
    path(r'leaderboard_by_games_played/', views.LeaderboardByGamesPlayedView.as_view(), name='leaderboard_by_games_played'), # page for showing the leaderboard
    path(r'leaderboard_by_win_rate/', views.LeaderboardByWinRateView.as_view(), name='leaderboard_by_win_rate'), # page for showing the leaderboard
    path(r'update_profile/', views.UpdateProfileView.as_view(), name='update_profile'), # page for updating a profile
    path(r'delete_upload_card/<int:pk>', views.DeleteUploadCardView.as_view(), name='delete_upload_card'), # page for deleting an upload card
    path(r'create_upload_card/', views.CreateUploadCardView.as_view(), name='create_upload_card'), # page for creating an upload card
    
    # login and logout paths
    path(r'login/', auth_views.LoginView.as_view(template_name='game/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='game/logged_out.html'), name='logout'),
]