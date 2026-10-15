# Arbitrary Keyword Arguments (**kwargs)

def display_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_details(
    name="Samarth",
    course="AIML",
    language="Python"
)
