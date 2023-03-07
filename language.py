def get_lang(lang):
    match lang:
        case 0:
            return "English"
        case 1:
            return "Latvian"
        case 2:
            return "Lithuanian"
        case 3:
            return "German"


print(get_lang(1))
