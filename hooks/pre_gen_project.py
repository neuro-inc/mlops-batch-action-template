import re
import sys
from pathlib import Path

# Test action name
ACTION_NAME = "{{ cookiecutter.action_name }}"

FULL_ACTION_DIR = Path(".").resolve().with_name(ACTION_NAME)
FORBIDDEN_CHARS = r'<>:"\/|?*'

forbidden_chars_in_dir_name = set(ACTION_NAME) & set(FORBIDDEN_CHARS)

if forbidden_chars_in_dir_name:
    print(f"ERROR: '{ACTION_NAME}' contains forbidden chars ({FORBIDDEN_CHARS})")
    sys.exit(1)
elif not FULL_ACTION_DIR.exists():
    try:
        FULL_ACTION_DIR.mkdir(parents=True)
        FULL_ACTION_DIR.rmdir()
    except Exception:
        print(
            f"ERROR: '{FULL_ACTION_DIR}' is not a valid action directory name "
            ", OS cannot create it. Use action name without forbidden chars."
        )
        sys.exit(1)

action_task_id = "{{ cookiecutter.action_task_id }}"
if not action_task_id.isidentifier():
    print(
        f"ERROR: '{action_task_id}' is not a valid action task identifier. "
        "It can only contain alphanumeric letters (a-zA-Z0-9), or underscores (_), "
        "and cannot start with a number, or contain any spaces."
    )
    sys.exit(1)


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
code_dir_name = "{{ cookiecutter.action_code_directory }}"

if not re.match(MODULE_REGEX, code_dir_name):
    print(
        "ERROR: %s is not a valid Python module name. Module name can only contain "
        "letters, digits, and underscores." % code_dir_name
    )
    sys.exit(1)
