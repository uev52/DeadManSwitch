import csv
with open("pysimplegui.csv") as bestand:
    inhoud = csv.DictReader(bestand)

    tweets = {}
    for rij in inhoud:
        # datum toevoegen aan tweets als key
        datum = rij['PostDate']
        datum = datum.split('T')
        datum = datum[0]

        # de tweet inhoud toevoegen aan tweets als value
        bericht = rij['TweetText']

        tweets[datum]=bericht

        print(tweets)
