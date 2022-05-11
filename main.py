import pandas as pd

pathToCSV = input('What is the name of qualtrics results CSV?\n')

qualtricsResultsDF = pd.read_csv(pathToCSV)

qualtricsResultsDF = qualtricsResultsDF.drop(columns=[
    'StartDate', 'EndDate', 'Status', 'IPAddress', 'Progress', 'Duration (in seconds)', 'Finished', 'RecordedDate', 
    'ResponseId', 'RecipientLastName', 'RecipientFirstName', 'RecipientEmail', 'ExternalReference', 'LocationLatitude',
    'LocationLongitude', 'DistributionChannel', 'UserLanguage'
])

qualtricsResultsDF = qualtricsResultsDF.drop(index=1)

qualtricsResultsDF = qualtricsResultsDF.fillna(value='N/A')

qualtricsResultsDF.to_excel('Qualtrics_Results.xlsx')