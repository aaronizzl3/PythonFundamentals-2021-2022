"""
5 - Win
3 - Draw
1 - Loss
"""
win = 5
draw = 3
loss = 1

num_wins = int(input("Number of wins: "))
num_draws = int(input("Number of draws: "))
num_losses = int(input("Number of losses: "))

games_played = num_wins + num_losses + num_draws
maximum_points = games_played * win
actual_points = (num_wins * win) + (num_draws * draw) + (num_losses * loss)

print(f"Games Played: {games_played}\n"
      f"Maximum Points Available: {maximum_points}\n"
      f"Actual Points: {actual_points}")


