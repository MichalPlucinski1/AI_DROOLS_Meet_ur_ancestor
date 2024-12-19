import re

# Data structure kindly provided by ChatGPT :)
# Which is why it's not correct at all
decision_tree = {
    "My favorite thing to do is": {
        "answers": {
            "MATE": {"next_question": "Hit it & Quit it ?", "answers": ["Yes", "No"]},
            "RUN": {"next_question": "How fast?", "answers": ["Yes", "No"]},
            "SWIM": {
                "next_question": "Where?",
                "answers": ["The Sand", "In the Shallows", "The Deep Blue Sea"],
            },
            "EAT": {"next_question": "Do you kill it?", "answers": ["Yes", "No"]},
            "SLEEP": {"next_question": "Are you cuddly?", "answers": ["Yes", "No"]},
            "I don't understand this chart": {
                "next_question": "",
                "answers": {
                    "It's ok noone expects you to": {
                        "next_question": "Belgium Sheep",
                        "answers": [],
                    }
                },
            },
        }
    },
    # MATE
    "Hit it & Quit it ?": {
        "answers": {
            "Yes": {"next_question": "Bottlenose Dolphin", "answers": []},
            "No": {
                "next_question": "Are you a stay at home dad?",
                "answers": ["Yes", "No"],
            },
        }
    },
    "Are you a stay at home dad?": {
        "answers": {
            "Yes": {"next_question": "Pygmy Seahorse", "answers": []},
            "No": {"next_question": "Turtle Dove", "answers": []},
        }
    },
    # SWIM
    "Where?": {
        "answers": {
            "The Sand": {"next_question": "Desert Monitor", "answers": []},
            "In the Shallows": {
                "next_question": "",
                "answers": {
                    "Sidewalk Puddles": {
                        "next_question": "Do you eat french fries?",
                        "answers": ["Yes, and pretzels", "No"],
                    },
                    "Ponds & Lakes": {
                        "next_question": "How's your buoyancy",
                        "answers": ["I sink like a rock", "I couldn't sink if I tried"],
                    },
                    "Rivers & Streams": {
                        "next_question": "Recreationally?",
                        "answers": ["I like to goof around", "I can be pretty intense"],
                    },
                },
            },
            "The Deep Blue Sea": {"next_question": "Alone?", "answers": ["Yes", "No"]},
            "No, the Deep Blue Sea": {
                "next_question": "Are you scary?",
                "answers": ["Yes", "No"],
            },
        }
    },
    "No, the Deep Blue Sea": {
        "answers": {
            "Yes": {
                "next_question": "Which do you have more of?",
                "answers": ["Teeth", "Appendages"],
            },
            "No": {
                "next_question": "Which do you have more of?",
                "answers": ["Teeth", "Appendages"],
            },
        }
    },
    "Which do you have more of?": {
        "answers": {
            "Teeth": {"next_question": "Viperfish", "answers": []},
            "Appendages": {"next_question": "Giant Squid", "answers": []},
        }
    },
    "Do you eat french fries?": {
        "answers": {
            "Yes, and pretzels": {"next_question": "Feral Pigeon", "answers": []},
            "No": {"next_question": "Propably Algae", "answers": []},
        }
    },
    "How's your buoyancy": {
        "answers": {
            "I sink like a rock": {
                "next_question": "Thick Shelled River Mussel",
                "answers": [],
            },
            "I couldn't sink if I tried": {
                "next_question": "Lesser Snow Goose",
                "answers": [],
            },
        }
    },
    "Recreationally?": {
        "answers": {
            "I like to goof around": {
                "next_question": "Eurasian River Otter",
                "answers": [],
            },
            "I can be pretty intense": {"next_question": "Red Piranha", "answers": []},
        }
    },
    "Alone?": {
        "answers": {
            "Yes": {"next_question": "Bummer why?", "answers": ["Because I'm mean"]},
            "No": {
                "next_question": "With who?",
                "answers": ["My Life Mate", "All 15 000 of my facebook friends"],
            },
        }
    },
    "Bummer why?": {
        "answers": {
            "Because I'm mean": {"next_question": "Bull Shark", "answers": []},
            "Because I feel invinsible": {
                "next_question": "Transparent Jellyfish",
                "answers": [],
            },
        }
    },
    "With who?": {
        "answers": {
            "My Life Mate": {"next_question": "French Angelfish", "answers": []},
            "All 15 000 of my facebook friends": {
                "next_question": "Yellow Tang",
                "answers": [],
            },
        }
    },
    # running
    "How fast?": {
        "answers": {
            "I'm pretty quick": {
                "next_question": "Mostly indoors?",
                "answers": ["Yes", "No"],
            },
            "So fast I fly": {"next_question": "Literally?", "answers": ["Yes", "No"]},
            "Kidding, I walk.": {
                "next_question": "With Haste?",
                "answers": ["Yes", "No"],
            },
        }
    },
    "Mostly indoors?": {
        "answers": {
            "Yes": {
                "next_question": "Do you own or rent",
                "answers": [
                    "If I pee on it, I own it, right?",
                    "I'm between floors at the moment",
                ],
            },
            "No": {
                "next_question": "What's on your ipod",
                "answers": ['"My old kentucky home"', "Hakuna matata"],
            },
        }
    },
    "Do you own or rent": {
        "answers": {
            "If I pee on it, I own it, right?": {
                "next_question": "Mniature Schnauzer",
                "answers": [],
            },
            "I'm between floors at the moment": {
                "next_question": "Cockroach",
                "answers": [],
            },
        }
    },
    "What's on your ipod": {
        "answers": {
            '"My old kentucky home"': {"next_question": "Quarterhorse", "answers": []},
            "Hakuna matata": {"next_question": "African lion", "answers": []},
        }
    },
    "Literally?": {
        "answers": {
            "Yes": {"next_question": "Peregrine falcon?", "answers": []},
            "No": {
                "next_question": "How so, then?",
                "answers": [
                    "In my dreams",
                    "Metaphoricly",
                ],
            },
        }
    },
    "How so, then?": {
        "answers": {
            "In my dreams": {"next_question": "Tanzania ostrich", "answers": []},
            "Metaphoricly": {"next_question": "Cheetah", "answers": []},
        }
    },
    # belgium sheep
    # eating
    "What?": {
        "answers": {
            "No meat": {"next_question": "Are you a hippie?", "answers": ["Yes", "No"]},
            "Eh, I'm not that picky": {
                "next_question": "Would you climb a tree to get it?",
                "answers": ["Yes", "No"],
            },
            "Things with blood": {
                "next_question": "Do you kill it?",
                "answers": ["Yes", "No"],
            },
        }
    },
    "Are you a hippie?": {
        "answers": {
            "Yes": {
                "next_question": "Rockin' the beard?",
                "answers": ["Full-body", "I'm more into tats"],
            },
            "No": {
                "next_question": "How do you vote?",
                "answers": ["For the underground movement", "For guns"],
            },
        }
    },
    "Rockin' the beard?": {
        "answers": {
            "Full-body": {"next_question": "Wooly yak", "answers": []},
            "I'm more into tats": {"next_question": "Grant's Zebra", "answers": []},
        }
    },
    "How do you vote?": {
        "answers": {
            "For the underground movement": {
                "next_question": "Garden worm",
                "answers": [],
            },
            "For guns": {"next_question": "African elephant", "answers": []},
        }
    },
    # worm
    # elephant
    # eating, not that picky
    "Would you climb a tree to get it?": {
        "answers": {
            "Yes": {
                "next_question": "How quickly?",
                "answers": ["Faster then you'd think", "Slower then you'd think"],
            },
            "No": {
                "next_question": "Why so lazy?",
                "answers": ["I need 9 months of beauty sleep", "Trash cans are easier"],
            },
        }
    },
    "How quickly?": {
        "answers": {
            "Faster then you'd think": {
                "next_question": "Himalayan black bear",
                "answers": [],
            },
            "Slower then you'd think": {
                "next_question": "Two-toed sloth?",
                "answers": [],
            },
        }
    },
    # sloth
    "Why so lazy?": {
        "answers": {
            "I need 9 months of beauty sleep": {
                "next_question": "Alpine marmot",
                "answers": [],
            },
            "Trash cans are easier": {
                "next_question": "Northern raccoon",
                "answers": [],
            },
        }
    },
    # eat things with blood
    "Do you kill it?": {
        "answers": {
            "Yes": {
                "next_question": "How long does it take?",
                "answers": [
                    "A Few Seconds",
                    "Hours",
                    "I tie it up back and kill it later",
                ],
            },
            "No": {
                "next_question": "Why Not?",
                "answers": ["'Cuz Someone Else Does", "I like my steak extra rare"],
            },
        }
    },
    "Why Not?": {
        "answers": {
            "'Cuz Someone Else Does": {
                "next_question": "Ruppell's Griffin Vulture",
                "answers": [],
            },
            "I like my steak extra rare": {
                "next_question": "Ruppell's Griffin Vulture",
                "answers": [],
            },
        }
    },
    "How long does it take?": {
        "answers": {
            "A Few Seconds": {"next_question": "Saltwater Crocodile", "answers": []},
            "Hours": {"next_question": "Burmese python", "answers": []},
            "I tie it up back and kill it later": {
                "next_question": "Black widow spider",
                "answers": [],
            },
        }
    },
    # sleeping
    "'Cuz you work the graveyard shift?": {
        "answers": {
            "Yes": {"next_question": "Brown Bat", "answers": []},
            "No": {
                "next_question": "Are you cuddly?",
                "answers": [
                    "My mother say I am",
                    "People other than my mother say I am",
                ],
            },
        }
    },
    "Are you cuddly?": {
        "answers": {
            "My mother say I am": {"next_question": "Giant Armadillo", "answers": []},
            "People other than my mother say I am": {
                "next_question": "Koala bear",
                "answers": [""],
            },
        }
    },
}

with open("rules.drl", "w") as f:
    q_num = 0
    r_num = 0
    step_question = 0
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
                if next_question == "":
                    step_question += 1
                    f.write(f'rule "SQ_{step_question}"\n')
                    f.write("    when\n")
                    f.write(
                        f'        Response(question == "{question}", answer == "{answer}")\n'
                    )
                    f.write("    then\n")
                    f.write(
                        f'        Knowledge k = new Knowledge("{next_question}", new String[]{{{", ".join([f'"{a}"' for a in answers])}}});\n'
                    )
                    f.write(
                        f"        ui.questionScreen(k.getQuestion(), k.getAnswers());\n"
                    )
                    f.write("end\n\n")
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
                        f"        ui.questionScreen(k.getQuestion(), k.getAnswers());\n"
                    )
                    f.write("end\n\n")

for image in images_to_get:
    print(f"Get image: {image}")
