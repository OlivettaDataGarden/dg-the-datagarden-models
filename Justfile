import "/Users/maartenderuyter/Documents/dg-development/dg_justfile/Justfile"

# Local vars:
IS_PACKAGE := "true"
COMMIT_PREFIX := "DGDM"
REPO_NAME := "dg-the-datagarden-models"


tox:
    uv run tox
