import streamlit as st
import openai
import random

st.title("Ad cre'AI'tor")

# product info
product_prompt = st.text_input("enter product info")
# name of the product
product_name_prompt = st.text_input("enter product name")
# audience selection
audience_prompt = st.selectbox(
    "Create audience",
    ["Child", "Young Adults", "Middle-aged Adults", "Old-aged Adults"],
    help="""Choose the input info of your audience""",
)
# features of the product
features_prompt = st.text_area(
    "enter product features", help="""enter product information by comma seperating"""
)

# api key
openai.api_key = "" # enter your api key here


def add_creator():
    indentation_op = []
    for i in range(5):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Write a creative ad for the following product to run on Facebook,instagram and linkedin aimed at {audience_prompt}:\n\
            \nProduct: {product_prompt} with product name {product_name_prompt} {features_prompt}",
            #   Learning Room is a virtual environment to help students from kindergarten to high school excel in school.
            temperature=0.5,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        # return response['choices'][0]['text']
        indentation_op.append(response["choices"][0]["text"])
    print(indentation_op)
    return indentation_op


with st.container():
    if st.button("Generate ad"):
        st.write(add_creator())

        # Add a next button and a previous button
        # page_number = 0
        # last_page = 10

        # prev, _ ,next = st.columns([1, 10, 1])

        # if next.button("Next"):

        #     if page_number + 1 > last_page:
        #         page_number = 0
        #     else:
        #         page_number += 1

        # if prev.button("Previous"):

        #     if page_number - 1 < 0:
        #         page_number = last_page
        #     else:
        #         page_number -= 1

        # # Get start and end indices of the next page of the dataframe

        # # Index into the sub dataframe
        # # Get start and end indices of the next page of the dataframe
        # start_idx = page_number
        # end_idx = (1 + page_number)

        # sub_df = add_creator()[start_idx:end_idx]
        # st.write(sub_df)
