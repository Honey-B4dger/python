class CaesarCipher():
    def __init__(self, message, mode, key):
        self.message = message
        self.mode = mode
        self.key = key
        # self.SYMBOLS = r'abcdefghijklmnopqrstuvwxyz'
        self.SYMBOLS = r'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
        self.result = ''

    def get_shifted_index(self, index):
        result = int()
        length = len(self.SYMBOLS)

        if self.mode == 'decode':
            index_shifted = index - self.key
        else:
            index_shifted = index + self.key

        if index_shifted in range(length):
            result = index_shifted
        elif index_shifted >= length:
            result = index_shifted - length
        else:
            result = index_shifted + length

        return result

    def decode_encode(self):
        result = ''
        for char in self.message:
            if char in self.SYMBOLS:
                index = self.SYMBOLS.find(char)
                shifted_index = self.get_shifted_index(index)
                result += self.SYMBOLS[shifted_index]
            else:
                result += char
        self.result = result

    def main(self):
        self.decode_encode()


if __name__ == '__main__':
    # message = 'qeFIP?eGSeECNNS'
    # message = '5coOMXXcoPSZIWoQI'
    # message = "avnl1olyD4l'ylDohww6DhzDjhuDil"
    message = 'z.GM?.cEQc. 70c.7KcKMKHA9AGFK'
    mode = 'decode'
    print(f'Message: {message}')
    print()

    for key in range(66):
        c = CaesarCipher(message, mode, key)
        c.main()
        print(f'Key {key}: {c.result}')
