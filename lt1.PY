def error_sents(args):
    import string
    import nltk
    import language_check
    tool = language_check.LanguageTool('en-US')
    matches1 = tool.check(args)
    text=[]
    text.append(language_check.correct(args,matches1))
    #print(language_check.correct(args,matches1))
    return ('\n'.join(map(str,text))
