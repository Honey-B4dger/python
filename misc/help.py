import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    result = False
    redWords = ['asap', 'help', 'urgent']
    for redWord in redWords:
        redWord = list(redWord)
        regexString = '+[!|-|\.]?'.join(redWord)
        regexString += '+'
        redWordRegex = re.compile(regexString, re.I)
        if redWordRegex.findall(subj):
            result = True

    if subj.endswith('!!!'):
        result = True

    return result

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("help!!!") == True, "Second"
    assert is_stressful("h!e!l!p") == True, "Second"
    assert is_stressful("u-r-g-e-n-t issue!!") == True, "Second"
    print('Done! Go Check it!')
