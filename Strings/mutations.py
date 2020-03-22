def mutate_string(string, position, character):
    news=string[:position]+character+string[position+1:]
    return news
