# CHange text e.g.
# Transformation Text ==> transformation text


def transform(text: str) -> str:
    return text.replace(' ', '_').lower()


def main():
    text = 'no selected name'
    print(transform(text))


if __name__ == "__main__":
    main()
