import urllib

def read_text():
    quotes = open("C:\Users\ppppp\Desktop\python\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document does not have any curse words.")
    else:
        print("Could not scan the document properly.")

##def read_text_pirate():
##    quotes = open("C:\Users\ppppp\Desktop\python\movie_quotes.txt")
##    contents_of_file = quotes.read()
##    print(contents_of_file)
##    quotes.close()
##    convert_to_pirate(contents_of_file)
##
##
##def convert_to_pirate(text_to_convert):
##    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_convert)
##    output = connection.read()
##    print(output)
##    connection.close()

read_text()
