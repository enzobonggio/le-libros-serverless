default: make_fetch_categories make_fetch_books_by_category

make_fetch_categories:
	cd lambdas/fetch_categories && make

make_fetch_books_by_category:
	cd lambdas/fetch_books_by_category && make
