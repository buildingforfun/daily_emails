import pandas as pd

def kindle_clipper(file_path):
    """
    Returns a random clip from the kindle clipping file
    """
    with open(file_path, 'r') as file:
        kindle_text = file.read()
    file.close()

    # Splits the text string into a list of sections
    sections = kindle_text.split('==========\n')

    titles = []
    quotes = []

    # Loops through all the sections
    for section in sections:
        # Removes any leading and trailing whitespaces
        if section.strip():
            # Splits the text string into a list by new lines
            lines = section.split('\n')
            # Separates the title, detail and quote by taking specific elements
            title = lines[0]
            quote = lines[3]
            # Appends the elements to lists
            titles.append(title)
            quotes.append(quote)
    kindle_df = pd.DataFrame({
        'Title': titles,
        'Quotes':quotes
    })

    kindle_clip = kindle_df.sample(n=1)
    
    return kindle_clip['Quotes'].values[0]
