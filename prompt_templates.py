FEEDBACK_PROMPT_TEMPLATE = """
Classify the following student feedback into one of the categories:
"Academics", "Facilities", or "Administration".

Feedback: "The Wi-Fi in the library has been down all week."
Category: Facilities

Feedback: "Professors in the data science department are really helpful."
Category: Academics

Feedback: "There was a delay in issuing the fee refund."
Category: Administration

Feedback: "The cafeteria food quality has improved lately."
Category: Facilities

Feedback: "{feedback}"
Category:
"""
