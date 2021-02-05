class ColumnarTranspositionDecryption():

    def __init__(self, ciphertext, key):
        self.ciphertext = list(ciphertext)
        self.key = key
        self.columns = [''] * self.key
        self.result = ''

    def message_at_length(self):
        length = len(self.message)
        pipes = self.key - (length - (length // self.key) * self.key)
        return self.message + pipes * ['|']

    def encrypt(self):
        message = self.message_at_length()
        i = 0
        while message:
            if i >= self.key:
                i = 0
            self.columns[i] += message.pop(0)
            i += 1

    def decrypt(self):
        message = self.message_at_length()

    def create_ciphertext(self):
        result = []
        for column in self.columns:
            result.append(''.join(column))
        result = ''.join(result)
        self.result = result

    def clean_ciphertext(self):
        result = self.result[:]
        result = result[:result.index('|')]
        result += '|'
        self.result = result

    def print_result(self):
        print(f'Decrypting ciphertext: "{"".join(self.ciphertext)}"')
        print(f'Key: {self.key}')
        print(f'\nResulting ciphertext: "{self.result}"')

    def main(self):
        self.encrypt()
        self.create_ciphertext()
        self.clean_ciphertext()

        self.print_result()


if __name__ == '__main__':
    message = 'Common sense is not so common.'
    key = 8

    t = ColumnarTranspositionEncryption(message, key)
    t.main()
