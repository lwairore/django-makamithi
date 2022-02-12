# You can find the most common open graph website types on the open graph webpage: https://ogp.me/#types

ARTICLE_VALUES = (
    ('article', 'Article'),
    ('article:published_time',
     'Article - Published Time - When the article was first published.'),
    ('article:modified_time',
     'Article - Modified Time - When the article was last changed.'),
    ('article:expiration_time',
     'Article - Expiration Time - When the article is out of date after.'),
    ('article:author', 'Article - Author - Writers of the article.'),
    ('article:section',
     'Article - Article - Section - A high-level section name. E.g. Technology'),
    ('article:tag', 'Article - Tag -Tag words associated with this article.')
)

BOOK_VALUES = (
    ('book', 'Book'),
    ('book:isbn', 'Book - ISBN - The ISBN'),
    ('book:release_date', 'Book - Release date - The date the book was released.'),
    ('book:tag', 'Book - Tag - Tag words associated with this book.')
)

PROFILE_VALUES = (
    ('profile', 'Profile'),
    ('profile:first_name', 'Profile - First Name - A name normally given to an individual by a parent or self-chosen.'),
    ('profile:last_name', 'Profile - Last Name - A name inherited from a family or marriage and by which the individual is commonly known.'),
    ('profile:username', 'Profile - Username - A short unique string to identify them.'),
    ('profile:gender', 'Profile - Gender - (male, female) - Their gender.')
)
