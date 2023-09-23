def sourcetemplate(url):
    def make_question(**kwargs):
        if kwargs:
            return url + "?" + "&".join([f"{i}={j}" for i, j in sorted(kwargs.items(), key=lambda x: x[0])])
        return url

    return make_question
