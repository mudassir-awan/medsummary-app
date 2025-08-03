from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# def get_summary(text):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a helpful assistant that summarizes medical reports in simple terms."
#             },
#             {
#                 "role": "user",
#                 "content": f"Summarize this medical report:\n{text}"
#             }
#         ],
#         max_tokens=300,       # Limit output length
#         temperature=0         # Deterministic output (no creativity)
#     )
#     return response.choices[0].message.content


def get_summary(text):
    prompt = f"""
Summarize the following medical report in three parts:
1. Patient Condition
2. Key Findings
3. Recommended Treatment

Medical Report:
{text}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes medical reports for doctors and patients."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=100,
        temperature=0
    )
    return response.choices[0].message.content
