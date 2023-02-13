import pandas as pd

import sheetslib as sl

from email_builder import molly_email
from email_builder import duncan_email

# import sheetsformatlib as sfl

# from csvhandler import get_csvs_from_input_folder

# from googleapiclient.errors import HttpError

# The ID of the main spreadsheet
spreadsheet_id = '1mLInhGR4zrkH2BbNZBEtyTqfZuV33od2ZG_JmaMDpOQ' #TOEDIT

our_link = "https://www.memberstack.com/blog/using-custom-code-in-webflow" #TOEDIT

if __name__ == '__main__':
    creds, service = sl.authorize()

print(creds, service)

response = sl.read_values(spreadsheet_id, "Link Building Prospects", service)

# print(response)

df = pd.DataFrame(response[1:], columns=response[0])

print(df.info())

df["Email"] = df.apply(lambda row: duncan_email(row["Recipient"], row["Content URL"], row["Topic"], our_link, row["Anchor Text"], row["Reciprocical"]), axis="columns")

print(df.tail())

print(df["Recipient"].values.tolist())

body = df["Email"].values.tolist()
body = [[item] for item in body]

sl.update_values(spreadsheet_id, "Link Building Prospects!P2:P43", "USER_ENTERED", body, service) #TOEDIT