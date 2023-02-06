import pandas as pd

import sheetslib as sl

from email_builder import molly_email

# import sheetsformatlib as sfl

# from csvhandler import get_csvs_from_input_folder

# from googleapiclient.errors import HttpError

# The ID of the main spreadsheet
spreadsheet_id = '1_TFwhDWEbNOHqyUy_6GDtEEjdTTpbsCrc9QI67nP3Zo'

our_link = "https://www.memberstack.com/blog/cloneable-webflow-parallax-animation-templates"

if __name__ == '__main__':
    creds, service = sl.authorize()

print(creds, service)

response = sl.read_values(spreadsheet_id, "Link Building Prospects", service)

# print(response)

df = pd.DataFrame(response[1:], columns=response[0])

print(df.info())

df["Email"] = df.apply(lambda row: molly_email(row["Recipient"], row["Content URL"], row["Topic"], our_link, row["Anchor Text"]), axis="columns")

print(df.tail())

print(df["Recipient"].values.tolist())

body = df["Email"].values.tolist()
body = [[item] for item in body]

sl.update_values(spreadsheet_id, "Link Building Prospects!P2:P26", "USER_ENTERED", body, service)