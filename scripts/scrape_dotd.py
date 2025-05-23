#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def find_h3_in_sections(url: str) -> list:
    """Find all h3 elements inside divs within sections with the specified class and return their text."""
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        sections = soup.find_all(
            "section",
            class_=(
                "mx-auto max-w-full mobile:max-w-[480px] tablet:max-w-[768px] "
                "laptop:max-w-[986px] desktop:max-w-[1320px] px-[10px] "
                "laptop:px-[10px] desktop:px-[10px] font-titillium text-17 "
                "leading-[23px] border-0"
            ),
        )

        h3_texts = []
        for section in sections:
            # Find all divs in the section
            divs = section.find_all("div")
            for div in divs:
                # Find h3s in each div
                h3s = div.find_all("h3")
                for h3 in h3s:
                    h3_texts.append(h3.text.strip())

        return h3_texts

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []


if __name__ == "__main__":
    url = "https://www.formula1.com/en/latest/article/driver-of-the-day-2021.78AqC4wM6NVtaNH1mZA4on"

    h3_texts = find_h3_in_sections(url)

    print("\nH3 elements found in divs within sections:")
    print("-" * 50)
    for i, text in enumerate(h3_texts, 1):
        print(f"{i}. {text}")
        print("-" * 50)
