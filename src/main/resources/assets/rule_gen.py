import re

# Data structure kindly provided by ChatGPT :)
# Which is why it's not correct at all
decision_tree = {
    "My favorite thing to do is": {
        "answers": {
            "MATE": {"next_question": "Hit it & Quit it ?", "answers": ["Yes", "No"]},
            "RUN": {"next_question": "With Haste?", "answers": ["Yes", "No"]},
            "SWIM": {
                "next_question": "Where?",
                "answers": ["The Sand", "In the Shallows", "The Deep Blue Sea"],
            },
            "EAT": {"next_question": "Do you kill it?", "answers": ["Yes", "No"]},
            "SLEEP": {"next_question": "Are you cuddly?", "answers": ["Yes", "No"]},
        }
    },
    "Hit it & Quit it ?": {
        "answers": {
            "Yes": {"next_question": "Feral Pigeon", "answers": []},
            "No": {"next_question": "Pygmy Seahorse", "answers": []},
        }
    },
    "With Haste?": {
        "answers": {
            "Yes": {"next_question": "How's your posture?", "answers": ["Quasimodo"]},
            "No": {"next_question": "Galapagos Tortoise", "answers": []},
        }
    },
    "Where?": {
        "answers": {
            "The Sand": {"next_question": "Sidewalk Puddles", "answers": []},
            "In the Shallows": {
                "next_question": "Rivers & Streams",
                "answers": ["Recreationally?", "Yes", "No"],
            },
            "The Deep Blue Sea": {"next_question": "Alone?", "answers": ["Yes", "No"]},
        }
    },
    "Do you kill it?": {
        "answers": {
            "Yes": {
                "next_question": "How long does it take?",
                "answers": ["A Few Seconds", "Hours"],
            },
            "No": {"next_question": "Why Not?", "answers": ["'Cuz Someone Else Does"]},
        }
    },
    "Are you cuddly?": {
        "answers": {
            "Yes": {"next_question": "Giant Squid", "answers": ["Appendages"]},
            "No": {
                "next_question": "Transparent Jellyfish",
                "answers": ["'Cuz You Work the Graveyard Shift?"],
            },
        }
    },
    "How's your posture?": {
        "answers": {
            "Quasimodo": {"next_question": "Silverback Gorilla", "answers": []},
        }
    },
    "Alone?": {
        "answers": {
            "Yes": {"next_question": "Are you scary?", "answers": ["Yes", "No"]},
            "No": {"next_question": "French Angelfish", "answers": ["My Life Mate"]},
        }
    },
    "Are you scary?": {
        "answers": {
            "Yes": {
                "next_question": "Which do you have more of?",
                "answers": ["Teeth", "Appendages"],
            },
            "No": {"next_question": "Yellowtail Barracuda", "answers": []},
        }
    },
    "How long does it take?": {
        "answers": {
            "A Few Seconds": {"next_question": "Saltwater Crocodile", "answers": []},
            "Hours": {"next_question": "Brown Bat", "answers": []},
        }
    },
    "Recreationally?": {
        "answers": {
            "Yes": {"next_question": "Red Piranha", "answers": []},
            "No": {"next_question": "Bottlenose Dolphin", "answers": []},
        }
    },
    "Why Not?": {
        "answers": {
            "'Cuz Someone Else Does": {
                "next_question": "Ruppell's Griffin Vulture",
                "answers": [],
            },
        }
    },
    "'Cuz You Work the Graveyard Shift?": {
        "answers": {
            "Yes": {"next_question": "Giant Squid", "answers": []},
        }
    },
    "Which do you have more of?": {
        "answers": {
            "Teeth": {"next_question": "Viperfish", "answers": []},
            "Appendages": {"next_question": "Giant Squid", "answers": []},
        }
    },
}

with open("rules.drl", "w") as f:
    q_num = 0
    r_num = 0
    images_to_get = []
    for question, data in decision_tree.items():
        for answer, outcome in data["answers"].items():
            q_num += 1
            next_question = outcome["next_question"]
            answers = outcome["answers"]
            if len(answers) == 0:
                r_num += 1
                f.write(f'rule "R_{r_num}"\n')
                f.write("    when\n")
                f.write(
                    f'        Response(question == "{question}", answer == "{answer}")\n'
                )
                f.write("    then\n")
                f.write(f'        Result r = new Result("{next_question}");\n')
                f.write(f"        ui.resultScreen(r.getResult());\n")
                f.write("end\n\n")
                filename = (
                    re.sub(r"[^a-z0-9]", "_", next_question.strip().lower()) + ".jpg"
                )
                images_to_get.append(filename)
            else:
                f.write(f'rule "Q_{q_num}"\n')
                f.write("    when\n")
                f.write(
                    f'        Response(question == "{question}", answer == "{answer}")\n'
                )
                f.write("    then\n")
                f.write(
                    f'        Knowledge k = new Knowledge("{next_question}", new String[]{{{", ".join([f'"{a}"' for a in answers])}}});\n'
                )
                f.write(
                    f"        String res = ui.questionScreen(k.getQuestion(), k.getAnswers());\n"
                )
                f.write("end\n\n")

for image in images_to_get:
    print(f"Get image: {image}")
