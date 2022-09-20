# CHange text e.g.
# Transformation Text ==> transformation text




def transform(text: str) -> str:
    return text.replace(' ', '_').lower()


def main():
    text = 'Allow the use of cookies from Instagram on this browser?'
    print(transform(text))




if __name__ == "__main__":
    main()