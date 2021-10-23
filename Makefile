install: install_fetch_categories install_fetch_books_by_category
test: test_fetch_categories test_fetch_books_by_category

install_fetch_categories:
	cd lambdas/fetch_categories && make install

install_fetch_books_by_category:
	cd lambdas/fetch_books_by_category && make install

test_fetch_categories:
	cd lambdas/fetch_categories && make test

test_fetch_books_by_category:
	cd lambdas/fetch_books_by_category && make test

