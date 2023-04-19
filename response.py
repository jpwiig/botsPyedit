
def newresponse(mssge: str) -> str:
    message = mssge.lower();
    # if  message contains a word in the list, return the corresponding warning
    contains = {

        'faen': 'ikke bann!',
        'fuck deg': 'ikke bann',

    }

    for contains, warning in contains.items():
        if contains in message:
            return warning

    only = {

        'https://tenor.com/view/ruben-vareide-ruben-vareide-prebz-og-dennis-prebz-gif-26529878': 'https://tenor.com/view/hammer-nope-hit-gif-25244680',
        'mus': 'ehus',
        '!hva': 'tulling XD',
        'grr': 'kanskje du bør roe deg ned litt',
        'rick': 'never gonna give you up, never gonna let you down',
    }


    for a, warning in only.items():
        if a == message:
            return warning
    return None
