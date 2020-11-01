from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
#plt.xkcd()

minutes = [i for i in range(1,10)]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['Player 1', 'Player 2', 'Player 3']

#plt.pie([1, 1, 1], labels=['Player 1','Player 2','Player 3'])
plt.stackplot(minutes, player1, player2, player3, labels=labels)

plt.legend(loc='upper left')
plt.title('Stack Plot')
plt.tight_layout()
plt.show()
