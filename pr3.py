from datetime import date
import random
from typing import Tuple

QUOTES = [
	"Be yourself; everyone else is already taken. — Oscar Wilde",
	"The only way to do great work is to love what you do. — Steve Jobs",
	"Do what you can, with what you have, where you are. — Theodore Roosevelt",
	"Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill",
]


def today_and_quote() -> Tuple[str, str]:
	"""Return today's date (YYYY-MM-DD) and a random quote.

	Returns:
		(date_str, quote)
	"""
	today = date.today().isoformat()
	quote = random.choice(QUOTES)
	return today, quote


if __name__ == '__main__':
	d, q = today_and_quote()
	print(d)
	print(q)

