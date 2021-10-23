install: install_fetch_categories install_fetch_books_by_category
requirements: requirements_fetch_categories requirements_fetch_books_by_category

install_fetch_categories:
	cd lambdas/fetch_categories && make install

install_fetch_books_by_category:
	cd lambdas/fetch_books_by_category && make install

requirements_fetch_categories:
	cd lambdas/fetch_categories && make requirements

requirements_fetch_books_by_category:
	cd lambdas/fetch_books_by_category && make requirements
