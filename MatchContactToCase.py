import csv

csv.register_dialect('addQuoteDialect',
quoting = csv.QUOTE_ALL,
skipinitialspace = True)

case_file_path = '../Case.csv'
contact_file_path = '../Contact.csv'

def main():
    # Open contact csv file and create dictionary
    with open(contact_file_path, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        contact_data = [row for row in reader]

    contact_dictionary = create_dictionary(contact_data)

    # Open case csv file
    with open(case_file_path, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        case_data = [row for row in reader]

    # Get column indexes to be used in for loop
    firstname_column = get_col_number('FirstName', contact_data)
    lastname_column = get_col_number('LastName', contact_data)
    middlename_column = get_col_number('MiddleName', contact_data)
    mailingstreet_column = get_col_number('MailingStreet', contact_data)
    mailingcity_column = get_col_number('MailingCity', contact_data)
    mailingstate_column = get_col_number('MailingState', contact_data)
    mailingpostalcode_column = get_col_number('MailingPostalCode', contact_data)
    phone_column = get_col_number('Phone', contact_data)
    fax_column = get_col_number('Fax', contact_data)
    mobilephone_column = get_col_number('MobilePhone', contact_data)
    homephone_column = get_col_number('HomePhone', contact_data)
    otherphone_column = get_col_number('OtherPhone', contact_data)
    email_column = get_col_number('Email', contact_data)
    businessemail_column = get_col_number('Business_Email__c', contact_data)
    title_column = get_col_number('Title', contact_data)
    district_column = get_col_number('District__c', contact_data)

    # For each case, get the contact id from the case and corresponding contact information from contact dictionary
    for i in range(len(case_data)):
        contact_id = get_value(i, get_col_number('ContactId', case_data), case_data)
        #find contactId in contact_dictionary
        contact = (contact_dictionary.get(contact_id))
        if contact:
            #set contact fields to be written to new file
            firstname = contact[firstname_column]
            lastname = contact[lastname_column]
            casenumber = case_data[i][get_col_number('CaseNumber', case_data)]
            #print(contact[32])
            print(firstname + " " + lastname + " " + casenumber)

def get_value(row, col, data) -> str:
        return(data[row][col])

def get_col_number(col_header, data) -> int:
        for row in data:
            if row.index(col_header) + 1:
                colNumber = row.index(col_header)
                return colNumber
            else:
                print("Column col_header not found")
                break

def create_dictionary(data) -> dict:
    dictionary = {}
    for i in range(1, len(data)):
        key = get_value(i, get_col_number('Id',data), data)
        dictionary[key] = list(data[i])
    return dictionary

main()
