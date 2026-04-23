import json

# ---------- LOAD TREE ----------
with open("reflection-tree.json", encoding = "utf-8") as f:
    nodes = {n["id"]: n for n in json.load(f)}

# ---------- STATE ----------
state = {
    "axis1_internal": 0,
    "axis1_external": 0,
    "axis2_contribution": 0,
    "axis2_entitlement": 0,
    "axis2_neutral": 0,
    "axis3_self": 0,
    "axis3_other": 0
}

answers = {}

# ---------- HELPERS ----------
def get_dominant(axis_prefix):
    filtered = {k: v for k, v in state.items() if k.startswith(axis_prefix)}

    values = list(filtered.values())

    # if all values same → mixed
    if len(set(values)) == 1:
        return "mixed"

    return max(filtered, key=filtered.get).split("_")[1]

def render(text):
    # replace answers
    for k, v in answers.items():
        text = text.replace(f"{{{k}}}", v)

    # replace axis dominance
    text = text.replace("{axis1.dominant}", get_dominant("axis1"))
    text = text.replace("{axis2.dominant}", get_dominant("axis2"))
    text = text.replace("{axis3.dominant}", get_dominant("axis3"))

    return text


# ---------- RUN ----------
current = "START"
steps = 0
MAX_STEPS = 100 # safety limit

while current:
    steps += 1

    if steps > MAX_STEPS:
        print("Error: Too many steps (possible loop).")
        break

    node = nodes.get(current)

    if not node:
        print("Error: Node not found:", current)
        break

    # print text
    if "text" in node:
        print("\n" + render(node["text"]))

    if node["type"] == "end":
        break

    elif node["type"] == "question":
        options = node["options"]

        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")

        while True:
            user_input = input("Choose option: ")

            if not user_input.isdigit():
                print("Please enter a valid number.")
                continue

            choice = int(user_input) - 1

            if choice < 0 or choice >= len(options):
                print(f"Please choose between 1 and {len(options)}.")
                continue

            selected = options[choice]
            answers[current] = selected
            break

        # apply signals
        if "signals" in node:
            signal = node["signals"].get(selected)
            if signal:
                state[signal] += 1

        current = node.get("next")

        if not current:
            print("Error: Missing 'next' in node:", node["id"])
            break

    elif node["type"] == "decision":

        # Axis-based decisions
        if node["id"] == "A1_BRANCH":
            key = get_dominant("axis1")

        elif node["id"] == "A2_BRANCH":
            key = get_dominant("axis2")

        elif node["id"] == "A3_BRANCH":
            key = get_dominant("axis3")

        else:
            # Answer-based decisions
            if not answers:
                print("Error: No previous answer found.")
                break

            last_q = list(answers.keys())[-1]
            key = answers[last_q]

        if key not in node["rules"]:
            print(f"Error: No rule for '{key}' at node {node['id']}")
            break

        current = node["rules"][key]

    else:
        # reflection, bridge, summary
        current = node.get("next")

        if not current:
            print("Error: Missing 'next' in node:", node["id"])
            break