import re
import sys
from pathlib import Path


# >>> Optionally clearing comments
COMMENTS_STRUCTURE = {
   "{{cookiecutter.action_name}}.yaml": r"(\s*#.*)",
}
PRESERVE_HINTS_VARIANS = {
    "yes": True,
    "y": True,
    "true": True,
    "no": False,
    "n": False,
    "false": False,
}
PRESERVE_HINTS_ANSWER = (
    "{{ cookiecutter['preserve action template hints'] | lower }}"
)
if PRESERVE_HINTS_ANSWER not in PRESERVE_HINTS_VARIANS:
    print(
        f"ERROR: '{PRESERVE_HINTS_ANSWER}' is not a valid answer, "
        f"please select one among [{', '.join(PRESERVE_HINTS_VARIANS)}]."
    )
    sys.exit(1)
else:
    if not PRESERVE_HINTS_VARIANS[PRESERVE_HINTS_ANSWER]:
        for f_name in COMMENTS_STRUCTURE:
            f_path = Path(f_name)
            if not f_path.exists():
                print(f"WARNING: skipping comments removal from file {f_name}")
            else:
                content = f_path.read_text().splitlines(keepends=True)
                result = []
                for line in content:
                    if not re.match(COMMENTS_STRUCTURE[f_name], line):
                        result.append(line)
                f_path.write_text("".join(result))
# <<< Optionally clearing comments
